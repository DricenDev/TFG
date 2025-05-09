from qiskit                          import QuantumCircuit
from qiskit.compiler                 import transpile
from qiskit.quantum_info             import Statevector
from qiskit.providers.basic_provider import BasicProvider, BasicSimulator

import random
import pickle
import socket
import time

# Constants
NUM_QUBITS = 20

# Step 1: Select a random base
base = random.choice(['Computational', 'Hadamard'])
print("Alice's base:")
print(base)

# Step 2: Select random bits
bit_array = [str(random.randint(0, 1)) for _ in range(NUM_QUBITS)]
print("Alice's random bits:")
print(bit_array)

# Step 3: Initialize each qubit
qc_array = [QuantumCircuit(1) for _ in range(NUM_QUBITS)]
for i in range(NUM_QUBITS):
    if base == 'Computational':
        if bit_array[i] == '1':
            qc_array[i].x(0)
    if base == 'Hadamard':
        if bit_array[i] == '1':
            qc_array[i].x(0)
            qc_array[i].h(0)
        else:
            qc_array[i].h(0)

# Step 4: Send qubits to Bob
time.sleep(5)  # Ensure Bob is ready to receive
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('coin_flip_bob', 61000))
    data_to_send = [Statevector(qc).data for qc in qc_array]
    data_to_send = pickle.dumps(data_to_send)
    s.sendall(data_to_send)

# # Step 5: Receive Bob's base
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind(('coin_flip_alice', 61000))
#     s.listen()
#     conn, addr = s.accept()
#     with conn:
#         data = conn.recv(1024)
#         bob_base = json.loads(data.decode('utf-8'))

# # Step 6: Send Bob the base
# time.sleep(5)  # Ensure Bob is ready to receive
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect(('coin_flip_bob', 61000))
#     data_to_send = json.dumps(bob_base).encode('utf-8')
#     s.sendall(data_to_send)

# # Step 7: Send Bob the bits
# time.sleep(5)  # Ensure Bob is ready to receive
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect(('coin_flip_bob', 61000))
#     data_to_send = json.dumps(bit_array).encode('utf-8')
#     s.sendall(data_to_send)

# # Step 8: You either won or not
# if base == bob_base:
#     print("Bob WON!")
# else:
#     print("Alice WON!")
