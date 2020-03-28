from qiskit import *

qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])
backend_sim = BasicAer.get_backend('qasm_simulator')
result = execute(qc, backend_sim).result()
print(result.get_counts(qc))
