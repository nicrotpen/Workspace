def cambiaTexto1(palabra):
    longitudPalabra = len(palabra)
    if longitudPalabra <=2:
        return palabra
    elif longitudPalabra>2 and longitudPalabra<=6:
        temp1 = palabra[0:2]
        temp2 = palabra[len(palabra)-2:]
        palabra = temp2 + palabra + temp1
        return palabra
    else:
        temp1 = palabra[0:3]
        temp2 = palabra[len(palabra)-3:]
        palabra = temp2 + temp1
        return palabra

def cambiaTexto2(palabra):
    if palabra.lower() == palabra:
        return palabra.upper()
    elif palabra.upper() == palabra:
        return palabra.lower()
    else:
        return "mezclado"

def cambiaTexto3(palabra):
    longitud = 5 * len(palabra)
    palabra = str(longitud-5) + palabra + str(longitud)
    return palabra

def cambiaTexto4(palabra):
    longitud = 10*len(palabra)
    palabra= str(longitud-9) + palabra.upper() + str(longitud)
    return palabra

import random
palabra= str(input('Por favor introduzca una palabra: '))
combinacion = random.randint(1,3)

if combinacion== 1:
    contrasenya= palabra
    contrasenya = cambiaTexto3(cambiaTexto2(cambiaTexto1(contrasenya)))

elif combinacion==2:
    contrasenya= palabra
    contrasenya = cambiaTexto1(cambiaTexto2(cambiaTexto4(contrasenya)))

elif combinacion==3:
    contrasenya= palabra
    contrasenya = cambiaTexto4(cambiaTexto2(cambiaTexto3(contrasenya)))

if len(contrasenya)<10:
    n=10-len(contrasenya)
    plus= 10**(n-1)
    contrasenya = str(plus) + contrasenya

elif len(contrasenya)>10:
    contrasenya= contrasenya [0:11]

print(f'Tu contraseña es {contrasenya}')