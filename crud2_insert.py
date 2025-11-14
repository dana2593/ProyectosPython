#Conexion y operaciones CRUD BDD AdventureWorks
# Author JGAS
# Insert Record
#2024/05/12

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
    #Crear Cursor
    micursor = conexion.cursor()
    # Ejemplo: Insertar Tabla Estudiantes 1 Registro
    SENTENCIA_SQL = """
    INSERT INTO Estudiantes
    (IDEstudiante,NombreEstudiante,ApellidoEstudiante,Email,Telefono)
    VALUES(?,?,?,?,?)
    """
    #one_record = ('10','Pepe','Muñoz','pepem@gmail.com','2378008')   
    #micursor.execute(SENTENCIA_SQL, one_record)
    print("\n\t\tINSERTAR NUEVO ESTUDIANTE:\n")  
     ## Ingreso de Informacion
    l_IDEstudiante = int(input("Ingrese ID del Estudiante: \t"))
    l_NombreEstudiante = input("Ingrese Nombre Estudiante: \t")
    l_ApellidoEstudiante = input("Ingrese Apellido Estudiante:\t")
    l_Email = input("Ingrese Email Estudiante: \t")
    l_Telefono = input("Ingrese Telefono Estudiante:\t")   
         
    micursor.execute( SENTENCIA_SQL,(l_IDEstudiante,l_NombreEstudiante,l_ApellidoEstudiante,l_Email,l_Telefono))
       
    #Realizar Commit
    micursor.commit()
    print("\nOk ... Insercion Exitosa: \n")  
except Exception as e:
    print("\n \t Ocurrió un error al insertar con SQL Server: \n\n", e)
      
finally:
    conexion.close()
    print("Conexion Cerrada: \n")
    

