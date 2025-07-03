import random
import time
import sys

from shared.communication import send_data, receive_data
from shared.communication import send_qubits, recieve_qubits
from shared.quantum       import encode_qubits, measure_qubits

# Constants
secret_1 = "clave1234"
secret_2 = "S3cr3t!"
secret_1_size = len(secret_1)
secret_2_size = len(secret_2)
if secret_1_size > secret_2_size: NUM_QUBITS = secret_1_size*2*8
else                            : NUM_QUBITS = secret_2_size*2*8

# Step 1: Encode the secret in binary
if secret_1_size < secret_2_size: secret_1 += " "*(secret_2_size - secret_1_size) # Fill with space the smallest one
else                            : secret_2 += " "*(secret_1_size - secret_2_size) # so both are same size
secret_1_bits = [bit for char in secret_1 for bit in format(ord(char), '08b')]
secret_2_bits = [bit for char in secret_2 for bit in format(ord(char), '08b')]
bit_array = secret_1_bits + secret_2_bits
print('Alice encoded secrets:')
print(bit_array)

# Step 2: Select a random bases
base_array = [random.choice(['C', 'H']) for _ in range(NUM_QUBITS)]
print("Alice's bases:")
print(base_array)

# Step 3: Initialize each qubit
qc_array = encode_qubits(bit_array, base_array)

# Step 4: Send qubits to Bob
send_qubits(qc_array, 'oblibious_transfer_bob')

# Step 5: Wait for Bob to measure
time.sleep(1) # A time long enough so qubits would lose coherence

# Step 6: Send Bob the bases
send_data(base_array, 'oblibious_transfer_bob')

# Step 7: Receive Bob indexes
group_a, group_b = receive_data('oblibious_transfer_alice')

# Step 8: Send Bob the values for one group on the first half and for the other group on the second half
bits_dictionary = {}
if random.choice([True, False]):
    for i in range(0, NUM_QUBITS//2):
        if i in group_a:
            bits_dictionary[i] = bit_array[i]
    for i in range(NUM_QUBITS//2, NUM_QUBITS):
        if i in group_b:
            bits_dictionary[i] = bit_array[i]
else:
    for i in range(0, NUM_QUBITS//2):
        if i in group_b:
            bits_dictionary[i] = bit_array[i]
    for i in range(NUM_QUBITS//2, NUM_QUBITS):
        if i in group_a:
            bits_dictionary[i] = bit_array[i]
send_data(bits_dictionary, 'oblibious_transfer_bob')
