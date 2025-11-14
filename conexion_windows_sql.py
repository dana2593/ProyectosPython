import pyodbc
# Datos de Conexión
name_server = 'DESKTOP-6GO61O3\SQLEXPRESS'
database ='AdventureWorks2008R2'
username ='pythonconect'
password = 'UDLA'
controlador_odbc='SQL Server'
#Otros controladores más utilizados:
# SQL Server
# ODBC Driver 17 for SQL Server
# ODBC Driver 18 for SQL Server

#Conexion Windows
#connection_string = f'DRIVER={controlador_odbc};SERVER={name_server};DATABASE={database};Trusted_Connection=yes;'

# Conexion SQL
#connection_string = f'DRIVER={controlador_odbc};SERVER={name_server};DATABASE={database};UID={username};PWD={password}'

# Establece la conexión
conn = pyodbc.connect(connection_string)
#Creacion de Cursor
cursor_personas = conn.cursor()
# Ejemplo: Consulta la tabla "Person.Person" con autenticación Windows
cursor_personas.execute('SELECT TOP 20 LastName,FirstName FROM Person.Person')
rows = cursor_personas.fetchall()
for row in rows:
    print(row)
# Cierra la conexión
conn.close()
