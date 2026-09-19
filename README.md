# APCSFullYearProject

## Project Dependencies:

### Qiskit
**MacOS:**
`python3 -m venv qiskit-env`

`source qiskit-env/bin/activate`

`pip install --upgrade pip`

`pip install 'qiskit[visualization]'`

### Python version 3.11 or higher

## Project Brainstorm:
**Qubit Leakage Modeling**( currently preferred idea ):

**User:** Physicists, students and engineers interested in studying Leakage in quantum computing, especially the spread of it in a transmon superconducting qubit architecture.   

**Problem:** Leakage in quantum computing is often hard to identify and greatly contributes to the error rate that locks modern quantum computing at NISQ, modeling leakage can allow for pattern identification either through deep machine learning or the exploitation of a given trend to reduce and identify leakage. 

**Features:** The application should be able to accurately model the spread of leakage between two or more qubits, track and display how the quantum state of each qubits changes and perhaps demonstrate/simulate the effects of leakage in a QEC circuit. 

**Question:** In order to build the application, I would have to learn how leakage mathematically spreads (resonance pairing) and how to perform advanced mathematics in Java, as there is no numpy or other libraries in Java oriented towards quantum computing like python does. 

**Educational General Relativity Game:**

**User:** The general public; anyone interested in general relativity.

**Problem:** General relativity is often either shallowly/inaccurately portrayed or explained in a depth that makes it hard for the general public to learn in terms of online resources.

**Functionality:** The game should slowly and intuitively introduce general relativity, perhaps using a classical mechanics analog and slowly working its way up to basic general relativity that is taught to the user through the game.

**Machine Learning Model To Identify Leakage**

**User:** Physicists, students and engineers interested in developing software that combats leakage in quantum computing

**Problem:** Leakage in quantum computing is often hard to identify and greatly contributes to the error rate that locks modern quantum computing at NISQ for the transom superconducting qubit architecture. 

**Functionality:** The model should be able to somewhat correctly guess the position of a leaked qubit given a dataset of syndrome measurements from a given circuit that has an unknown leaked qubit(s). 
