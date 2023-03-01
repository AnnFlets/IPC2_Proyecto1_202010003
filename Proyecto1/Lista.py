from Nodo import Nodo

class Lista:

    def __init__(self, color):
        self.cabeza = None
        self.cola = None
        self.color = color
        self.limiteFilas = None
        self.limiteColumnas = None

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