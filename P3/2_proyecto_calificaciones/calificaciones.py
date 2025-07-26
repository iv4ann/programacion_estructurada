import mysql.connector
from mysql.connector import Error
import os

def borrarPantalla():
    os.system("cls" if os.name == "nt" else "clear")

def espereTecla():
    input("\n\t\t \U0001F552Presiona una tecla para continuar ...\U0001F552")

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_calificaciones"
        )
        return conexion
    except Error as e:
        print(f"❌ Error de conexión: {e}")
        return None

def menuPrincipal():
    print("\n\t\t \U0001F4DD.::: SISTEMA DE CALIFICACIONES CON MYSQL :::.\U0001F4DD\n\n\t 1️⃣ Agregar" \
    "\n\t 2️⃣ Mostrar \n\t 3️⃣ Calcular Promedios \n\t 4️⃣ Salir")
    return input("\n\t Elige una opción (1-4): ").strip()

def agregar_calif():
    borrarPantalla()
    print("\n\t\U0001F4DD..: AGREGAR CALIFICACIONES :..\U0001F4DD\n")
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        nombre = input("\U0001F464Nombre del Alumno: ").upper().strip()
        calificaciones = []
        for i in range(1, 4):
            while True:
                try:
                    cal = float(input(f"\U0001F50DCalificación #{i}: "))
                    if 0 <= cal <= 10:
                        calificaciones.append(cal)
                        break
                    else:
                        print("\n\t\u274C...Ingresa un valor entre 0 y 10\u274C")
                except ValueError:
                    print("\n\t\u274C::: Ingresa un valor numérico :::\u274C")
                    espereTecla()
        sql = "INSERT INTO calificaciones (nombre, cal1, cal2, cal3) VALUES (%s, %s, %s, %s)"
        val = (nombre, calificaciones[0], calificaciones[1], calificaciones[2])
        cursor.execute(sql, val)
        conexion.commit()
        print("\n\t\t \u2705::: ¡LA ACCIÓN SE REALIZÓ CON ÉXITO! :::\u2705\n")
        cursor.close()
        conexion.close()

def mostrar_calif():
    borrarPantalla()
    print("\n\t\U0001F4DD..: MOSTRAR CALIFICACIONES :..\U0001F4DD\n")
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre, cal1, cal2, cal3 FROM calificaciones")
        registros = cursor.fetchall()
        if registros:
            print(f"{'Nombre':<15}{'Calif. 1':<10}{'Calif.2':<10}{'Calif.3':<10}")
            print("-" * 50)
            for fila in registros:
                print(f"{fila[0]:<15}{fila[1]:<10}{fila[2]:<10}{fila[3]:<10}")
            print("-" * 50)
            print(f"Total de alumnos: {len(registros)}")
        else:
            print("\n\t\u26A0 No hay calificaciones registradas \u26A0")
        cursor.close()
        conexion.close()
    espereTecla()

def calcular_prom_calif():
    borrarPantalla()
    print("\n\t\U0001F4DD..: PROMEDIOS DE ALUMNOS :..\U0001F4DD\n")
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre, cal1, cal2, cal3 FROM calificaciones")
        registros = cursor.fetchall()
        if registros:
            print(f"{'Nombre':<15}{'Promedio':<10}")
            print("-" * 40)
            promedio_grupal = 0
            for fila in registros:
                promedio = (fila[1] + fila[2] + fila[3]) / 3
                print(f"{fila[0]:<15}{promedio:.2f}")
                promedio_grupal += promedio
            promedio_grupal /= len(registros)
            print("-" * 40)
            print(f"\U0001F389Promedio Grupal: {promedio_grupal:.2f}\U0001F389")
        else:
            print("\n\t\u26A0 No hay datos para calcular promedios \u26A0")
        cursor.close()
        conexion.close()
    espereTecla()