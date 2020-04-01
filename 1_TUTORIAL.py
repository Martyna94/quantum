import matplotlib
from qiskit import *
from qiskit.visualization import plot_histogram
from matplotlib import  *



n = 8
n_q = n
n_b = n
qc_output = QuantumCircuit(n_q, n_b)

j: int
for j in range(n):
    qc_output.measure(j, j)
qc_output.draw(output="mpl", filename="circut_fig")
backend_sim = BasicAer.get_backend('qasm_simulator')
counts = execute(qc_output, backend_sim).result().get_counts()
plot_histogram(counts,color='midnightblue', title="New Histogram").savefig('histogram')

input("Przemus to Gówniaczek:*")
