from NodoOrganismo import NodoOrganismo

class ListaMuestra:

    def __init__(self, codigo, descripcion, limiteFilas, limiteColumnas):
        self.cabeza = None
        self.cola = None
        self.codigo = codigo
        self.descripcion = descripcion
        self.limiteFilas = limiteFilas
        self.limiteColumnas = limiteColumnas
        self.siguiente = None

    def getCodigo(self):
        return self.codigo

    def setCodigo(self, codigo):
        self.codigo = codigo

    def getDescripcion(self):
        return self.descripcion

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def getLimiteFilas(self):
        return self.limiteFilas

    def setLimiteFilas(self, limiteFilas):
        self.limiteFilas = limiteFilas

    def getLimiteColumnas(self):
        return self.limiteColumnas

    def setLimiteColumnas(self, limiteColumnas):
        self.limiteColumnas = limiteColumnas

    def getCabeza(self):
        return self.cabeza

    def setCabeza(self, cabeza):
        self.cabeza = cabeza

    def getCola(self):
        return self.cola

    def setCola(self, cola):
        self.cola = cola

    def getSiguiente(self):
        return self.siguiente

    def setSiguiente(self, siguiente):
        self.siguiente = siguiente

    def push(self, organismo):
        nodoTemporal = Nodo(organismo)
        if self.cabeza == None:
            self.cabeza = nodoTemporal
            self.cola = nodoTemporal
        else:
            self.cola.setSiguiente(nodoTemporal)
            self.cola = nodoTemporal

    def imprimirPosicionOrganismo(self):
        nodoTemporal = self.cabeza
        while nodoTemporal != None:
            print("Fila: " + str(nodoTemporal.getOrganismo().getFila()))
            print("Columna: " + str(nodoTemporal.getOrganismo().getColumna()))
            nodoTemporal = nodoTemporal.getSiguiente()