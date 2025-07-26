import mysql.connector
from mysql.connector import Error
import os

def borrarPantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def esperarTecla():
    input("\n\tPresiona una tecla para continuar...")

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_agenda"
        )
        return conexion
    except Error as e:
        print(f"❌ Error al conectar a la BD: {e}")
        return None
def agregarContacto():
    borrarPantalla()
    print("\n\tAgregar contacto\n")
    conexion = conectar()
    if conexion:
        nombre = input("Ingrese el nombre: ").upper().strip()
        telefono = input("Ingrese el teléfono: ").strip()
        email = input("Ingrese el email: ").lower().strip()

        cursor = conexion.cursor()
        try:
            sql = "INSERT INTO contactos (nombre, telefono, email) VALUES (%s, %s, %s)"
            val = (nombre, telefono, email)
            cursor.execute(sql, val)
            conexion.commit()
            print("\n✅ Contacto agregado exitosamente.")
        except mysql.connector.IntegrityError:
            print("\n⚠️ Ya existe un contacto con ese nombre.")
        cursor.close()
        conexion.close()
    esperarTecla()
def mostrarContactos():
    borrarPantalla()
    print("\n\tLista de contactos\n")
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre, telefono, email FROM contactos")
        registros = cursor.fetchall()
        if registros:
            print(f"{'NOMBRE':<15}{'TELÉFONO':<15}{'EMAIL':<30}")
            print("-" * 60)
            for fila in registros:
                print(f"{fila[0]:<15}{fila[1]:<15}{fila[2]:<30}")
            print("-" * 60)
        else:
            print("\n📭 Agenda vacía.")
        cursor.close()
        conexion.close()
    esperarTecla()
def buscarContacto():
    borrarPantalla()
    print("\n\tBuscar contacto\n")
    conexion = conectar()
    if conexion:
        nombre = input("Ingrese el nombre a buscar: ").upper().strip()
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre, telefono, email FROM contactos WHERE nombre = %s", (nombre,))
        fila = cursor.fetchone()
        if fila:
            print(f"\n📇 Contacto encontrado:")
            print(f"{'NOMBRE':<15}{'TELÉFONO':<15}{'EMAIL':<30}")
            print("-" * 60)
            print(f"{fila[0]:<15}{fila[1]:<15}{fila[2]:<30}")
        else:
            print("\n❌ Contacto no encontrado.")
        cursor.close()
        conexion.close()
    esperarTecla()
def modificarContacto():
    borrarPantalla()
    print("\n\tModificar contacto\n")
    conexion = conectar()
    if conexion:
        nombre = input("Ingrese el nombre del contacto a modificar: ").upper().strip()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM contactos WHERE nombre = %s", (nombre,))
        fila = cursor.fetchone()
        if fila:
            print(f"\n📝 Contacto actual:\nNombre: {fila[1]}\nTeléfono: {fila[2]}\nEmail: {fila[3]}")
            confirmar = input("¿Deseas modificar este contacto? (si/no): ").lower()
            if confirmar == "si":
                telefono = input("Nuevo teléfono: ").strip()
                email = input("Nuevo email: ").lower().strip()
                cursor.execute("UPDATE contactos SET telefono = %s, email = %s WHERE nombre = %s",
                               (telefono, email, nombre))
                conexion.commit()
                print("\n✅ Contacto actualizado con éxito.")
        else:
            print("\n❌ Contacto no encontrado.")
        cursor.close()
        conexion.close()
    esperarTecla()
def borrarContacto():
    borrarPantalla()
    print("\n\tEliminar contacto\n")
    conexion = conectar()
    if conexion:
        nombre = input("Ingrese el nombre del contacto a eliminar: ").upper().strip()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM contactos WHERE nombre = %s", (nombre,))
        fila = cursor.fetchone()
        if fila:
            confirmar = input(f"¿Estás seguro de eliminar a {nombre}? (si/no): ").lower()
            if confirmar == "si":
                cursor.execute("DELETE FROM contactos WHERE nombre = %s", (nombre,))
                conexion.commit()
                print("\n✅ Contacto eliminado correctamente.")
        else:
            print("\n❌ Contacto no encontrado.")
        cursor.close()
        conexion.close()
    esperarTecla()