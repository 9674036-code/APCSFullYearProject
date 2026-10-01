import numpy as np
import matplotlib.pyplot as plt
from qiskit.quantum_info import Operator, DensityMatrix, Kraus, SuperOp
from qiskit_dynamics import Solver
from collections import dequeue
g_queue=dequeue()
n_queue=dequeue()
dim = 3


while true:
    g_queue=n_queue
    w = 5.0 * 2 * np.pi  # Qubit frequency (e.g., 5 GHz)
    while True:
        try:
            tMax = float(input("Enter simulation time (in ns): "))  # Simulation time
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    numSteps = 200      # Number of evaluation points
    tEval = np.linspace(0, tMax, numSteps)
    
    print(f"Your Current Gate Queue: {g_queue}")    
    while true:
        ans=input("Press 1 to load an X gate into the queue, 0 to delete the most recent gate from the queue and anything else to save the queue"  )
        if ans=="1":
            g_queue.append(ans)
        elif ans=="0":
            g_queue.pop()
        else:
            print("Queue saved")
            n_queue=g_queue
            break
    
    # Define Pauli operators
    X =  np.array([[0, 1, 0],
         [1, 0, 0],
         [0, 0, 1]])
    Z = np.array([[1,0,0],
        [0,-1,0],
        [0,0,0]])
    noisy_gate_channel = add_average_leakage(X, leakage_rate=0.02, computational_dim=2)
    
    # Define the Hamiltonian
    H = (w / 2) * Z
    
    
    # Define Dissipators
    t1 = 0.5  # Relaxation time constant
    t2 = 0.3  # Dephasing time constant
    
    # Dissipator for T1 (lowering operator: |0><1|)
    # Qiskit's convention maps |0> to [1, 0]^T and |1> to [0, 1]^T
    # Lowering operator maps |1> -> |0>, which is the matrix elements [[0, 1], [0, 0]]
    lRelax = np.array([[0,1,0],
        [0,0,0],
        [0,0,0]
    ]) / np.sqrt(t1)
    
    lRelaxLeakage=np.array([[0,0,0],
        [0,0,np.sqrt(2)],
        [0,0,0]
    ]) / np.sqrt(t1)
    
    # Dissipator for T2
    lDephase = Z / np.sqrt(2 * t2)
    
    #Qiskit Dynamics Solver
    solver = Solver( static_hamiltonian=H,
        static_dissipators=[lRelax, lRelaxLeakage, lDephase])
    
    #Define initial state (Superposition state: |+>)
    initialState = DensityMatrix(np.pad(DensityMatrix.from_label('+').data, ((0, 1), (0, 1))))
    
    # Run the simulation
    sol = solver.solve( t_span=[0, tMax],
        y0=initialState,
        t_eval=tEval,
        method="RK45")
    
    # Extract the density matrix array at all time steps
    states = sol.y
    
    # Population of ground state |0> is the top-left element: \rho_00
    excitedPopulation = []
    # Coherence is the off-diagonal element: |\rho_01|
    coherence = []
    i=0
    for rho in states:
        if hasattr(rho, 'data'):
            matrix = rho.data
        else:
            matrix = rho
        if i=9 and g_queue[0]==1:
            matrix=matrix.evolve(noisy_gate_channel)
            g_queue.popleft()
        i++
        excitedPopulation.append(np.real(matrix[1, 1])) 
        leakagePopulation.append(np.real(matrix[2, 2]))
    
    # Plotting
    plt.figure(figsize=(10, 5))
    plt.plot(tEval, excitedPopulation, leakagePopulation,
              labels=[r'Excited ($\vert1\rangle$)', r'Leaked ($\vert2\rangle$)'],
              colors=['lightblue', 'blue', 'red'], alpha=0.7)
    plt.xlabel('Time (ns)')
    plt.ylabel('Value')
    plt.title('Single Qubit Population Stack Over Time')
    plt.legend()
    plt.grid(True)
    plt.show()

    if input("Do you want to simulate again?(Y/N)  ")!="Y":
        break

def add_average_leakage(ideal_gate_matrix, leakage_rate, computational_dim):
    
    embedded_gate = np.identity(dim, dtype=complex)
    embedded_gate[:computational_dim, :computational_dim] = ideal_gate_matrix
    
    E0 = np.identity(dim, dtype=complex)
    for i in range(computational_dim):
        E0[i, i] = np.sqrt(1 - leakage_rate)
    E0[computational_dim, computational_dim] = 1.0
    
    # Define the Kraus operator for the leakage path
    E1 = np.zeros((dim, dim), dtype=complex)
    for i in range(computational_dim):
        E1[computational_dim, i] = np.sqrt(leakage_rate)
        
    # Combine the embedded unitary gate action with the leakage noise channel
    gate_superop = SuperOp(Operator(embedded_gate))
    leakage_channel = SuperOp(Kraus([E0, E1]))
    
    return leakage_channel @ gate_superop

