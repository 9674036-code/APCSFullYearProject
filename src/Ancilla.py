from Qubit import Qubit
class Ancilla(Qubit):
    def __init__(self,s,p):
        super.__init__(s)
        self.position=p # Position within QEC to identify within Hilbert Space
    def collapse():
        pass # Some funciton to interpret the computationl basis and resulting Hilbert Space
