from datetime import datetime
from bd_conexcion import cursor,conexion
import pandas as pd


def borrarpantalla():
    import os
    os.system("cls")

def esperartecla():
    opa=input("Oprima cualquier tecla para continuar :) ")

def menu_principal():
    proceso = True
    while proceso:
        borrarpantalla()
        print("\t\t\U0001F354----HAMBURGUESAS LAS MENONAS----\U0001F354\n")
        opcion=input("Elija la opción que desea realizar\n 1.-Registrar empleado\n 2.-Login\n 3.-Salir\n\U0001F449 ")
        return opcion

def obtener_menu():
    try:
        cursor.execute("SELECT * FROM menu")
        return cursor.fetchall()
    except Exception as e:
        print(f"\t\u26A0..::Error al obtener el menú: {e}")
        return []

def registrar_ventas(n_empleado,conexion):  
    borrarpantalla()
    print("\t\U0001F4B0..::Registrar Ventas::..\U0001F4B0")
    menu = obtener_menu()
    print("\n\t\U0001F354----Menú----\U0001F354")
    for i in menu:
        print(f"{i[0]}. {i[1]} - ${i[2]}")
    resp = True
    total = 0
    carrito={
        "n_producto": [],
        "nombre": [],
        "cantidad": [],
        "subtotal": []
    }
    while resp:
        np = input("\nIngrese el número del producto que desea vender: ").strip()
        cantidad = input("Ingrese la cantidad vendida: ").strip()
        try:
            cantidad = int(cantidad)
        except ValueError:
            print("Cantidad no válida, por favor ingrese un número entero.")
            continue
        cursor.execute("SELECT producto, precio FROM menu WHERE n_producto=%s", (np,))
        resultado = cursor.fetchone()
        if resultado:
            producto,precio = resultado
            subtotal = precio * cantidad
            total += subtotal
            
            carrito["n_producto"].append(np)
            carrito["nombre"].append(producto)
            carrito["cantidad"].append(cantidad)
            carrito["subtotal"].append(subtotal)

            print(f">> Se agregó: {producto} x {cantidad} --- Subtotal: ${subtotal} <<")
        else:
            print(f"Producto con número {np} no encontrado, por favor intente de nuevo.")
            continue
        preguntar = input("¿Desea agregar otro producto? (s/n): ").strip().lower()
        if preguntar != 's':
            resp = False
    fecha_venta = datetime.now()
    cursor.execute("INSERT INTO ventas (total, fecha, n_empleado) VALUES (%s, %s, %s)", (total, fecha_venta, n_empleado))
    conexion.commit()
    id_venta = cursor.lastrowid

    for i in range(len(carrito["n_producto"])):
        np = carrito["n_producto"][i]
        cantidad = carrito["cantidad"][i]
        subtotal = carrito["subtotal"][i]
        cursor.execute("INSERT INTO venta_detalle (id_venta, n_producto, cantidad, subtotal) " \
        "VALUES (%s, %s, %s, %s)",(id_venta, np, cantidad, subtotal))
    conexion.commit()
    print(f"\n\t\u2705 Venta registrada correctamente. Total: ${total} \u2705")
    print(f"\n\tID de venta: {id_venta} | Total: ${total}")
    print("\n\tTicket:")
    for i in range(len(carrito["n_producto"])):
        np = carrito["n_producto"][i]
        nombre = carrito["nombre"][i]
        cantidad = carrito["cantidad"][i]
        subtotal = carrito["subtotal"][i]
        print(f"{nombre} x {cantidad} = ${subtotal}")
    esperartecla()

def verventas():
    borrarpantalla()
    print("\t\U0001F9FE..::Mostrar ventas::..\U0001F9FE")
    try:
        cursor.execute("SELECT * FROM ventas")
        ventas = cursor.fetchall()
        if ventas:
            print("\n\t\U0001F4B0----Ventas Registradas----\U0001F4B0")
            fecha=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"{'ID':<5} {'Total':<10} {'Fecha':<20} {'N.Empleado':<10}")
            for venta in ventas:
                print(f"{venta[0]:<5} ${venta[1]:<10} {fecha:<20} {venta[3]:<10}")
                print(f"{'-'*50}")
        else:
            print("\t\u26A0..::No hay ventas registradas::..\u26A0")
        esperartecla()
    except Exception as e:
        print(f"\t\u26A0..::Error al obtener las ventas: {e}")
        return []
    
def revisainv():
    borrarpantalla()
    print("\t\U0001F4C8..::Revisar Inventario::..\U0001F4C8")
    try:
        cursor.execute("select * from inventario")
        inventario=cursor.fetchall()
        print(f"{'CÓDIGO':<10} {'PRODUCTO':<18} {'CANTIDAD':<10}")
        for i in inventario:
            print(f"{i[0]:<10} {i[1]:<18} {i[2]:<10}")
        esperartecla()
        return
    except Exception as e:
        print(f"\t\u26A0..::Error al obtener el inventario: {e}")
        return []

def modificarinv():
    borrarpantalla()
    print("\t\U0001F4C9..::Modificar Inventario::..\U0001F4C9")
    opcion=input("Elija la opción que desea realizar: \n 1.-Modificar cantidad de un producto\n 2.-Agregar nuevo producto\n 3.-Eliminar producto\n\U0001F449 ")
    while opcion not in ["1", "2", "3"]:
        print("Opción no válida, por favor intente de nuevo.")
        opcion = input("Elija la opción que desea realizar: \n 1.-Modificar cantidad de un producto\n " \
        "2.-Agregar nuevo producto\n 3.-Eliminar producto\n\U0001F449 ")   
    match opcion:
        case "1":
                print("\n\t\U0001F4C8----Modificar Cantidad de Producto----\U0001F4C8")
                try:
                    cursor.execute("select * from inventario")
                    inventario=cursor.fetchall()
                    print("\n\t\U0001F4C8----Inventario Actual----\U0001F4C8")
                    print(f"{'CÓDIGO':<10} {'PRODUCTO':<18} {'CANTIDAD':<10}")
                    for i in inventario:
                        print(f"{i[0]:<10} {i[1]:<18} {i[2]:<10}")
                    pregunta=input(f"\n¿Desea modificar algún producto del inventario? (s/n): ").strip().lower()
                    if pregunta=="s":
                        codigo=input("Ingrese el código del producto que desea modificar: ").strip()
                        cursor.execute("select * from inventario where codigo=%s",(codigo,))
                        producto=cursor.fetchone()
                        if producto:
                            ncantidad=input(f"Ingrese la nueva cantidad para el producto {producto[1]}: ").strip()
                            cursor.execute("update inventario set cantidad=%s where codigo=%s",(ncantidad,codigo))
                            conexion.commit()
                            print(f"\t\u2705 Producto {producto[1]} modificado correctamente \u2705")
                            esperartecla()
                        else:
                            print(f"\t\u26A0..::Producto con código {codigo} no encontrado, intentelo de nuevo::..\u26A0")
                            esperartecla()
                            return

                except Exception as e:
                    print(f"Error al modificar el inventario: {e}")
        case "2":
                borrarpantalla()
                print("\n\t\U0001F4C8----Agregar Producto----\U0001F4C8")
                nombre=input("Ingrese el nombre del nuevo producto: ").strip().lower()
                cantidad=input("Ingrese la cantidad del nuevo producto: ").strip()
                try:
                    cantidad = int(cantidad)
                except ValueError:
                    print("Cantidad no válida, por favor ingrese un número entero.")
                    return
                cursor.execute("insert into inventario (producto, cantidad) values (%s, %s)", (nombre, cantidad))
                conexion.commit()
                print(f"\t\u2705 Producto {nombre} agregado correctamente \u2705")
                esperartecla()
        case "3":
                borrarpantalla()
                print("\n\t\U0001F4C8----Eliminar Producto----\U0001F4C8")
                cursor.execute("select * from inventario")
                inventario=cursor.fetchall()
                print("\n\t\U0001F4C8----Inventario Actual----\U0001F4C8")
                print(f"{'CÓDIGO':<10} {'PRODUCTO':<18} {'CANTIDAD':<10}")
                for i in inventario:
                    print(f"{i[0]:<10} {i[1]:<18} {i[2]:<10}")
                cod=input("Ingrese el código del producto que desea eliminar: ").strip()
                cursor.execute("select * from inventario where codigo=%s", (cod,))
                producto = cursor.fetchone()
                confirmacion = input(f"¿Está seguro de eliminar el producto {producto[1]}? (s/n): ").strip().lower()
                if confirmacion == 's':
                    cursor.execute("delete from inventario where codigo=%s", (cod,))
                    conexion.commit()
                    print(f"\t\u2705 Producto {producto[1]} eliminado correctamente \u2705")
                    esperartecla()
                else:
                    print("\t\u26A0..::Operación cancelada::..\u26A0")
                    esperartecla()
        case "_":
                print("Opción no válida, por favor intente de nuevo.")
                esperartecla()
                return
        
def exportar_ventas_excel(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute(" SELECT  v.id_venta, v.fecha AS FechaVenta, vd.n_producto, " \
        "m.producto, vd.cantidad, vd.subtotal FROM ventas v JOIN venta_detalle vd " \
        "ON v.id_venta = vd.id_venta JOIN menu m ON vd.n_producto = m.n_producto;")
        datos = cursor.fetchall()
        if not datos:
            print("\n⚠ No hay ventas registradas para exportar.")
            return
        columnas = ["ID Venta", "Fecha", "N° Producto", "Producto", "Cantidad", "Subtotal"]
        df = pd.DataFrame(datos, columns=columnas)
        df["Fecha"] = pd.to_datetime(df["Fecha"], errors="coerce").dt.strftime("%Y-%m-%d")
        archivo = "ventas_exportadas.xlsx"
        df.to_excel(archivo, index=False)
        print(f"\n✅ Ventas exportadas exitosamente a '{archivo}'")
    except Exception as e:
        print(f"\n⚠ Error al exportar ventas: {e}")
