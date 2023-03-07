from Lectura import leerArchivoXML
# TDA
from ListaOrganismo import ListaOrganismo
from NodoOrganismo import NodoOrganismo
from DatoOrganismo import DatoOrganismo

from ListaMuestras import ListaMuestras
from ListaMuestra import ListaMuestra
from NodoMuestra import NodoMuestra
from Organismo import Organismo

menuPrincipal = True
miListaOrganismo = ListaOrganismo()
miListaMuestras = ListaMuestras()

while menuPrincipal:
    menuSecundario = True
    try:
        print("""
            =============== BIENVENIDO ===============
            | 1. Cargar archivo                      |
            | 2. Modificar muestra                   |
            | 3. Salir                               |
            ==========================================
            """)
        opcionMenuPrincipal = int(input("Ingrese la opción a realizar: "))
        if opcionMenuPrincipal == 1:
            print("----- CARGAR ARCHIVO -----")
            miListaOrganismo, miListaMuestras = leerArchivoXML()
            print("¡Archivo cargado con éxito!")
        elif opcionMenuPrincipal == 2:
            while menuSecundario:
                print("----- MODIFICAR MUESTRA -----")
                print("1. Seleccionar muestra")
                print("2. Ingresar organismo")
                print("3. Regresar al menú principal")
                opcionMenuSecundario = int(input("Ingrese la opción a realizar: "))
                if opcionMenuSecundario == 1:
                    miListaMuestras.imprimirInformacionMuestras()
                    codigoMuestra = input("Ingrese el código correspondiente a la muestra a modificar: ")
                    miMuestra = miListaMuestras.devolverMuestra(codigoMuestra)
                    if miMuestra != None:
                        print("Muestra seleccionada: " + str(miMuestra.getCodigo()))
                        #print(miMuestra.buscarOrganismo(1, 6))
                        #print(miMuestra.buscarOrganismo(18, 3))
                        #print(miMuestra.buscarOrganismo(9, 15))
                    else:
                        print("La muestra con el código ingresado no existe")
                elif opcionMenuSecundario == 2:
                    miListaOrganismo.imprimirTiposOrganismos()
                    numeroOrganismo = int(input("Ingrese el número correspondiente al organismo a insertar: "))
                    miOrganismo = miListaOrganismo.devolverOrganismo(numeroOrganismo)
                    if miOrganismo != None:
                        print("Organismo seleccionado: " + str(miOrganismo.getCodigo() + " - " + str(miOrganismo.getNombre())))
                        miMuestra.buscarCeldasAptasHorizonal(miOrganismo.getCodigo())
                        miMuestra.buscarCeldasAptasVertical(miOrganismo.getCodigo())
                        miMuestra.buscarCeldasAptasDiagonal(miOrganismo.getCodigo())
                    else:
                        print("La opción ingresada no existe")
                elif opcionMenuSecundario == 3:
                    print("Regresando...")
                    menuSecundario = False
                else:
                    print("La opción ingresada no existe")
        elif opcionMenuPrincipal == 3:
            print("Saliendo...")
            menuPrincipal = False
        else:
            print("La opción ingresada no existe")
    except:
        print("Opción inválida")