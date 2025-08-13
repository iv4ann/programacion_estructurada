import backend 
import os
os.system("cls")
import getpass
import empleados
from backend import menu_principal
import bd_conexcion
CREATE DATABASE IF NOT EXISTS bd_las_menonas DEFAULT CHARACTER SET utf8mb4
COLLATE utf8mb4_general_ci;
USE bd_las_menonas;

def menu_ventas(n_empleado, nombre, apellidos):
        repite=True
        while repite:
            backend.borrarpantalla()
            pregunta=input("Elija la opcion que desea realizar\n 1.-Registrar ventas\n " \
            "2.-Revisar inventario\n 3.-Modificar el inventario\n 4.-Ver ventas\n 5.-Exportart ventas " \
            "a excel\n 6.-Salir\n\U0001F449 ")
            match pregunta:
                case "1":
                    from bd_conexcion import conexion
                    backend.registrar_ventas(n_empleado, conexion)
                case "2":
                    backend.revisainv()
                case "3":
                    backend.modificarinv()
                case "4":
                    backend.verventas()
                case "5":
                    backend.exportar_ventas_excel(backend.conexion)
                    backend.esperartecla()
                case "6":
                    print("Saliendo del sistema...")
                    break
                case _:
                    print("Opción no válida, por favor intente de nuevo.")
                    
def main():
    opcion=True
    while opcion:
        backend.borrarpantalla()
        opcion = menu_principal()
        if opcion == "1":
            from empleados import registrar_empleado
            backend.borrarpantalla()
            print("\t\U0001F4DD..::Registrar Empleado::..\U0001F4DD\n")
            nombre = input("Ingrese el nombre del empleado: ").strip().upper()
            apellidos = input("Ingrese los apellidos del empleado: ").strip().upper()
            telefono = input("Ingrese el teléfono del empleado: ").strip()
            contrasena = getpass.getpass("\t Ingresa tu contraseña: ").strip()
            resultado = empleados.registrar_empleado(nombre, apellidos, telefono, contrasena)
            if resultado:
                print(f"\n\t\u2705 Se registró el empleado {nombre} {apellidos} correctamente\u2705")
                print(f"\n\t Número de empleado: {empleados.cursor.lastrowid} \n2")
            else:
                print(f"\n\t..No fue posible registrar el empleado en este momento, inténtalo más tarde ...")
            backend.esperartecla()
        elif opcion == "2":
            backend.borrarpantalla()
            print("\t\U0001F511..::Inicio de Sesión::..\U0001F511\n")
            n_empleado=input("Ingrese su número de empleado: ").strip()
            contrasena=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            paso=empleados.inicio_sesion(n_empleado, contrasena)
            empleados.n_empleado = n_empleado  
            if paso:
                backend.borrarpantalla()
                print(f"\n\tBienvenido {paso[1]} {paso[2]}, has iniciado sesión ...")
                backend.esperartecla()
                backend.borrarpantalla()
                if len(paso)>0:
                    menu_ventas(paso[0],paso[1],paso[2])
            else:
                print(f"\n\tNúmero de empleado y/o contraseña incorrectas, por favor verifique ....")
                backend.esperartecla()
        elif opcion== "3":
            print("Termino la Ejecución del Sistema")
            opcion = False
            backend.esperartecla()
        else:
            print("Opción no válida, por favor intente de nuevo.")
            opcion = True
            backend.esperartecla()


if __name__ == "__main__":
    main()  
   
