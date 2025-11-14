"""
    Conexión a SQLServer con Python
    Ejemplo de CRUD evitando inyecciones SQL
    
    @author Ing. Geovanni Aucancela Soliz

"""

# Función para leer registros

def consultar_registros(conexion):
    #Inicio
    try:
        # Establece la conexión
        #conexion = pyodbc.connect(connection_string)
        print("Conexion Exitosa:")  
        # 1.Cree una variable para la cadena de consulta SQL.
        SQL_QUERY = """
        SELECT IDEstudiante,NombreEstudiante,ApellidoEstudiante,Email,Telefono
        FROM Estudiantes
        """
        cursor = conexion.cursor()
        cursor.execute(SQL_QUERY)
        records = cursor.fetchall()
        for r in records:
            print(f"{r.IDEstudiante}\t{r.NombreEstudiante} \t {r.ApellidoEstudiante}\t{r.Email} \t {r.Telefono}")
    
    except Exception as e:
        print("\n \t Ocurrió un error al conectar a SQL Server: \n\n", e)
    
    finally:
        conexion.close()
        print("Conexion Finalizada")


def insertar_registros(conexion):
    ## Control de Errores
    try:
        
        with conexion.cursor() as micursor:
            
        
            # 1.Cree una variable para la cadena de INSERTAR SQL.     
            #SQL_STATEMENT = "INSERT INTO Production.Location (Name,CostRate,Availability,ModifiedDate) VALUES (?, ?, ?, GETDATE())"
            SQL_STATEMENT = """INSERT INTO Estudiantes
            (IDEstudiante,NombreEstudiante,ApellidoEstudiante,Email,Telefono)
            VALUES (?,?,?,?,?)"""
            ## Ingreso de Informacion
            l_IDEstudiante = int(input("Ingrese ID del Estudiante: \t"))
            l_NombreEstudiante = input("Ingrese Nombre Estudiante: \t")
            l_ApellidoEstudiante = input("Ingrese Apellido Estudiante:\t")
            l_Email = input("Ingrese Email Estudiante: \t")
            l_Telefono = input("Ingrese Telefono Estudiante:\t")        
            micursor.execute( SQL_STATEMENT,(l_IDEstudiante,l_NombreEstudiante,l_ApellidoEstudiante,l_Email,l_Telefono))
            
            conexion.commit()
    except Exception as e:
        print("\n \t Ocurrió un error De Conexión en SQL Server: \n\n Error:", e)

# Fin Insertar

def actualizar_registros(conexion):
    ## Control de Errores
    try:
        
        with conexion.cursor() as micursor:
            
        
            # 1.Cree una variable para la cadena de INSERTAR SQL.     
            #SQL_STATEMENT = "INSERT INTO Production.Location (Name,CostRate,Availability,ModifiedDate) VALUES (?, ?, ?, GETDATE())"
            SQL_STATEMENT = """UPDATE Estudiantes
            SET Email = ?
            WHERE IDEstudiante= ?"""
            ## Ingreso de Informacion
            l_IDEstudiante = int(input("Ingrese ID del Estudiante: \t"))
            l_Email = input("Ingrese Nuevo E-Mail Estudiante: \t")
            micursor.execute( SQL_STATEMENT,(l_Email,l_IDEstudiante))
            
            conexion.commit()
    except Exception as e:
        print("\n \t Ocurrió un error De Conexión en SQL Server: \n\n Error:", e)

# Fin Actualizar


def eliminar_registros(conexion):
    ## Control de Errores
    try:
        
        with conexion.cursor() as micursor:
            SQL_STATEMENT = """DELETE FROM Estudiantes
            WHERE IDEstudiante= ?"""
            ## Ingreso de Informacion
            print("\nEliminar Registro: \n")
            l_IDEstudiante = int(input("Ingrese ID del Estudiante : \t"))        
            micursor.execute( SQL_STATEMENT,(l_IDEstudiante))
            
            conexion.commit()
    except Exception as e:
        print("\n \t Ocurrió un error De Conexión en SQL Server: \n\n Error:", e)

# Fin Eliminar


# Función para listar opciones CRUD
def mostrar_opciones_crud():
    print("\t** SISTEMA CRUD UDEMYTEST ** \n")  
    print("\t***************************")  
    print("\tOpciones CRUD:\n")
    print("\t1. Crear registro")
    print("\t2. Consultar registros")
    print("\t3. Actualizar registro")
    print("\t4. Eliminar registro")
    print("\t5. Salir\n\n")

### Inicio  Programa principal ########
import pyodbc
# Datos de Conexion
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

# Inicio Conexion de BDD
try:
    # Establece la conexión
    conexion = pyodbc.connect(connection_string) 
except Exception as e:
    print("\n \t Ocurrió un error al conectar a SQL Server: \n\n", e)    
else:
    print("Conexion Exitosa:")  
# Fin Conexion de BDD

mostrar_opciones_crud()
opcion = input("Seleccione una opción 1-5:\t")

while True:
    if opcion == '1':
        #crear_registro(conexion)
        insertar_registros(conexion)
    elif opcion == '2':
        #leer_registros(conexion)
        consultar_registros(conexion)
    elif opcion == '3':
        actualizar_registros(conexion)
    elif opcion == '4':
        eliminar_registros(conexion)
    elif opcion == '5':
        conexion.close()
        print("Conexion Finalizada")
        print("Saliendo del programa..\n\n.")
    break
else:
    print("Opción no válida.")

    conexion.close()
