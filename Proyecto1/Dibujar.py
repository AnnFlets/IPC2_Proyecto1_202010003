def dibujarLista(miListaMuestra, miOrganismo):
    auxiliar = miListaMuestra.getCabeza()
    limiteHorizontal = miListaMuestra.getLimiteFilas()
    limiteVertical = miListaMuestra.getLimiteColumnas()
    texto = "digraph {\n"
    texto = texto + "\ttbl [\n"
    texto = texto + "\t\tshape=plaintext\n"
    texto = texto + "\t\tlabel=<\n"
    texto = texto + "\t\t\t<table border='0' cellborder='1' color='blue' cellspacing='0'>\n"
    miListaOrganismosFila = None

    while auxiliar != None:

        auxiliar = auxiliar.getSiguiente()
    texto = texto + "\t\t\t</table>\n"
    texto = texto + "\t\t>];\n"
    texto = texto + "}\n"
    nombreArchivo = "Dibujo" + str(miListaMuestra.getCodigo()) + ".dot"
    archivo = open(nombreArchivo, 'w')
    archivo.write(texto)
    archivo.close()

def generarDibujo():
    def GenerarDibujo(self):
        Texto = "digraph {\n"
        Texto = Texto + "\ttbl [\n"
        Texto = Texto + "\t\tshape=plaintext\n"
        Texto = Texto + "\t\tlabel=<\n"
        Texto = Texto + "\t\t\t<table border='0' cellborder='1' color='blue' cellspacing='0'>\n"
        ContFilaVacia = 0
        for i in range(self.LimiteVertical):
            ListaFila = self.ObtenerTodaLaFila(i)
            if ListaFila.Cabeza != None:
                if ContFilaVacia > 0:
                    Texto = Texto + "\t\t\t\t<tr>\n"
                    Texto = Texto + "\t\t\t\t\t<td colspan='" + str(self.LimiteHoritontal) + "'>...</td>\n"
                    Texto = Texto + "\t\t\t\t</tr>\n"
                ContFilaVacia = 0
                Texto = Texto + "\t\t\t\t<tr>\n"
                ContColumnaVacia = 0
                for j in range(self.LimiteHoritontal):
                    Auxilar = ListaFila.ObtenerEnColumna(j)
                    if Auxilar != None:
                        if ContColumnaVacia > 0:
                            Texto = Texto + "\t\t\t\t\t<td colspan='" + str(
                                ContColumnaVacia) + "' bgcolor='White'><font color='Black'>\n"
                            Texto = Texto + "\t\t\t\t\t\t<table color='White'>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t<tr>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t\t<td>...</td>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t</tr>\n"
                            Texto = Texto + "\t\t\t\t\t\t</table>\n"
                            Texto = Texto + "\t\t\t\t\t</font></td>\n"
                        ContColumnaVacia = 0
                        if Auxilar.ObtenerBorde() == 'Green':
                            Texto = Texto + "\t\t\t\t\t<td bgcolor='" + str(
                                Auxilar.ObtenerColor()) + "'><font color='lightblue'>\n"
                            Texto = Texto + "\t\t\t\t\t\t<table color='Green'>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t<tr>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t\t<td>" + str(Auxilar.ObtenerFila()) + "," + str(
                                Auxilar.ObtenerColumna()) + "</td>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t</tr>\n"
                            Texto = Texto + "\t\t\t\t\t\t</table>\n"
                            Texto = Texto + "\t\t\t\t\t</font></td>\n"
                        else:
                            Texto = Texto + "\t\t\t\t\t<td bgcolor='" + str(
                                Auxilar.ObtenerColor()) + "'><font color='lightblue'>\n"
                            Texto = Texto + "\t\t\t\t\t\t<table color='" + str(Auxilar.ObtenerColor()) + "'>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t<tr>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t\t<td>" + str(Auxilar.ObtenerFila()) + "," + str(
                                Auxilar.ObtenerColumna()) + "</td>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t</tr>\n"
                            Texto = Texto + "\t\t\t\t\t\t</table>\n"
                            Texto = Texto + "\t\t\t\t\t</font></td>\n"
                    else:
                        ContColumnaVacia = ContColumnaVacia + 1
                    if j + 1 == self.LimiteHoritontal:
                        if ContColumnaVacia > 0:
                            Texto = Texto + "\t\t\t\t\t<td colspan='" + str(
                                ContColumnaVacia) + "' bgcolor='White'><font color='Black'>\n"
                            Texto = Texto + "\t\t\t\t\t\t<table color='White'>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t<tr>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t\t<td>...</td>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t</tr>\n"
                            Texto = Texto + "\t\t\t\t\t\t</table>\n"
                            Texto = Texto + "\t\t\t\t\t</font></td>\n"
                Texto = Texto + "\t\t\t\t</tr>\n"
            else:
                ContFilaVacia = ContFilaVacia + 1
                if i + 1 == self.LimiteVertical:
                    if ContFilaVacia > 0:
                        Texto = Texto + "\t\t\t\t<tr>\n"
                        Texto = Texto + "\t\t\t\t\t<td colspan='" + str(self.LimiteHoritontal) + "'>...</td>\n"
                        Texto = Texto + "\t\t\t\t</tr>\n"
        Texto = Texto + "\t\t\t</table>\n"
        Texto = Texto + "\t\t>];\n"
        Texto = Texto + "}\n"
        Destino = open('./Clase7/Dibujo.dot', 'w')
        Destino.write(Texto)
        Destino.close()