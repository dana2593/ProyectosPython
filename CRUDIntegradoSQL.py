# CRUD Completo Estudiantes - SQL Server
# Autor: JGAS Adaptado
# 2024/11/15

import pyodbc

# Datos de Conexión
name_server ='localhost\\SQLEXPRESS'
database ='UDEMYTEST1'
username ='pythonconsultor'
password = 'UDLA'
controlador_odbc='ODBC Driver 17 for SQL Server'

# Cadena de conexión
connection_string = f'DRIVER={controlador_odbc};SERVER={name_server};DATABASE={database};UID={username};PWD={password}'

def conectar():
    return pyodbc.connect(connection_string)

# ============ CRUD ============

def listar_estudiantes():
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT IDEstudiante,NombreEstudiante,ApellidoEstudiante,Email,Telefono FROM Estudiantes")
        rows = cursor.fetchall()

        print("\n===== LISTA DE ESTUDIANTES =====\n")
        for row in rows:
            print(f"{row.IDEstudiante}\t{row.NombreEstudiante}\t{row.ApellidoEstudiante}\t{row.Email}\t{row.Telefono}")
        print("\n=================================\n")

    except Exception as e:
        print("Error:", e)
    finally:
        conexion.close()


def insertar_estudiante():
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        print("\n===== INSERTAR ESTUDIANTE =====\n")
        IDEstudiante = int(input("ID Estudiante: "))

        
        cursor.execute("SELECT COUNT(*) FROM Estudiantes WHERE IDEstudiante = ?", (IDEstudiante,))
        existe = cursor.fetchone()[0]

        if existe > 0:
            print("\n El ID ingresado YA EXISTE en la base de datos. Intente con otro ID.\n")
            return 

        Nombre = input("Nombre: ")
        Apellido = input("Apellido: ")
        Email = input("Email: ")
        Telefono = input("Telefono: ")

        cursor.execute("""
            INSERT INTO Estudiantes (IDEstudiante,NombreEstudiante,ApellidoEstudiante,Email,Telefono)
            VALUES (?,?,?,?,?)
        """, (IDEstudiante, Nombre, Apellido, Email, Telefono))

        conexion.commit()
        print("\n Registro Insertado Correctamente.\n")

    except Exception as e:
        print("Error al insertar:", e)
    finally:
        conexion.close()


def actualizar_estudiante():
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        print("\n===== ACTUALIZAR EMAIL =====\n")
        IDEstudiante = int(input("Ingrese ID del estudiante: "))
        Email = input("Nuevo Email: ")

        cursor.execute("""
            UPDATE Estudiantes
            SET Email = ?
            WHERE IDEstudiante = ?
        """, (Email, IDEstudiante))

        conexion.commit()
        print("\n Registro Actualizado Correctamente.\n")

    except Exception as e:
        print("Error al actualizar:", e)
    finally:
        conexion.close()


def eliminar_estudiante():
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        print("\n===== ELIMINAR ESTUDIANTE =====\n")
        IDEstudiante = int(input("ID del estudiante a eliminar: "))

        cursor.execute("DELETE FROM Estudiantes WHERE IDEstudiante = ?", (IDEstudiante,))
        conexion.commit()

        print("\n Registro Eliminado Correctamente.\n")

    except Exception as e:
        print("Error al eliminar:", e)
    finally:
        conexion.close()


# ============ MENÚ ============

def menu():
    while True:
        print("""
===== SISTEMA CRUD ESTUDIANTES =====

1. Listar Estudiantes
2. Insertar Estudiante
3. Actualizar Estudiante
4. Eliminar Estudiante
5. Salir

====================================
""")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listar_estudiantes()
        elif opcion == "2":
            insertar_estudiante()
        elif opcion == "3":
            actualizar_estudiante()
        elif opcion == "4":
            eliminar_estudiante()
        elif opcion == "5":
            print("\nSaliendo...\n")
            break
        else:
            print("\n Opción no válida.\n")


# Ejecutar
menu()
2