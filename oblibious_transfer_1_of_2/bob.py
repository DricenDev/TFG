import random
import sys

from shared.communication import send_data, receive_data
from shared.communication import send_qubits, recieve_qubits
from shared.quantum       import encode_qubits, measure_qubits

# Step 1: Receive qubits from Alice
qc_array = recieve_qubits('oblibious_transfer_bob')
NUM_QUBITS = len(qc_array)

# Step 2: Select random bases
base_array = [random.choice(['C', 'H']) for _ in range(NUM_QUBITS)]
print("Bob's bases:")
print(base_array)

# Step 3: Measure qubits
for i in range(NUM_QUBITS):
    if base_array[i] == 'H':
        qc_array[i].h(0)
results = measure_qubits(qc_array)
print("Bob's bits:")
print(results)

# Step 4: Receive bases from Alice
alice_bases = receive_data('oblibious_transfer_bob')

# Step 5: Divide bits in two groups, rigth and random
group_ok = []
group_random = []
for i in range(0, NUM_QUBITS):
    if base_array[i] == alice_bases[i]:
        group_ok += [i]
    else:
        group_random += [i]
print('Ok group: ')
print(group_ok)
print('Random group: ')
print(group_random)

# Step 6: Send Alice the indexes of each group
if random.choice([True, False]): groups = [group_ok, group_random]
else:                            groups = [group_random, group_ok]
send_data(groups, 'oblibious_transfer_alice')

# Step 7: Recieve Alice bits
bits_dictionary = receive_data('oblibious_transfer_bob')
print('Bits received:')
print(bits_dictionary)

# Step 8: Decode the completed half
secret_bit_array = []
if (group_random[0] in bits_dictionary or group_random[0] >= NUM_QUBITS//2):
    for i in range(0, NUM_QUBITS//2):
        if i in group_ok:
            secret_bit_array += results[i]
        else:
            secret_bit_array += bits_dictionary[i]
else: 
    for i in range(NUM_QUBITS//2, NUM_QUBITS):
        if i in group_ok:
            secret_bit_array += results[i]
        else:
            secret_bit_array += bits_dictionary[i]
secret = ''.join(chr(int(''.join(secret_bit_array[i:i+8]), 2)) for i in range(0, len(secret_bit_array), 8))
print('Decoded secret:')
print(secret)
