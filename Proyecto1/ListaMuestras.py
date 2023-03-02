from ListaMuestra import ListaMuestra

class ListaMuestras:

    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.limiteFilas = 0
        self.limiteColumnas = 0

    def getCabeza(self):
        return self.cabeza

    def setCabeza(self, cabeza):
        self.cabeza = cabeza

    def getCola(self):
        return self.cola

    def setCola(self, cola):
        self.cola = cola

    def getLimiteFilas(self):
        return self.limiteFilas

    def setLimiteFilas(self, limiteFilas):
        self.limiteFilas = limiteFilas

    def getLimiteColumnas(self):
        return self.limiteColumnas

    def setLimiteColumnas(self, limiteColumnas):
        self.limiteColumnas = limiteColumnas

    def push(self, lista):
        if lista.getLimiteFilas() > self.limiteFilas:
            self.limiteFilas = lista.getLimiteFilas()
        if lista.getLimiteColumnas() > self.limiteColumnas:
            self.limiteColumnas = lista.getLimiteColumnas()
        if self.cabeza == None:
            self.cabeza = lista
            self.cola = lista
        else:
            self.cola.setSiguiente(lista)
            self.cola = lista


    def imprimirLimites(self):
        print("Límite filas: " + str(self.limiteFilas))
        print("Limite columnas: " + str(self.limiteColumnas))

    def imprimirInfoMuestras(self):
        auxiliar = self.cabeza
        while auxiliar != None:
            print("Código: " + str(auxiliar.getCodigo()))
            print("Descripción: " + str(auxiliar.getDescripcion()))
            print("Límite filas: " + str(auxiliar.getLimiteFilas()))
            print("Limite columnas: " + str(auxiliar.getLimiteColumnas()))
            auxiliar = auxiliar.getSiguiente()