'''
contactos={
        "Ruben":["6181111111","ruben@gmail.com"]


}
'''


def borrarPantalla():
    import os
    os.system("cls")

def espereTecla():
    input(f"\n\t\t\U0001F552 Oprima cualquier tecla pra continuar ...")

def menu_principal():
    print(F"\n\t\t\t\U0001F4DE Sistema de gestion de agenda de contactos  \U0001F4DE\n\n\t1\uFE0F\u20E3\tAgregar contacto \n\t2\uFE0F\u20E3\tMostrar todos los contactos\n\t3\uFE0F\u20E3\tBuscar contacto por nombre\n\t4\uFE0F\u20E3\tModificar atributo\n\t5\uFE0F\u20E3\tBorrar un contacto\n \t6\uFE0F\u20E3\tSalir")
    opcion=input(f"\t\t\U0001F4DD Elige una opcion (1-4): ").upper()
    return opcion

def agregarContac(agenda):
    borrarPantalla()
    print("\t\t Agregar contactos ")
    nombre=input("Ingrese su nombre: ").upper().strip()
    if nombre in agenda:
        print("Este contacto ya existe")
    else:
        telefono=input("Ingrese su numero de telefono: ").upper()
        email=input("Ingrese su correo electronico: ").lower().strip()
        agenda[nombre]=[telefono,email]
        print("Operacion realizada con exito")
    print("")


def mostrarContac(agenda):
    borrarPantalla()
    print("\t\t Mostrar contactos ")
    if not agenda:
        print("La agenda esta vacia")
    else:
        print(f"{'NOMBRE':<15} {'TELEFONO':<15} {'EMAIL':<10}")
        print(f"-"*45)
        for nombre,fila in agenda.items():
            print(f"{nombre:<15} {fila[0]:<15} {fila[1]:<10}")
            print(f"-"*45)
    print("")

    for nombre in agenda:
        print(f"{nombre:<15} {agenda[nombre][0]:<15} {agenda[nombre][0]:<10}")

def buscarContac(agenda):
    borrarPantalla()
    print("\t\t Mostrar contactos ")
    if not agenda:
        print("La agenda esta vacia")
    else:
        nombre=input("Introduzca el nombre a buscar: ").upper().strip()
        if nombre in agenda:
            print(f"{'NOMBRE':<15} {'TELEFONO':<15} {'EMAIL':<10}")
            print(f"-"*45)
            print(f"{nombre:<15} {agenda[nombre][0]:<15} {agenda[nombre][0]:<10}")
            #print(f"{nombre:<15} {fila[0]:<15} {fila[1]:<10}")
            #Tambien funciona esta forma
            print(f"-"*45)
        else:
            print("No se encontro este nombre ")

def modificarContac(agenda):
    borrarPantalla()
    print("\t\t Modificar contactos ")
    if not agenda:
        print("La agenda esta vacia")
    else:
        nombre=input("Introduce el nombre al que le deseas modificar sus atributos: ").upper().strip()
        if nombre in agenda:
            print("Estos son los valores actuales")
            print(f"Nombre: {nombre}\n Telefono: {agenda[nombre][0]}\n Email: {agenda[nombre][0]}")
            resp=input("Desea cambiar los valores? (si/no)").lower()
            if resp=="si":
                telefono=input("Ingrese su numero de telefono: ").upper()
                email=input("Ingrese su correo electronico: ").lower().strip()
                agenda[nombre]=[telefono,email]
                print("Accion realizada con exito")
        else:
            print("Este contacto no existe")


    '''
        for i in agenda:
            if nombre in agenda:
                resp=input("Desea cambiar el telefono? (si/no) ").lower()
                if resp=="si":
                    telefono=input("Ingrese su numero de telefono: ").upper()
                resp2=input("Desea cambiar el emial? (si/no) ").lower()
                if resp2=="si":
                    email=input("Ingrese su correo electronico: ").lower().strip()
                agenda[nombre]=[telefono,email]
    '''
                

def borrarContac(agenda):
    borrarPantalla()
    print("\t\t Borrar contacto ")
    if not agenda:
        print("La agenda esta vacia")
    else:
        nombre=input("Introduce el nombre al que le deseas modificar sus atributos: ").upper().strip()
        if nombre in agenda:
            #agenda[nombre]=[]
            agenda.pop(nombre)

            
                
                
