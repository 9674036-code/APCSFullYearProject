from qiskit.circuit import QuantumCircuit
from qiskit.circuit.library import PauliEvolutionGate
from qiskit.quantum_info import SparsePauliOp

# Define the Hamiltonian using Pauli operators
H = SparsePauliOp(["ZZ", "XI"], coeffs=[1.0, -0.1])

# Create the coherent time evolution gate for user-defined time
evo_gate = PauliEvolutionGate(H, time=float(input("Enter the evolution time: ")))

# Plug it into a quantum circuit
qc = QuantumCircuit(2)
qc.append(evo_gate, [0, 1])

print(qc.draw())
