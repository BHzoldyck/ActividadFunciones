import os,time
from funtions import *

# Trabajo Colaborativo: "Mini Agenda de Contactos"
# Objetivo:
# Desarrollar una pequeña aplicación de consola en Python que funcione como una agenda de contactos. El objetivo es aplicar los conocimientos de programación estructurada (variables, constantes, tipos de datos, estructuras de control, funciones, etc.) y prácticas básicas de trabajo colaborativo con Git y GitHub.
# ________________________________________
# Requisitos del Proyecto
# La aplicación debe permitir al usuario:
# 1.	Agregar un contacto: nombre, teléfono, email.
# 2.	Listar contactos: mostrar todos los contactos guardados.
# 3.	Buscar un contacto por nombre.
# 4.	Eliminar un contacto.
# 5.	Salir del programa.
# Debe usarse un menú para navegar entre estas opciones.
# La estructura de datos puede ser una lista de diccionarios.
# ________________________________________
# Organización del Trabajo
# •	El repositorio debe ser creado por uno de los integrantes del grupo y compartido con los otros.
# •	Todos deben clonar el repositorio en su computadora local.
# •	Cada alumno trabajará en una rama propia (ejemplo: rama-juan, rama-maria, rama-carlos).
# •	Cada uno será responsable de una parte del programa:
# o	Alumno 1: Función para agregar y mostrar contactos.
# o	Alumno 2: Función para buscar y eliminar contactos.
# o	Alumno 3: Estructura del menú principal y control de flujo del programa.

contactos = []

while True:
    os.system("cls")
    print("\t AGENDA DE CONTACTOS\n")
    print("1) Agregar contacto")
    print("2) Listar contactos")
    print("3) Buscar contacto por nombre")
    print("4) Eliminar contacto")
    print("5) Salir\n")
    try:
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            os.system("cls")
            print("\tAGREGAR CONTACTO\n")
            agregar(contactos)
            os.system("Pause")
        
        elif opcion == 2:
            os.system("cls")
            print("\tLISTAR CONTACTOS\n")   
            mostrar(contactos)
            os.system("Pause")

        elif opcion == 3:
            os.system("cls")
            print("\tBUSCAR CONTACTO POR NOMBRE\n")  
            buscar(contactos)
            os.system("Pause")

        elif opcion == 4:  
            os.system("cls")
            print("\tELIMINAR CONTACTO\n")
            eliminar(contactos)
            os.system("Pause")
            

        elif opcion == 5:
            os.system("cls")
            print("\tSaliendo.\n")
            time.sleep(1)
            os.system("cls")
            print("\tSaliendo..\n")
            time.sleep(1)
            os.system("cls")
            print("\tSaliendo...\n")
            time.sleep(1)
            os.system("cls")
            print("\tADIOS :)\n")
            time.sleep(1)
            break
            
            
        else:
            os.system("cls")
            print("Opcion no existente, intente de nuevo")  
            os.system("Pause")
            
    except:
        os.system("cls")
        print("opcion no valida, intente nuevamente")
        os.system("Pause")