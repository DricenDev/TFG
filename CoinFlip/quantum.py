from qiskit                          import QuantumCircuit
from qiskit.compiler                 import transpile
from qiskit.quantum_info             import Statevector
from qiskit.providers.basic_provider import BasicProvider, BasicSimulator

simulator = BasicSimulator() # Meterlo dentro de la funcion?
def run(qc):
  transpiled_circuit = transpile(qc, simulator)
  job = simulator.run(transpiled_circuit, shots=1)
  result = job.result()
  result = list(result.get_counts(qc).keys())[0]
  return result

# qc_array = [QuantumCircuit(1, 1) for _ in range(20)]
# for qc in qc_array:
#     qc.h(0)
#     qc.measure(0, 0)
# results = [run(qc) for qc in qc_array]
# print(results)