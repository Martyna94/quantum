import qiskit

qr = qiskit.QuantumRegister(1)
cr = qiskit.ClassicalRegister(1)
program = qiskit.QuantumCircuit(qr, cr)

program.measure(qr, cr)

job = qiskit.execute(program, qiskit.BasicAer.get_backend('qasm_simulator'))

print(job.result().get_counts())

qiskit.IBMQ.load_account()
backend = qiskit.providers.ibmq.least_busy(qiskit.IBMQ.backends(simulator=False))
print("We'll use the least busy device:", backend.name())
job = qiskit.execute(program, backend)
print(job.result().get_counts())
