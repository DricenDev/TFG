import random
import sys

from shared.communication import send_data, receive_data
from shared.communication import send_qubits, recieve_qubits
from shared.quantum       import encode_qubits, measure_qubits

# Constants
NUM_QUBITS = 20

# Step 1: Select random bases
base_array = [random.choice(['C', 'H']) for _ in range(NUM_QUBITS)]
print("Bob's bases:")
print(base_array)

# Step 2: Receive qubits from Alice
qc_array = recieve_qubits('coin_flip_bob')

# Step 3: Measure qubits
for i in range(NUM_QUBITS):
    if base_array[i] == 'H':
        qc_array[i].h(0)
results = measure_qubits(qc_array)
print("Bob's bits:")
print(results)

# Step 4: Select random base
bob_base = random.choice(['C', 'H'])
print("Bob's guess base:")
print(bob_base)

# Step 5: Send Alice the base
send_data(bob_base, 'coin_flip_alice')

# Step 6: Receive Alice's base
alice_base = receive_data('coin_flip_bob')

# Step 7: Receive Alice's bits
alice_bits = receive_data('coin_flip_bob')

# Step 8: Compare bits
bit_are_not_the_same = False
for i in range(NUM_QUBITS):
    if base_array[i] == alice_base:
        if results[i] != alice_bits[i]:
            bit_are_not_the_same = True
            break

# Step 9: Say who won
if(bit_are_not_the_same):
    print("There was problem, the coin flip is not valid")
    sys.exit(1)
else:
    if alice_base == bob_base:
        print("Bob WON!")
    else:
        print("Alice WON!")
