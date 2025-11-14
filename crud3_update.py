#Conexion y operaciones CRUD BDD AdventureWorks
# Author JGAS
# UUPDATE Record
#2024/11/15

# 1. Importar Biblioteca de conexión
import pyodbc

# 2. Declarar variables de Conexión
name_server ='localhost\SQLEXPRESS'
database ='UDEMYTEST1'
username ='pythonconsultor'
password = 'UDLA'
controlador_odbc='ODBC Driver 17 for SQL Server'

# 3. Crear Cadena de Conexion.
#3.1 Conexion Login SQL
connection_string = f'DRIVER={controlador_odbc};SERVER={name_server};DATABASE={database};UID={username};PWD={password}'

# 3.2 Con Autenticacion Windows
#connection_string = f'DRIVER={controlador_odbc};SERVER={name_server};DATABASE={database};Trusted_Connection=yes;'


#4. Establece la conexión y realiza Operacion CRUD

try:
    conexion = pyodbc.connect(connection_string)    
    #Crear Cursor
    micursor = conexion.cursor()
    
    SENTENCIA_SQL = """UPDATE Estudiantes
    SET Email = ?
    WHERE IDEstudiante= ?"""
    ## Ingreso de Informacion
    print("\n\t Actualizar Informacion Estudiante:\n")
    l_IDEstudiante = int(input("Ingrese ID del Estudiante: \t"))
    l_Email = input("Ingrese Nuevo E-Mail Estudiante: \t")
    micursor.execute( SENTENCIA_SQL,(l_Email,l_IDEstudiante))
    
    micursor.commit()
    print("\nOk ... Actualización Exitosa: \n")   
except Exception as e:
    print("\n \t Ocurrió un error al Actualizar con SQL Server: \n\n", e)

finally:
    conexion.close()
    print("Conexion Cerrada: \n")

