# Librería utilizada para la lectura del archivo XML
import xml.dom.minidom as MD

# TDA
from ListaOrganismo import ListaOrganismo

from ListaMuestras import ListaMuestras
from ListaMuestra import ListaMuestra

def leerArchivoXML():
    # LECTURA DE XML
    try:
        ruta = input("Ingrese la ruta del archivo XML a leer:")
        # Se lee el archivo
        xml = MD.parse(ruta)

        datosMarte = xml.getElementsByTagName("datosMarte")
        listaOrganismos = xml.getElementsByTagName("listaOrganismos")
        listadoMuestras = xml.getElementsByTagName("listadoMuestras")

        listaColores = ["#FBB9FF", "#CAFFB9", "#B9E4FF", "#FF8C8C", "#F5FFAA", "#FFCD95", "#CC95FF", "#95FFF7", "#C6C6C6"]
        contador = 0

        # Lista que contendrá la información de los tipos de organismos existentes
        miListaOrganismo = ListaOrganismo()

        # Se obtienen los valores de los atributos para almacenarlos en la lista de organismos
        for listaOrganismo in listaOrganismos:
            organismos = listaOrganismo.getElementsByTagName("organismo")
            for organismo in organismos:
                codigoOrganismo = organismo.getElementsByTagName("codigo")[0].firstChild.data
                nombreOrganismo = organismo.getElementsByTagName("nombre")[0].firstChild.data
                miListaOrganismo.push(codigoOrganismo, nombreOrganismo, listaColores[contador])
                contador = contador + 1

        # Lista que contendrá la información de las muestras y los organismos vivos
        miListaMuestras = ListaMuestras()

        # Lista con los datos de las muestras de los organismos
        for listadoMuestra in listadoMuestras:
            muestras = listadoMuestra.getElementsByTagName("muestra")
            for muestra in muestras:
                codigoMuestra = muestra.getElementsByTagName("codigo")[0].firstChild.data
                descripcionMuestra = muestra.getElementsByTagName("descripcion")[0].firstChild.data
                limiteFilas = int(muestra.getElementsByTagName("filas")[0].firstChild.data)
                limiteColumnas = int(muestra.getElementsByTagName("columnas")[0].firstChild.data)
                listaMuestraNueva = ListaMuestra(codigoMuestra, descripcionMuestra, limiteFilas, limiteColumnas)
                listadoCeldasVivas = muestra.getElementsByTagName("listadoCeldasVivas")
                for listadoCeldaViva in listadoCeldasVivas:
                    celdasVivas = listadoCeldaViva.getElementsByTagName("celdaViva")
                    for celdaViva in celdasVivas:
                        filaOrganismo = int(celdaViva.getElementsByTagName("fila")[0].firstChild.data)
                        columnaOrganismo = int(celdaViva.getElementsByTagName("columna")[0].firstChild.data)
                        codigoOrganismo = celdaViva.getElementsByTagName("codigoOrganismo")[0].firstChild.data
                        colorOrganismo = miListaOrganismo.devolverColor(codigoOrganismo)
                        listaMuestraNueva.push(filaOrganismo, columnaOrganismo, codigoOrganismo, colorOrganismo,
                                               "BLACK")
                miListaMuestras.push(listaMuestraNueva)
        return miListaOrganismo, miListaMuestras
    except:
        print("[ERROR]: Existen problemas con el archivo")