
from cgi import print_environ
from itertools import count


def invertir_palabra(palabra):
    palabra =  input("Ingresar palabra ")
    invertir=""
    for j in palabra:
        invertir = j + invertir
    print("La palabra " + "'"+ palabra +"'" +" invertida es " +invertir)

invertir_palabra("palabra")