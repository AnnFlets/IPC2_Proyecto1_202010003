class Organismo:
    def __init__(self, fila, columna, codigo, color, borde):
        self.fila = fila
        self.columna = columna
        self.codigo = codigo
        self.color = color
        self.borde = borde

    def getFila(self):
        return self.fila

    def setFila(self, fila):
        self.fila = fila

    def getColumna(self):
        return self.columna

    def setColumna(self, columna):
        self.columna = columna

    def getCodigo(self):
        return self.codigo

    def setCodigo(self, codigo):
        self.codigo = codigo

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getBorde(self):
        return self.borde

    def setBorde(self, borde):
        self.borde = borde