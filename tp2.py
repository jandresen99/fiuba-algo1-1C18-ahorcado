import platform

arch_cuentos = open('Cuentos.txt', encoding="ISO-8859-1")
arch_arania_negra = open('La araña negra - tomo 1.txt', encoding="ISO-8859-1")
arch_1000_noches_y_1_noche = open('Las 1000 Noches y 1 Noche.txt', encoding="ISO-8859-1")
arch_palabras = open('palabras.txt', 'w+')
palabras_validas_cuentos = open('palabras_texto_cuentos.txt', 'w+')
palabras_validas_arania_negra = open('palabras_texto_arania_negra.txt', 'w+')
palabras_validas_1000_noches_y_1_noche = open('palabras_texto_1000_noches_y_1_noche.txt', 'w+')
caracteres_reemplazar = open('reemplazar.txt', encoding="ISO-8859-1")


def sistemaOperativo():
    """Programada por Joaquín Andresen.
    Detecta el sistema operativo del usuario"""
    return platform.system()

def leer_archivo(archivo):
    linea = archivo.readline()
    lista = []
    while linea:
        if len(linea) > 1:
            listaPalabras = pasarTextoALista(linea)
            for palabra in listaPalabras:
                lista.append(palabra)
        linea = archivo.readline()
    return lista


def pasarTextoALista(lineaTexto):
    listaPalabras = lineaTexto.split()
    return listaPalabras


def es_texto_valido(palabra):
    """Programada por Maximiliano Coppola.
    Checkea si la palabra contine algun caracter no valido"""
    if palabra == "":
        return False
    for letra in palabra:
        if letra.lower() not in " aábcdeéfghiíjklmnñoópqrstuúüvwxyz" or letra.isdigit() == True:
            return False
    return True


def contar_palabras(lista):
    """ Devuelve un diccionario formado por todas las palabras validas del texto y su cantidad de repeticiones. """
    diccionario = {}
    for renglon in lista:
        palabras = renglon.split()
        for palabra in palabras:
            palabra = palabra.lower()
            reemplazar(palabra)
            palabra = palabra.upper()
            caract = es_texto_valido(palabra)
            num = any(caract == False for letra in palabra)
            if num is False and len(palabra) >= 5:
                if palabra in diccionario:
                    diccionario[palabra] += 1
                else:
                    diccionario[palabra] = 1
    return diccionario

def escribirArchivos(archivo_leer, archivo_escribir):
    """Programada por Joaquín Andresen.
    Recibe dos archivos, lee archivo_leer y crea un diccionario con sus palabras, luego procede a escribir el contenido
    del diccionario en archivo_escribir."""
    lista_de_palabras = leer_archivo(archivo_leer)
    diccionario_de_palabras = contar_palabras(lista_de_palabras)
    for palabra in sorted(diccionario_de_palabras.items(), key=lambda x: x[0]):
        if sistemaOperativo() == "Windows":
            archivo_escribir.write(palabra[0]+"\n")
        else:
            archivo_escribir.write((palabra[0]+"\n").encode('ascii', 'ignore').decode('ascii'))
    print("Datos guardados exitosamente!")
    archivo_leer.seek(0)
    archivo_escribir.seek(0)

def reemplazar(palabra):
    linea = caracteres_reemplazar.readline()
    while linea:
        caracteres = linea.strip().split(",")
        palabra = palabra.replace(caracteres[0], caracteres[1])
        linea = caracteres_reemplazar.readline()
    return palabra


def leerLineaALinea(archivo, default):
    linea = archivo.readline()
    # print(linea)
    return linea if linea else default

escribirArchivos(arch_cuentos, palabras_validas_cuentos)
escribirArchivos(arch_arania_negra, palabras_validas_arania_negra)
escribirArchivos(arch_1000_noches_y_1_noche, palabras_validas_1000_noches_y_1_noche)

linea1 = leerLineaALinea(palabras_validas_cuentos, "zzz")
linea2 = leerLineaALinea(palabras_validas_1000_noches_y_1_noche, "zzz")
linea3 = leerLineaALinea(palabras_validas_arania_negra, "zzz")

palabra1 = linea1.rstrip()
palabra2 = linea2.rstrip()
palabra3 = linea3.rstrip()


while palabra1 != "zzz" or palabra2 != "zzz" or palabra3 != "zzz":
    palabratxt = arch_palabras
    leerLineaALinea(palabratxt, "zzz")
    lista = [palabra1, palabra2, palabra3]
    p1 = min(lista)
    if p1 not in palabratxt:
        palabratxt.write(p1 + "\n")
    if p1 == palabra1:
        linea1 = leerLineaALinea(palabras_validas_cuentos, "zzz")
        palabra1 = linea1.rstrip()
    if p1 == palabra2:
        linea2 = leerLineaALinea(palabras_validas_1000_noches_y_1_noche, "zzz")
        palabra2 = linea2.rstrip()
    if p1 == palabra3:
        linea3 = leerLineaALinea(palabras_validas_arania_negra, "zzz")
        palabra3 = linea3.rstrip()


arch_cuentos.close()
arch_arania_negra.close()
arch_1000_noches_y_1_noche.close()
arch_palabras.close()
palabras_validas_1000_noches_y_1_noche.close()
palabras_validas_cuentos.close()
palabras_validas_arania_negra.close()
caracteres_reemplazar.close()