from qiskit                          import QuantumCircuit
from qiskit.compiler                 import transpile
from qiskit.quantum_info             import Statevector
from qiskit.providers.basic_provider import BasicSimulator

simulator = BasicSimulator()

def run(qc):
    transpiled_circuit = transpile(qc, simulator)
    job = simulator.run(transpiled_circuit, shots=1)
    result = job.result()
    result = list(result.get_counts(qc).keys())[0]
    return result

def encode_qubits(bits, bases):
    qubits_ammount = len(bits)
    qc_array = [QuantumCircuit(1, 1) for _ in range(qubits_ammount)]
    for i in range(qubits_ammount):
        if bases[i] == 'C':
            if bits[i] == '1':
                qc_array[i].x(0)
        if bases[i] == 'H':
            if bits[i] == '1':
                qc_array[i].x(0)
                qc_array[i].h(0)
            else:
                qc_array[i].h(0)
    return qc_array

def measure_qubits(quantum_circuits):
    for qc in quantum_circuits: qc.measure(0, 0)
    return [run(qc) for qc in quantum_circuits]
