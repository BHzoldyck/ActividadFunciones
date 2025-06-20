def agregar(lista):
    while True:
        nombre = input("Ingrese el nombre del contacto (mínimo 3 caracteres): ").strip()
        if len(nombre) >= 3:
            break
        print("El nombre es demasiado corto.")

    while True:
        try:
            telefono = int(input("Ingrese el número de teléfono (9 dígitos): "))
            if 100000000 <= telefono <= 999999999:
                break
            else:
                print("El número debe tener exactamente 9 dígitos.")
        except:
            print("Número inválido. Intente de nuevo.")

    while True:
        email = input("Ingrese el correo electrónico: ").strip()
        if "@" in email and "." in email:
            break
        print("Correo inválido.")

    contacto = {"nombre": nombre, "telefono": telefono, "email": email}
    lista.append(contacto)
    print("Contacto agregado correctamente.")

def listar(lista):
    if not lista:
        print("No hay contactos registrados.")
    else:
        print("Lista de contactos:")
        for i, contacto in enumerate(lista, 1):
            print(f"{i}) Nombre: {contacto['nombre']}, Tel: {contacto['telefono']}, Email: {contacto['email']}")

def buscar(lista):
    nombre_buscado = input("Ingrese el nombre a buscar: ")
    encontrado = False
    for contacto in lista:
        if contacto['nombre'].lower() == nombre_buscado.lower():
            print(f"{contacto['nombre']} - {contacto['telefono']} - {contacto['email']}")
            encontrado = True
    if not encontrado:
        print("No se encontró el contacto.\n")

def eliminar(lista):
    nombre_eliminar = input("Ingrese el nombre del contacto a eliminar: ")
    for contacto in lista:
        if contacto['nombre'].lower() == nombre_eliminar.lower():
            lista.remove(contacto)
            print("Contacto eliminado correctamente.\n")
            return
    print("No se encontró un contacto con ese nombre.\n")