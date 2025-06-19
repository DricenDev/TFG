import random
import time
import sys

from shared.communication import send_data, receive_data
from shared.communication import send_qubits, recieve_qubits
from shared.quantum       import run, QuantumCircuit

# Constants
NUM_QUBITS = 20

# Step 1: Select a random base
alice_base = random.choice(['Computational', 'Hadamard'])
print("Alice's base:")
print(alice_base)

# Step 2: Select random bits
bit_array = [str(random.randint(0, 1)) for _ in range(NUM_QUBITS)]
print("Alice's random bits:")
print(bit_array)

# Step 3: Initialize each qubit
qc_array = [QuantumCircuit(1) for _ in range(NUM_QUBITS)]
for i in range(NUM_QUBITS):
    if alice_base == 'Computational':
        if bit_array[i] == '1':
            qc_array[i].x(0)
    if alice_base == 'Hadamard':
        if bit_array[i] == '1':
            qc_array[i].x(0)
            qc_array[i].h(0)
        else:
            qc_array[i].h(0)

# Step 4: Send qubits to Bob
time.sleep(3) # Ensure Bob is ready to receive
send_qubits(qc_array, 'coin_flip_bob')

# Step 5: Receive Bob's base
bob_base = receive_data('coin_flip_alice')

# Step 6: Send Bob the base
time.sleep(3) # Ensure Bob is ready to receive
send_data(alice_base, 'coin_flip_bob')

# Step 7: Send Bob the bits
time.sleep(5)  # Ensure Bob is ready to receive
send_data(bit_array, 'coin_flip_bob')

# Step 8: Say who won
if alice_base == bob_base:
    print("Bob WON!")
else:
    print("Alice WON!")
