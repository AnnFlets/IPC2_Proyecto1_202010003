from Organismo import Organismo

class NodoMuestra:
    def __init__(self, fila, columna, codigo, color, borde):
        self.organismo = Organismo(fila, columna, codigo, color, borde)
        self.siguiente = None

    def getFila(self):
        return self.organismo.getFila()

    def setFila(self, fila):
        self.organismo.setFila(fila)

    def getColumna(self):
        return self.organismo.getColumna()

    def setColumna(self, columna):
        self.organismo.setColumna(columna)

    def getCodigo(self):
        return self.organismo.getCodigo()

    def setCodigo(self, codigo):
        self.organismo.setCodigo(codigo)

    def getColor(self):
        return self.organismo.getColor()

    def setColor(self, color):
        self.organismo.setColor(color)

    def getBorde(self):
        return self.organismo.getBorde()

    def setBorde(self, borde):
        self.organismo.setBorde(borde)

    def getSiguiente(self):
        return self.siguiente

    def setSiguiente(self, siguiente):
        self.siguiente = siguiente