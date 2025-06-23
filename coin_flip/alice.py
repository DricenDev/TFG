import random
import sys

from shared.communication import send_data, receive_data
from shared.communication import send_qubits, recieve_qubits
from shared.quantum       import encode_qubits, measure_qubits

# Constants
NUM_QUBITS = 20

# Step 1: Select a random base
alice_base = random.choice(['C', 'H'])
print("Alice's base:")
print(alice_base)

# Step 2: Select random bits
bit_array = [str(random.randint(0, 1)) for _ in range(NUM_QUBITS)]
print("Alice's random bits:")
print(bit_array)

# Step 3: Initialize each qubit
qc_array = encode_qubits(bit_array, [alice_base]*NUM_QUBITS)

# Step 4: Send qubits to Bob
send_qubits(qc_array, 'coin_flip_bob')

# Step 5: Receive Bob's base
bob_base = receive_data('coin_flip_alice')

# Step 6: Send Bob the base
send_data(alice_base, 'coin_flip_bob')

# Step 7: Send Bob the bits
send_data(bit_array, 'coin_flip_bob')

# Step 8: Say who won
if alice_base == bob_base:
    print("Bob WON!")
else:
    print("Alice WON!")
