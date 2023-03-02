from NodoOrganismo import NodoOrganismo

class ListaOrganismo:

    def __init__(self):
        self.cabeza = None
        self.cola = None

    def getCabeza(self):
        return self.cabeza

    def setCabeza(self, cabeza):
        self.cabeza = cabeza

    def getCola(self):
        return self.cola

    def setCola(self, cola):
        self.cola = cola

    def push(self, codigo, nombre, color):
        nodoTemporal = NodoOrganismo(codigo, nombre, color)
        if self.cabeza == None:
            self.cabeza = nodoTemporal
            self.cola = nodoTemporal
        else:
            self.cola.setSiguiente(nodoTemporal)
            self.cola = nodoTemporal

    def devolverColor(self, codigo):
        auxiliar = self.cabeza
        while auxiliar != None:
            if auxiliar.getCodigo() == codigo:
                return auxiliar.getColor()
            auxiliar = auxiliar.getSiguiente()

    def imprimirTiposOrganismos(self):
        auxiliar = self.cabeza
        while auxiliar != None:
            print("Código: " + str(auxiliar.getCodigo()))
            print("Nombre: " + str(auxiliar.getNombre()))
            print("Color: " + str(auxiliar.getColor()))
            print("-----------------------------------------------------")
            auxiliar = auxiliar.getSiguiente()