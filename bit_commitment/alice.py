import random
import time
import sys

from shared.communication import send_data, receive_data
from shared.communication import send_qubits, recieve_qubits
from shared.quantum       import encode_qubits, measure_qubits

# Constants
NUM_QUBITS = 20

## Commitment phase
# Step 1: Select a base (Computational would represent commit to bit 0, Hadamard would represent commit to bit 1)
alice_base = random.choice(['C', 'H'])
alice_comitted_bit = '0' if alice_base == 'C' else '1' 
print("Alice's commited bit / base:")
print(alice_comitted_bit + '' + alice_base)

# Step 2: Generate random bits
bit_array = [str(random.randint(0, 1)) for _ in range(NUM_QUBITS)]
print("Alice's random bits:")
print(bit_array)

# Step 3: Initialize qubits
qc_array = encode_qubits(bit_array, [alice_base]*NUM_QUBITS)

# Step 4: Send qubits to Bob
send_qubits(qc_array, 'bit_commitment_bob')

# Step 5: Wait for Bob to measure
time.sleep(1) # A time long enough so qubits would lose coherence



## Reveal Phase
# Step 6: Send Bob the commited bit
send_data(alice_comitted_bit, 'bit_commitment_bob')

# Step 7: Send Bob the random bits
send_data(bit_array, 'bit_commitment_bob')
