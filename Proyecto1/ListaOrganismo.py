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
        contador = 1
        auxiliar = self.cabeza
        while auxiliar != None:
            print("ORGANISMO #" + str(contador))
            print(str(auxiliar.getCodigo()) + " - " + str(auxiliar.getNombre()))
            auxiliar = auxiliar.getSiguiente()
            contador = contador + 1

    def devolverOrganismo(self, numero):
        contador = 1
        auxiliar = self.cabeza
        while auxiliar != None:
            if contador == numero:
                return auxiliar
            auxiliar = auxiliar.getSiguiente()
            contador = contador + 1
        return None