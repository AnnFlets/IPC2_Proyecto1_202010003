class Organismo:
    def __init__(self, fila, columna, color, borde):
        self.fila = fila
        self.columna = columna
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

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getBorde(self):
        return self.borde

    def setBorde(self, borde):
        self.borde = borde