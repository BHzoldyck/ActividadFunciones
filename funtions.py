def buscar(lista):
    palabra = ""
    encontrados = []
    contacto = ""
    if len(lista) == 0:
        print("No existen contactos.")
    else:
        palabra = input("Ingrese nombre: ") 
        encontrados = []
        for x in lista:
            if palabra in contacto.lower():
                encontrados.append(contacto)
                if len(encontrados) > 0:
                    print("===Tareas encontradas===")
                    for x in encontrados:
                        print("- " + x)
                else:
                    print("No se encontraron tareas.")
                    
def eliminar(lista):
    if len(lista) == 0:
        print("No existen contactos")
    else:
        print("La lista de contactos registrados es:\n ")
        for x in range(len(lista)):
            print(f"{x} - {lista[x]}")
            try:
                indice = int(input("Ingrese indice a eliminar: "))
                if indice >= 0 and indice < len(lista):
                    lista.pop(indice)
                    print("La tarea se ha eliminado.")
                else:
                    print("El indice ingresado no existe.")
            except:
                print("Valor debe ser numerico.")     