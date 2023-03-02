class DatoOrganismo:

    def __init__(self, codigo, nombre, color):
        self.codigo = codigo
        self.nombre = nombre
        self.color = color

    def getCodigo(self):
        return self.codigo

    def setCodigo(self, codigo):
        self.codigo = codigo

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color