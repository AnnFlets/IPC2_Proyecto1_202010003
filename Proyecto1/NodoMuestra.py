class NodoMuestra:
    def __init__(self, organismo):
        self.organismo = organismo
        self.siguiente = None

    def getOrganismo(self):
        return self.organismo

    def setOrganismo(self, organismo):
        self.organismo = organismo

    def getSiguiente(self):
        return self.siguiente

    def setSiguiente(self, siguiente):
        self.siguiente = siguiente