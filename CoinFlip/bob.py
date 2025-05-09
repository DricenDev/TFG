from qiskit                          import QuantumCircuit
from qiskit.compiler                 import transpile
from qiskit.quantum_info             import Statevector
from qiskit.providers.basic_provider import BasicProvider, BasicSimulator

simulator = BasicSimulator()
def run(qc):
  transpiled_circuit = transpile(qc, simulator)
  job = simulator.run(transpiled_circuit, shots=1)
  result = job.result()
  result = list(result.get_counts(qc).keys())[0]
  return result

import random
import pickle
import socket
import time

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
        data = b""
        while True:
            chunk = conn.recv(1024)
            if not chunk:
                break
            data += chunk
        state_vectors = pickle.loads(data)
for sv in state_vectors:
    print("Received state vector:")
    print(sv)
qc_array = [QuantumCircuit(1, 1) for _ in range(NUM_QUBITS)]
for qc, sv in zip(qc_array, state_vectors):
    qc.initialize(sv, 0)

# Step 3: Measure qubits
for i in range(NUM_QUBITS):
    if base_array[i] == 'Computational':
        qc_array[i].measure(0, 0)
    if base_array[i] == 'Hadamard':
        qc_array[i].h(0)
        qc_array[i].measure(0, 0)
results = [run(qc) for qc in qc_array]
print("Bob's bits:")
print(results)

# Step 4: Select random base
base = random.choice(['Computational', 'Hadamard'])
print("Bob's guess base:")
print(base)

# # Step 5: Send Alice the base
# time.sleep(5)  # Ensure Alice is ready to receive
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect(('coin_flip_alice', 61000))
#     data_to_send = json.dumps(base).encode('utf-8')
#     s.sendall(data_to_send)

# # Step 6: Receive Alice's base
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind(('coin_flip_bob', 61000))
#     s.listen()
#     conn, addr = s.accept()
#     with conn:
#         data = conn.recv(1024)
#         alice_base = json.loads(data.decode('utf-8'))

# # Step 7: Receive Alice's bits
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind(('coin_flip_bob', 61000))
#     s.listen()
#     conn, addr = s.accept()
#     with conn:
#         data = conn.recv(1024)
#         alice_bits = json.loads(data.decode('utf-8'))

# # Step 8: Compare bits
