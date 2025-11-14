#Conexion y operaciones CRUD BDD AdventureWorks
# Author JGAS
# Consulta : Llamada a SP SQL Server
#2025/02/05

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


#4. Establece la conexión
try:
    conexion = pyodbc.connect(connection_string)

    #Parámetro de Entrada
    l_IDEstudiante = int(input("\n\n\tIngrese ID del Estudiante a Consultar: \t"))
    #Crear Cursor
    micursor = conexion.cursor()
    # 1. Ejemplo: Llamar a SP para Consulta la tabla "Estudiantes”
    SENTENCIA_SQL = "{CALL sp_ListadoEstudiantes (?)}"
    micursor.execute(SENTENCIA_SQL,(l_IDEstudiante))
    
    # Obtener los resultados  
    print("\n\n\t\t\tDatos del Estudiante:")
    rows = micursor.fetchall()
    
    #if rows:
    for row in rows:
    ##print(f"\t\t{row.NombreEstudiante}\t{row.ApellidoEstudiante}\t{row.Email}")
        print(row)

    print("\nOk ... Proceso Culminado con Exito: \n")
except Exception as e:
    print("\n \t Ocurrió un error al conectar a SQL Server: \n\n", e)
finally:
    print("Conexion Cerrada: \n")
