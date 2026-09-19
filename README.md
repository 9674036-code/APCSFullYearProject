# APCSFullYearProject

## Project Dependencies (Qiskit, Python 3.12):

### Windows (PowerShell)
**Download Python 3.12:** 

- Go to [Python3.12Install](https://www.python.org/downloads/release/python-3128/)
- In the files section at the bottom, download Windows installer (64-bit)
- Open the downloaded file
- At the bottom of the installation window check the box that says "Add python.exe to PATH"
- Click on Install Now at the top of the window and click "Close" once finished

```powershell
#Check Python version and ensure that it is 3.12
py -3.12 --version

# Create the virtual environment using Python 3.12
py -3.12 -m venv qiskit-env

# Activate the environment
.\qiskit-env\Scripts\Activate.ps1

# Upgrade package installer
pip install --upgrade pip

# Install Qiskit and the local Aer simulator
pip install qiskit qiskit-aer qiskit-ibm-runtime
```
### macOS (Terminal)


```bash
# Install Python 3.12 using Homebrew
brew install python@3.12

# Create the virtual environment using Python 3.12 explicitly
python3.12 -m venv qiskit-env

# Activate the environment
source qiskit-env/bin/activate

# Upgrade your package installer
pip install --upgrade pip

# Install Qiskit and the local Aer simulator
pip install qiskit qiskit-aer qiskit-ibm-runtime
```

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
