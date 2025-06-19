def agregar(lista):
    nombre = ""
    telefono = 0
    mail = ""
    sublista = []
    while (len(nombre) <= 2):
        nombre = input("Ingrese el nombre del contacto (largo del nombre debe ser minimo de 3 caracteres): \n")
        sublista.append(nombre)
    while telefono < 100000000 or telefono > 999999999:
        try:
            telefono = int(input("Digite su numero de telefono de contacto de nueve (9) digitos: \n"))
        except:
            print("El numero ingresado no es valido, por favor intente nuevamente: \n")
        sublista.append(telefono)
    while "@" not in mail:
        mail = input("Ingrese su dirección de correo valida: \n")
        sublista.append(mail)
    lista.append(sublista)

def mostrar(lista):
    if len(lista) == 0:
        print("No hay contactos registrados.")
    else:    
        print("La lista de contactos registrados es: \n")   
        for x in range(len(lista)):
            print(f"{x+1} - {lista[x]}")