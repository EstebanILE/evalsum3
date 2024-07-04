import csv 
import os 
import time 
import random

limpia_pantalla = "cls"

contador = 0

pedido_encabezado = [("Nro. de pedido  cliente direccion   sector   saco 5kg   saco 10kg    saco 20 kg")]

os.system(limpia_pantalla)

with open('archivo.csv', 'a', newline='') as archico_prue:
    lecturo = archico_prue.__dict__
    les = archico_prue.txt


def pedido():
    saco_5kilos = 0
    saco_10kilos = 0
    saco_20kilos = 0
    return

def numero1():
    return random.randomi(1.1000)
pedido_listo = []


while True:
    print("Bienvenido a la tienda CatPremuin")
    print("1. Registar pedido")
    print("2. listar de todos los pedidos")
    print("3. Imprimri hoja de ruta")
    print("4. Salir del programa")
    res1 = input("Ingrese su respuesta (1-4): ")
    if res1 == 1:
        print("vamos a depirle unos datos para registrarlo en el pedido")
        nombr = input("Ingrese su nombre: ")
        apellidoo = input("Ingrese su apellido: ")
        direccionn =int(input("ingrese su dirrecion para su pedido"))
        comun = input("Ingrese la comuna de donde vive: ")
        print("Esta bien sus datos")
        print("1. si")
        print("2. no")
        res2 = input("ingrese su respuesta (1-2): ")
        if res2 == 1:
            print("Que saco necesita ")
            print("1.Saco de 5 kilos")
            print("2. sacos de 10 kilos")
            print("3. sacos de 20 kilos")
            print("4. salir")
            res3 = input("ingrese una opcion (1-4): ")
            if res3 ==1:
                print("decidio la opcion de 5 kilos")
                saco_5kilos += 1
                
            elif res3 ==2:
                print("ingreso la opcion de 10 kilos")
                saco_10kilos +=1
                
            elif res3 ==3:
                print("ingreso a la opcion de 20 kilos")
                saco_20kilos += 1
            elif res3 == 4:
                print("muchas gracias")
                break
        elif res2 ==2:
            print("espere un momento")
            break

        else:
            print("Ingrese una opcion valida")
    elif res1 ==2:
        print("aca estan todos los pedidos ")
        
    elif res1 ==3:
        print("eligio la opcion de imprimir la hoja de ruta")
        contador += 1
        break
    elif res1 == 4:
        print("gracias por elegirnos :)")
        break
    else:
        print("la opcion que eligio no esta disponible vuelva a intentarlo")

while contador ==1:
    print("este es la opcion de imprimir ruta ")
    print(f"la direccion es {direccionn}")
    print(f"la comuna donde ira el pedido es {comun}")
    print("esos son las rutas que se van a utilizar ")
    break




