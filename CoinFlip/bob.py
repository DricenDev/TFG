from qiskit                          import QuantumCircuit
# from qiskit.compiler                 import transpile
from qiskit.quantum_info             import Statevector
# from qiskit.providers.basic_provider import BasicProvider, BasicSimulator
# from qiskit.visualization            import plot_histogram, circuit_drawer, plot_bloch_multivector

import random
import json
import socket
import time
import numpy as np

# Constants
NUM_QUBITS = 20

# Step 1: Select random bases
base_array = [random.choice(['Computational', 'Hadamard']) for _ in range(NUM_QUBITS)]
print("Bob's bases:")
print(base_array)

# Step 2: Receive qubits from Alice
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('coin_flip_bob', 61000))
    s.listen()
    conn, addr = s.accept()
    with conn:
        data = conn.recv(1024)
        qc_array = json.loads(data.decode('utf-8'))
        qc_array = [QuantumCircuit(1, 1).from_dict(np.array(qc)) for qc in qc_array]

# Step 3: Measure qubits
for i in range(NUM_QUBITS):
    if base_array[i] == 'Computational':
        qc_array[i].measure(0, 0)
    if base_array[i] == 'Hadamard':
        qc_array[i].h(0)
        qc_array[i].measure(0, 0)

# Step 4: Select random base
base = random.choice(['Computational', 'Hadamard'])
print("Bob's guess base:")
print(base)

# Step 5: Send Alice the base
time.sleep(5)  # Ensure Alice is ready to receive
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('coin_flip_alice', 61000))
    data_to_send = json.dumps(base).encode('utf-8')
    s.sendall(data_to_send)

# Step 6: Receive Alice's base
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('coin_flip_bob', 61000))
    s.listen()
    conn, addr = s.accept()
    with conn:
        data = conn.recv(1024)
        alice_base = json.loads(data.decode('utf-8'))

# Step 7: Receive Alice's bits
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('coin_flip_bob', 61000))
    s.listen()
    conn, addr = s.accept()
    with conn:
        data = conn.recv(1024)
        alice_bits = json.loads(data.decode('utf-8'))

# Step 8: Compare bits
