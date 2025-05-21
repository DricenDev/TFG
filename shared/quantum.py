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
