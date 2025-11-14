import pyodbc
import json

class GestorEstudiantes:
    def __init__(self):
        try:
            with open("config.json", "r") as archivo:
                config = json.load(archivo)
            name_server = config["name_server"]
            database = config["database"]
            username = config["username"]
            password = config["password"]
            controlador = config["odbc_driver"]

            self.connection_string = (
                f"DRIVER={controlador};SERVER={name_server};DATABASE={database};"
                f"UID={username};PWD={password}"
            )

            self.conexion = pyodbc.connect(self.connection_string)
            cursor = self.conexion.cursor()
            cursor.execute("SELECT DB_NAME()")
            print("Conectado a la base de datos:", cursor.fetchone()[0])

        except Exception as e:
            print("❌ Error al conectar:", e)
            raise

    def consultar_estudiantes(self):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT IDEstudiante, NombreEstudiante, ApellidoEstudiante, Email, Telefono FROM Estudiantes ORDER BY IDEstudiante")
            rows = cursor.fetchall()
            print("\n===== LISTA DE ESTUDIANTES =====\n")
            for row in rows:
                print(f"{row.IDEstudiante}\t{row.NombreEstudiante}\t{row.ApellidoEstudiante}\t{row.Email}\t{row.Telefono}")
            print("\n=================================\n")
        except Exception as e:
            print("❌ Error al consultar:", e)

    def insertar_estudiante(self):
        try:
            cursor = self.conexion.cursor()
            print("\n===== INSERTAR ESTUDIANTE =====\n")
            IDEstudiante = int(input("ID Estudiante: "))
            Nombre = input("Nombre: ")
            Apellido = input("Apellido: ")
            Email = input("Email: ")
            Telefono = input("Telefono: ")

            cursor.execute(
                "INSERT INTO Estudiantes (IDEstudiante, NombreEstudiante, ApellidoEstudiante, Email, Telefono) VALUES (?, ?, ?, ?, ?)",
                (IDEstudiante, Nombre, Apellido, Email, Telefono)
            )

            self.conexion.commit()
            print("\n✔ Commit realizado.")

            cursor.execute("SELECT IDEstudiante, NombreEstudiante, ApellidoEstudiante, Email, Telefono FROM Estudiantes WHERE IDEstudiante = ?", (IDEstudiante,))
            row = cursor.fetchone()
            if row:
                print("\n✔ Inserción verificada. Registro encontrado:")
                print(f"{row.IDEstudiante}\t{row.NombreEstudiante}\t{row.ApellidoEstudiante}\t{row.Email}\t{row.Telefono}")
            else:
                print("\n⚠️ No se encontró el registro tras el INSERT.")

        except Exception as e:
            print("❌ Error al insertar:", e)

    def actualizar_email(self):
        try:
            cursor = self.conexion.cursor()
            print("\n===== ACTUALIZAR EMAIL =====\n")
            IDEstudiante = int(input("Ingrese ID del estudiante: "))
            Email = input("Nuevo Email: ")
            cursor.execute("UPDATE Estudiantes SET Email = ? WHERE IDEstudiante = ?", (Email, IDEstudiante))
            self.conexion.commit()
            print("\n✔ Registro actualizado correctamente.")
        except Exception as e:
            print("❌ Error al actualizar:", e)

    def eliminar_estudiante(self):
        try:
            cursor = self.conexion.cursor()
            print("\n===== ELIMINAR ESTUDIANTE =====\n")
            IDEstudiante = int(input("ID del estudiante a eliminar: "))
            cursor.execute("DELETE FROM Estudiantes WHERE IDEstudiante = ?", (IDEstudiante,))
            self.conexion.commit()
            print("\n✔ Registro eliminado correctamente.")
        except Exception as e:
            print("❌ Error al eliminar:", e)

    def ejecutar_menu(self):
        while True:
            print("""
===== SISTEMA CRUD OOP – ESTUDIANTES =====
1. Consultar Estudiantes
2. Insertar Estudiante
3. Actualizar Email
4. Eliminar Estudiante
5. Salir
============================================
""")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.consultar_estudiantes()
            elif opcion == "2":
                self.insertar_estudiante()
            elif opcion == "3":
                self.actualizar_email()
            elif opcion == "4":
                self.eliminar_estudiante()
            elif opcion == "5":
                print("\n👋 Saliendo...\n")
                break
            else:
                print("\n❌ Opción no válida.\n")

if __name__ == "__main__":
    gestor = GestorEstudiantes()
    gestor.ejecutar_menu()
