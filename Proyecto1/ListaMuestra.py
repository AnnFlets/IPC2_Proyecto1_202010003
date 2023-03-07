from NodoMuestra import NodoMuestra

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

    def push(self, fila, columna, codigo, color, borde):
        nodoTemporal = NodoMuestra(fila, columna, codigo, color, borde)
        if self.cabeza == None:
            self.cabeza = nodoTemporal
            self.cola = nodoTemporal
        else:
            self.cola.setSiguiente(nodoTemporal)
            self.cola = nodoTemporal

    def buscarOrganismo(self, fila, columna, codigo):
        if fila < self.getLimiteFilas() and columna < self.getLimiteColumnas() and fila >= 0 and columna >= 0:
            auxiliar = self.cabeza
            while auxiliar != None:
                if (auxiliar.getFila() == fila and auxiliar.getColumna() == columna and auxiliar.getCodigo() != codigo):
                    return 0
                elif (auxiliar.getFila() == fila and auxiliar.getColumna() == columna and auxiliar.getCodigo() == codigo):
                    return 1
                auxiliar = auxiliar.getSiguiente()
        return 2

    def buscarCeldasAptasHorizonal(self, codigo):
        auxiliar = self.cabeza
        while auxiliar != None:
            if auxiliar.getCodigo() == codigo:
                fila = auxiliar.getFila()
                columna = auxiliar.getColumna()
                comer = False
                if self.buscarOrganismo(fila, columna + 1, codigo) == 0:
                    fila = auxiliar.getFila()
                    columna = auxiliar.getColumna()
                    columna = columna + 1
                    contador = columna
                    while(contador <= self.getLimiteColumnas()):
                        if self.buscarOrganismo(fila, contador + 1, codigo) == 2:
                            comer = True
                            break
                        elif self.buscarOrganismo(fila, contador + 1, codigo) == 1:
                            break
                        elif self.buscarOrganismo(fila, contador + 1, codigo) == 0:
                            pass
                        contador = contador + 1
                    if comer == True:
                        print("Auxiliar en:\nFila: " + str(fila) + " Columna: " + str(columna - 1))
                        print("Puede Comer Ficha en Fila: " + str(fila) + " Columna: " + str(columna))
                        columnaCeldaApta = columna + 1
                        while (self.buscarOrganismo(fila, columna + 1, codigo) == 0):
                            print("\nPuede Comer Ficha en Fila: " + str(fila) + " Columna: " + str(columna + 1))
                            columnaCeldaApta = columnaCeldaApta + 1
                            columna = columna + 1
                        print("Celda apta (VERDE) -> fila: " + str(fila) + " - columna: " + str(columnaCeldaApta))
                    print("--------------------------------------------------")
                if self.buscarOrganismo(fila, columna - 1, codigo) == 0:
                    fila = auxiliar.getFila()
                    columna = auxiliar.getColumna()
                    columna = columna - 1
                    contador = columna
                    while (contador >= 0):
                        if self.buscarOrganismo(fila, contador - 1, codigo) == 2:
                            comer = True
                            break
                        elif self.buscarOrganismo(fila, contador - 1, codigo) == 1:
                            break
                        elif self.buscarOrganismo(fila, contador - 1, codigo) == 0:
                            pass
                        contador = contador - 1
                    if comer == True:
                        print("Auxiliar en:\nFila: " + str(fila) + " Columna: " + str(columna + 1))
                        print("Puede Comer Ficha en Fila: " + str(fila) + " Columna: " + str(columna))
                        columnaCeldaApta = columna - 1
                        while (self.buscarOrganismo(fila, columna - 1, codigo) == 0):
                            print("\nPuede Comer Ficha en Fila: " + str(fila) + " Columna: " + str(columna - 1))
                            columnaCeldaApta = columnaCeldaApta - 1
                            columna = columna - 1
                        print("Celda apta (VERDE) -> fila: " + str(fila) + " - columna: " + str(columnaCeldaApta))
                    print("--------------------------------------------------")
            auxiliar = auxiliar.getSiguiente()

    def buscarCeldasAptasVertical(self, codigo):
        auxiliar = self.cabeza
        while auxiliar != None:
            if auxiliar.getCodigo() == codigo:
                fila = auxiliar.getFila()
                columna = auxiliar.getColumna()
                comer = False
                if self.buscarOrganismo(fila + 1, columna, codigo) == 0:
                    fila = auxiliar.getFila()
                    columna = auxiliar.getColumna()
                    fila = fila + 1
                    contador = fila
                    while (contador <= self.getLimiteFilas()):
                        if self.buscarOrganismo(contador + 1, columna, codigo) == 2:
                            comer = True
                            break
                        elif self.buscarOrganismo(contador + 1, columna, codigo) == 1:
                            break
                        elif self.buscarOrganismo(contador + 1, columna, codigo) == 0:
                            pass
                        contador = contador + 1
                    if comer == True:
                        print("Auxiliar en:\nFila: " + str(fila - 1) + " Columna: " + str(columna))
                        print("Puede Comer Ficha en Fila: " + str(fila) + " Columna: " + str(columna))
                        filaCeldaApta = fila + 1
                        while (self.buscarOrganismo(fila + 1, columna, codigo) == 0):
                            print("\nPuede Comer Ficha en Fila: " + str(fila + 1) + " Columna: " + str(columna))
                            filaCeldaApta = filaCeldaApta + 1
                            fila = fila + 1
                        print("Celda apta (VERDE) -> fila: " + str(filaCeldaApta) + " - columna: " + str(columna))
                    print("--------------------------------------------------")
                if self.buscarOrganismo(fila - 1, columna, codigo) == 0:
                    fila = auxiliar.getFila()
                    columna = auxiliar.getColumna()
                    fila = fila - 1
                    contador = fila
                    while (contador >= 0):
                        if self.buscarOrganismo(contador - 1, columna, codigo) == 2:
                            comer = True
                            break
                        elif self.buscarOrganismo(contador - 1, columna, codigo) == 1:
                            break
                        elif self.buscarOrganismo(contador - 1, columna, codigo) == 0:
                            pass
                        contador = contador - 1
                    if comer == True:
                        print("Auxiliar en:\nFila: " + str(fila + 1) + " Columna: " + str(columna))
                        print("Puede Comer Ficha en Fila: " + str(fila) + " Columna: " + str(columna))
                        filaCeldaApta = fila - 1
                        while (self.buscarOrganismo(fila - 1, columna, codigo) == 0):
                            print("\nPuede Comer Ficha en Fila: " + str(fila - 1) + " Columna: " + str(columna))
                            filaCeldaApta = filaCeldaApta - 1
                            fila = fila - 1
                        print("Celda apta (VERDE) -> fila: " + str(filaCeldaApta) + " - columna: " + str(columna))
                    print("--------------------------------------------------")
            auxiliar = auxiliar.getSiguiente()

    def buscarCeldasAptasDiagonal(self, codigo):
        auxiliar = self.cabeza
        while auxiliar != None:
            fila = auxiliar.getFila()
            columna = auxiliar.getColumna()
            if self.buscarOrganismo(fila + 1, columna + 1, codigo):
                print("Auxiliar en:\nFila: " + str(fila) + " Columna: " + str(columna) +
                      "\nPuede Comer Ficha en Fila: " + str(fila + 1) + " Columna: " + str(columna + 1))
                #if (Fila + 2 < self.LimiteVertical and Columna + 2 < self.LimiteHorizontal):
                    #FichasContrarias.EliminarPosicion(Fila + 1, Columna + 1)
                    #self.MoverAuxiliar(Auxiliar, Fila + 2, Columna + 2)
            elif self.buscarOrganismo(fila - 1, columna + 1, codigo):
                print("Auxiliar en:\nFila: " + str(fila) + " Columna: " + str(columna) +
                      "\nPuede Comer Ficha en Fila: " + str(fila - 1) + " Columna: " + str(columna + 1))
                #if (Fila - 2 >= 0 and Columna + 2 < self.LimiteHorizontal):
                    #FichasContrarias.EliminarPosicion(Fila - 1, Columna + 1)
                    #self.MoverAuxiliar(Auxiliar, Fila - 2, Columna + 2)
            elif self.buscarOrganismo(fila - 1, columna - 1, codigo):
                print("Auxiliar en:\nFila: " + str(fila) + " Columna: " + str(columna) +
                      "\nPuede Comer Ficha en Fila: " + str(fila - 1) + " Columna: " + str(columna - 1))
                #if (Fila - 2 >= 0 and Columna - 2 >= 0):
                    #FichasContrarias.EliminarPosicion(Fila - 1, Columna - 1)
                    #self.MoverAuxiliar(Auxiliar, Fila - 2, Columna - 2)
            elif self.buscarOrganismo(fila + 1, columna - 1, codigo):
                print("Auxiliar en:\nFila: " + str(fila) + " Columna: " + str(columna) +
                      "\nPuede Comer Ficha en Fila: " + str(fila + 1) + " Columna: " + str(columna - 1))
                #if (Fila + 2 < self.LimiteVertical and Columna - 2 >= 0):
                    #FichasContrarias.EliminarPosicion(Fila + 1, Columna - 1)
                    #self.MoverAuxiliar(Auxiliar, Fila + 2, Columna - 2)
            auxiliar = auxiliar.getSiguiente()
    def imprimirPosicionOrganismo(self):
        nodoTemporal = self.cabeza
        while nodoTemporal != None:
            print("Fila: " + str(nodoTemporal.getFila()))
            print("Columna: " + str(nodoTemporal.getColumna()))
            nodoTemporal = nodoTemporal.getSiguiente()