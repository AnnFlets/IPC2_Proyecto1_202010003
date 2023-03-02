from DatoOrganismo import DatoOrganismo

class NodoOrganismo:
    def __init__(self, codigo, nombre, color):
        self.datoOrganismo = DatoOrganismo(codigo, nombre, color)
        self.siguiente = None

    def getCodigo(self):
        return self.datoOrganismo.getCodigo()

    def setCodigo(self, codigo):
        self.datoOrganismo.setCodigo(codigo)

    def getNombre(self):
        return self.datoOrganismo.getNombre()

    def setNombre(self, nombre):
        self.datoOrganismo.setNombre(nombre)

    def getColor(self):
        return self.datoOrganismo.getColor()

    def setColor(self, color):
        self.datoOrganismo.setColor(color)

    def getSiguiente(self):
        return self.siguiente

    def setSiguiente(self, siguiente):
        self.siguiente = siguiente