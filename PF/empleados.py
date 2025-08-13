from bd_conexcion import*
import hashlib
import datetime

def hash_password(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()

def registrar_empleado(nombre, apellidos, telefono,contrasena):
    try:
        fecha = datetime.datetime.now()
        contrasena=hash_password(contrasena)
        cursor.execute("insert into empleados (nombre,apellidos,telefono,contrasena,fecha_ingreso) values (%s,%s,%s,%s,%s)",(nombre, apellidos, telefono, contrasena, fecha))
        conexion.commit()
        return True
    except Exception as e:
        print(f"\t\u26A0..::Error al registrar empleado: {e}")
        return False
    
def inicio_sesion(n_empleado,contrasena):
    try:
        contrasena=hash_password(contrasena)
        cursor.execute("select * from empleados where n_empleado=%s and contrasena=%s",(n_empleado,contrasena)) 
        return cursor.fetchone()
    except Exception as e:
        print(f"\t\u26A0..::Error al iniciar sesión: {e}")
        return False