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

    def imprimirLimitesCuadricula(self):
        print("----------- TAMAÑO TABLERO -----------")
        print("*** Límite filas: " + str(self.limiteFilas))
        print("*** Limite columnas: " + str(self.limiteColumnas) + "\n")

    def imprimirInformacionMuestras(self):
        auxiliar = self.cabeza
        while auxiliar != None:
            print("MUESTRA")
            print("\t* Código: " + str(auxiliar.getCodigo()))
            print("\t* Descripción: " + str(auxiliar.getDescripcion()))
            print("\t* Límite filas: " + str(auxiliar.getLimiteFilas()))
            print("\t* Limite columnas: " + str(auxiliar.getLimiteColumnas()) + "\n")
            #print("__________ Organismos __________")
            #auxiliar.imprimirPosicionOrganismo()
            #print("")
            auxiliar = auxiliar.getSiguiente()

    def devolverMuestra(self, codigo):
        auxiliar = self.cabeza
        while auxiliar != None:
            if auxiliar.getCodigo() == codigo:
                return auxiliar
            auxiliar = auxiliar.getSiguiente()
        return None