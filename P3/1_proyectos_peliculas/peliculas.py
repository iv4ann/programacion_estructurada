'''
Dict u objeto que permita almacenar los siguientes atributos: nombre, categoria, clasificacion,
 genero, idioma de peliculas
'''
'''


pelicula=(
    "nombre":"",
    "categoria":"",
    "clasificacion":"",
    "genero":"",
    "idioma":""
    )
'''
import mysql.connector
from mysql.connector import Error

pelicula={}
#peli=""

def borrarPantalla():
    import os
    os.system("cls")

def espereTecla():
    input(f"\n\t... Oprima cualquier tecla pra continuar ...")

def conectar():
    try:
        conexion=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_peliculas1"
        )
        return conexion
    except Error as e: 
        print(f"El error que se presenta es {e}")
        return None
    
def crearPeliculas():
    borrarPantalla()
    conexion_bd=conectar()
    if conexion_bd!=None:
        print("\n\t.::Agregar peliculas::.\n")
    '''
    atributo=input("Ingresa la caracteristica: ").upper().strip()
    valor_atributo=input("Ingresa el valor de la caracteristica: ").upper().strip()
    pelicula.update(atributo,valor_atributo)
    '''
    resp="si"
    while resp=="si":
        pelicula.update({"nombre":input("Ingrese el nombre: ").upper().strip()})
        pelicula.update({"categoria":input("Ingrese la categoria: ").upper().strip()})
        pelicula.update({"clasificacion":input("Ingrese la clasificacion: ").upper().strip()})
        pelicula.update({"genero":input("Ingrese el genero: ").upper().strip()})
        pelicula.update({"idioma":input("Ingrese el idioma: ").upper().strip()})

        cursor=conexion_bd.cursor()
        sql="INSERT INTO peliculas ( nombre, categoria, clasificacion, genero, idioma) " \
        "VALUES ( %s, %s %s, %s, %s)"
        val=(pelicula["nombre"],pelicula["categoria"],pelicula["clasificacion"],pelicula["genero"],
             pelicula["idioma"])
        cursor.execute(sql,val)
        conexion_bd.commit()


        resp=input("Quiere agregar mas cosas?").lower
    print("\n\t\t.::LA OPERACION SE REALIZO CON EXITO!::.")

def mostrarPeliculas():

    borrarPantalla()
    conexion_bd=conectar()
    if conexion_bd!=None:
        cursor=conexion_bd.cursor()
        sql="Select *FROM peliculas"
        cursor.execute(sql)
        registros=cursor.fetchall()
        for pelis in registros:
            print(f"{pelis[0]}{pelis[1]}{pelis[2]}{pelis[3]}{pelis[4]}{pelis[5]}")

        print("\n\t.::Mostrar caracteristicas::.\n")
        if (len(pelicula)>0):
            for i in pelicula:
                print(f"{i}:  {pelicula[i]}")
        else:
            print("\n\t.::No hay atributos por el momento::.\n")


        borrarPantalla()
        print("\n\t.::Borrar o quitar la pelicula::.\n")
        if len(pelicula)>0:
            resp=input("Desea borrar todas las caracteristicas?(si/no): ").lower().strip()
            if resp=="si":
                pelicula.clear()
        else:
            print("No hay peliculas que borrar ")
        print("\n\t\t.::LA OPERACION SE REALIZO CON EXITO!::.")
    

        borrarPantalla()
        print("\n\t.::Borrar o quitar una caracteristica::.\n")
        if len(pelicula)>0:
            for i in pelicula:
                print(f"{i}:  {pelicula[i]}")
            resp=input("Desea borrar una caracteristica(si/no): ").lower().strip()
            if resp=="si":
                resp2=input("Ingrese la caracteristica que desea borrar: ").lower().strip()
                if resp2 in pelicula:
                    pelicula.pop(resp2)
                    print("\n\t\t.::LA OPERACION SE REALIZO CON EXITO!::.")      
                else:
                    print("No hay una caracteristica llamada asi")        
        else:
            print("No hay valores registrados")


def buscar_peliculas():
    borrarPantalla()
    conexion_bd=conectar()
    if conexion_bd!=None:
        cursor=conexion_bd.cursor()
        sql="Select *FROM peliculas where nombre=%s"
        cursor.execute(sql)
        registros=cursor.fetchall()
        for pelis in registros:
            print(f"{pelis[0]}{pelis[1]}{pelis[2]}{pelis[3]}{pelis[4]}{pelis[5]}")

        print("\n\t.::Mostrar caracteristicas::.\n")
        if (len(pelicula)>0):
            for i in pelicula:
                print(f"{i}:  {pelicula[i]}")
        else:
            print("\n\t.::No hay atributos por el momento::.\n")


        borrarPantalla()
        print("\n\t.::Borrar o quitar la pelicula::.\n")
        if len(pelicula)>0:
            resp=input("Desea borrar todas las caracteristicas?(si/no): ").lower().strip()
            if resp=="si":
                pelicula.clear()
        else:
            print("No hay peliculas que borrar ")
        print("\n\t\t.::LA OPERACION SE REALIZO CON EXITO!::.")
    

        borrarPantalla()
        print("\n\t.::Borrar o quitar una caracteristica::.\n")
        if len(pelicula)>0:
            for i in pelicula:
                print(f"{i}:  {pelicula[i]}")
            resp=input("Desea borrar una caracteristica(si/no): ").lower().strip()
            if resp=="si":
                resp2=input("Ingrese la caracteristica que desea borrar: ").lower().strip()
                if resp2 in pelicula:
                    pelicula.pop(resp2)
                    print("\n\t\t.::LA OPERACION SE REALIZO CON EXITO!::.")      
                else:
                    print("No hay una caracteristica llamada asi")        
        else:
            print("No hay valores registrados")