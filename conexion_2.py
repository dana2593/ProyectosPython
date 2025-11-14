#Conexion a la BDD AdventureWorks
# Author JGAS
#2024/0512



database ='AdventureWorks2008R2'
name_server ='DESKTOP-6GO61O3\\SQLEXPRESS'
#username ='pythonconect'
#password = 'UDLA'

#La biblioteca json es la librería estándar de Python 
#para trabajar con archivos JSON
import json

with open("config.json") as f:
    datos_conexion = json.load(f)
    username = datos_conexion["sql_server"]["user"]
    password = datos_conexion["sql_server"]["password"]


import pyodbc

#Conexion Login SQL
connection_string = f'DRIVER={{SQL Server}};SERVER={name_server};DATABASE={database};UID={username};PWD={password}'

# Autenticacion Windows
#connection_string = f'DRIVER={{SQL Server}};SERVER={name_server};DATABASE={database};Trusted_Connection=yes;'

# Establece la conexión
try:
    conexion = pyodbc.connect(connection_string)
    #Crear Cursor
    micursor = conexion.cursor()
    
    # Ejemplo: Consulta la tabla "Person.Person”
    micursor.execute('SELECT LastName,FirstName FROM Person.Person')
    rows = micursor.fetchall()
    for row in rows:
        print(f"{row.LastName}\t{row.FirstName}")
    
except Exception as e:
    print("\n \t Ocurrió un error al conectar a SQL Server: \n\n", e)
else:
    print("Ok ... Conexión Exitosa: \n")
finally:
    print("Fin Conexion: \n")
    #conexion.close()
