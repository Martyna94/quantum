# Importing standard Qiskit libraries and configuring account
from qiskit import QuantumCircuit, execute, Aer, IBMQ
from qiskit.visualization import plot_histogram, matplotlib

# Loading your IBM Q account(s)
provider = IBMQ.load_account()

circuit = QuantumCircuit(2, 2)

circuit.h(0)
circuit.cx(0, 1)
circuit.measure([0, 1], [0, 1])

simulator = Aer.get_backend('qasm_simulator')
job = execute(circuit, simulator, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:", counts)

plot_histogram(counts, color='midnightblue', title="New Histogram")
circuit.draw(output="mpl", filename="circut_fig")

