import numpy as np
import matplotlib.pyplot as plt
from qiskit.quantum_info import Operator, DensityMatrix
from qiskit_dynamics import Solver

w = 5.0 * 2 * np.pi  # Qubit frequency (e.g., 5 GHz)
while True:
    try:
        tMax = float(input("Enter simulation time (in ns): "))  # Simulation time
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
numSteps = 200      # Number of evaluation points
tEval = np.linspace(0, tMax, numSteps)

# Define Pauli operators
X = Operator.from_label('X').data
Z = Operator.from_label('Z').data
# Define the Hamiltonian
H = (w / 2) * Z

# Define Dissipators
t1 = 0.5  # Relaxation time constant
t2 = 0.3  # Dephasing time constant

# Dissipator for T1 (lowering operator: |0><1|)
# Qiskit's convention maps |0> to [1, 0]^T and |1> to [0, 1]^T
# Lowering operator maps |1> -> |0>, which is the matrix elements [[0, 1], [0, 0]]
lRelax = np.array([[0, 1], [0, 0]]) / np.sqrt(t1)

# Dissipator for T2
lDephase = Z / np.sqrt(2 * t2)

#Qiskit Dynamics Solver
solver = Solver( static_hamiltonian=H,
    static_dissipators=[lRelax, lDephase])

#Define initial state (Superposition state: |+>)
initialState = DensityMatrix.from_label('+')

# Run the simulation
sol = solver.solve( t_span=[0, tMax],
    y0=initialState,
    t_eval=tEval,
    method="RK45" )

# Extract and Plot Population and Coherence
# Extract the density matrix array at all time steps
states = sol.y

# Population of ground state |0> is the top-left element: \rho_00
excitedPopulation = []
# Coherence is the off-diagonal element: |\rho_01|
coherence = []
for rho in states:
    if hasattr(rho, 'data'):
        matrix = rho.data
    else:
        matrix = rho
    excitedPopulation.append(np.real(matrix[1, 1]))  # Population of |1>
    coherence.append(np.abs(matrix[0, 1]))       # Coherence |rho_01|

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(tEval, excitedPopulation,
         label=r'Excited State Population ($\rho_{11}$)', color='blue')
plt.plot(tEval, coherence,
         label=r'Coherence ($|\rho_{01}|$) ', color='orange', linestyle='--')
plt.xlabel('Time (ns)')
plt.ylabel('Value')
plt.title('Single Qubit Open System Decoherence and Relaxation')
plt.legend()
plt.grid(True)
plt.show()
