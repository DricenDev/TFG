import random
import sys

from shared.communication import send_data, receive_data
from shared.communication import send_qubits, recieve_qubits
from shared.quantum       import encode_qubits, measure_qubits

# Constants
NUM_QUBITS = 20

## Commitment phase
# Step 1: Select random bases
base_array = [random.choice(['C', 'H']) for _ in range(NUM_QUBITS)]
print("Bob's bases:")
print(base_array)

# Step 2: Receive qubits from Alice
qc_array = recieve_qubits('bit_commitment_bob')

# Step 3: Measure qubits
for i in range(NUM_QUBITS):
    if base_array[i] == 'H':
        qc_array[i].h(0)
results = measure_qubits(qc_array)
print("Bob's bits:")
print(results)



## Reveal Phase
# Step 4: Receive Alice's commited bit
alice_bit = receive_data('bit_commitment_bob')

# Step 5: Receive Alice's random bits
alice_bits = receive_data('bit_commitment_bob')

# Step 6: Compare bits
alice_base = ['C', 'H'][int(alice_bit)]
bit_are_not_the_same = False
for i in range(NUM_QUBITS):
    if base_array[i] == alice_base:
        if results[i] != alice_bits[i]:
            bit_are_not_the_same = True
            break

if(bit_are_not_the_same):
    print("There was problem, the bit commitment is not valid")
    sys.exit(1)
else:
    print('Everything ok, Alice commited to bit ' + alice_bit + ' on commiting phase')
