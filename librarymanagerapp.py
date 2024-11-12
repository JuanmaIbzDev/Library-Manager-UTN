# Library Manager UTN
# Para más información puede leer #Documentation.txt 
# Autor: Juan Manuel Vargas

import os
import platform
import mysql.connector
from tabulate import tabulate
from datetime import datetime

def conectar():
    try:
        db = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            database="gestor_biblioteca"
        )
        return db
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def ejecutar_consulta(query, params=()):
    db = conectar()
    if db is None:
        return
    
    try:
        cursor = db.cursor()
        cursor.execute(query, params)
        db.commit()
        return cursor
    
    except mysql.connector.Error as err:
        print(f"Error en la consulta: {err}")

    finally: 
        db.close()

def obtener_datos(query, params=()):
    db = conectar()
    if db is None:
        return
    
    try:
        cursor = db.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
    
    except mysql.connector.Error as err:
        print(f"Error en la consulta: {err}")
    
    finally:
        db.close()

def limpiar_consola():
    sistema = platform.system()

    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def usuario_activo_check(usuario_id):
    query = "SELECT estado FROM usuarios WHERE id = %s"
    resultado_usuario = obtener_datos(query, (usuario_id,))
    return resultado_usuario and resultado_usuario[0][0] == 1

def libro_activo_check(libro_id):
    query = "SELECT estado FROM libros WHERE id = %s"
    resultado_libro = obtener_datos(query, (libro_id,))
    return resultado_libro and resultado_libro[0][0] == 1

def crear_usuario():
    limpiar_consola()
    nombre = input("Ingrese el Nombre: ")
    apellido = input("Ingrese el Apellido: ")
    dni = input("Ingrese el DNI: ")
    telefono = input("Ingrese el número de Teléfono: ")
    email = input("Ingrese el Email: ")
    query = """
        INSERT INTO usuarios (nombre, apellido, dni, telefono, email, creado_el, actualizado_el, estado)
        VALUES (%s, %s, %s, %s, %s, NOW(), NOW(), 1)
    """
    ejecutar_consulta(query,(nombre, apellido, dni, telefono, email))
    print("El usuario ha sido creado correctamente.")

def actualizar_usuario():
    limpiar_consola()
    usuario_id = input("Ingrese el ID del usuario a actualizar: ")
    nuevo_nombre = input("Ingrese el nuevo nombre: ")
    nuevo_apellido = input("Ingrese el nuevo apellido: ")
    nuevo_dni = input("Ingrese el nuevo DNI: ")
    nuevo_telefono = input("Ingrese el nuevo teléfono: ")
    nuevo_email = input("Ingrese el nuevo email: ")
    query = """
        UPDATE usuarios SET nombre = %s, apellido = %s, dni = %s, telefono = %s, email = %s, actualizado_el = NOW()
        WHERE id = %s
    """
    ejecutar_consulta(query, (nuevo_nombre, nuevo_apellido, nuevo_dni, nuevo_telefono, nuevo_email, usuario_id))
    print(f"El usuario con el ID {usuario_id} ha sido actualizado correctamente.")

def onoff_usuario():
    limpiar_consola()
    usuario_id = input("Ingrese el id del usuario: ")
    onoff = int(input("¿Desea desactivar o activar el usuario? 1(Activar) 2(Desactivar)"))
    try:
        if onoff == 0:
            query = """UPDATE usuarios SET estado = 0, actualizado_el = NOW() 
            WHERE id = %s
            """
            ejecutar_consulta(query, (usuario_id,))
            print(f"El usuario con el id {usuario_id} ha sido desactivado.")
        
        elif onoff == 1:
            query = """UPDATE usuarios SET estado = 1, actualizado_el = NOW() 
            WHERE id = %s
            """
            ejecutar_consulta(query, (usuario_id,))
            print(f"El usuario con el id {usuario_id} ha sido activado.")
    except:
        print("Ingrese una opción válida.")

def crear_libro():
    limpiar_consola()
    nombre_libro = input("Ingrese el nombre del libro: ")
    autor = input("Ingrese el nombre del Autor del libro: ")
    fecha_lanzamiento = input("Ingrese la fecha de lanzamiento (AAAA-MM-DD): ")
    id_genero = input("Ingrese el ID del género: ")
    query = """INSERT INTO libros (nombre_libro, autor, fecha_lanzamiento, id_genero, creado_el, actualizado_el, estado) 
    VALUES (%s, %s, %s, %s, NOW(), NOW(), 1)
    """
    ejecutar_consulta(query, (nombre_libro, autor, fecha_lanzamiento, id_genero))
    print("El libro ha sido agregado correctamente.")

def actualizar_libro():
    limpiar_consola()
    libro_id = input("Ingrese el id del libro a modificar: ")
    nuevo_nombre_libro = input("Ingrese el nuevo nombre del libro: ")
    nuevo_autor = input("Ingrese el nombre del autor: ")
    nueva_fecha_lanzamiento = input("Ingrese la fecha de lanzamiento (AAAA-MM-DD): ")
    query = """UPDATE libros SET nombre_libro = %s, autor = %s, fecha_lanzamiento = %s, actualizado_el = NOW() 
    WHERE id = %s
    """
    ejecutar_consulta(query, (nuevo_nombre_libro, nuevo_autor, nueva_fecha_lanzamiento, libro_id))
    print(f"El libro con el id {libro_id} ha sido actualizado correctamente.")

def onoff_libro():
    limpiar_consola()
    libro_id = input("Ingrese el id del libro: ")
    onoff = input("¿Desea desactivar o activar el libro? 1(Activar) 2(Desactivar)")
    try:
        if onoff == 0:
            query = """UPDATE libros SET estado = 0, actualizado_el = NOW() 
            WHERE id = %s
            """
            ejecutar_consulta(query, (libro_id,))
            print(f"El libro con el id {libro_id} ha sido desactivado.")
        
        elif onoff == 1:
            query = """UPDATE libros SET estado = 0, actualizado_el = NOW() 
            WHERE id = %s
            """
            ejecutar_consulta(query, (libro_id,))
            print(f"El libro con el id {libro_id} ha sido activado.")
    except:
        print("Ingrese una opción válida.")

def crear_genero():
    limpiar_consola()
    genero = input("Ingrese el nombre del género a agregar: ")
    query = """INSERT INTO generos (genero) 
    VALUES (%s)
    """ 
    ejecutar_consulta(query, (genero,))
    print("El género ha sido agregado correctamente.")

def actualizar_genero():
    limpiar_consola()
    genero_id = input("Ingrese el id del género a modificar: ")
    nuevo_nombre_genero = input("Ingrese el nombre del género: ")
    query = """UPDATE generos SET genero = %s 
    WHERE id = %s
    """
    ejecutar_consulta(query, (nuevo_nombre_genero, genero_id))
    print("El genero ha sido actualizado correctamente.")

def crear_prestamo():
    limpiar_consola()
    try:
        usuario_id = input("Inserte el ID del usuario: ")
        if not usuario_activo_check(usuario_id):
            input("El usuario está inactivo o no existe. No se puede crear el préstamo.")
            return

        print("Usuario activo.")
        
        libro_id = input("Ingrese el ID del libro: ")
        if not libro_activo_check(libro_id):
            input("El libro está inactivo o no disponible para préstamo.")
            return

        print("Libro disponible para préstamo.")

        fecha_prestamo = input("Ingrese la fecha del préstamo (AAAA-MM-DD): ")
        fecha_devolucion_estimada = input("Ingrese la fecha de devolución estimada (AAAA-MM-DD): ")

        query = """INSERT INTO prestamos (usuario_id, libro_id, fecha_prestamo, fecha_devolucion_estimada, fecha_devolucion_real)
                VALUES (%s, %s, %s, %s, NOW())"""
        ejecutar_consulta(query, (usuario_id, libro_id, fecha_prestamo, fecha_devolucion_estimada))

        input("El préstamo ha sido creado correctamente.")

    except ValueError:
        input("Error: Formato de fecha inválido. Utilice el formato (AAAA-MM-DD).")
    except Exception as e:
        input(f"Ocurrió un error al crear el préstamo: {e}")

def actualizar_fecha_devolucion_real():
    limpiar_consola()
    prestamo_id = input("Ingrese el ID del préstamo: ")
    try:
        fecha_devolucion_real = input("Ingrese la fecha de devolución real (AAAA-MM-DD): ")
        fecha_devolucion_real = datetime.strptime(fecha_devolucion_real, '%Y-%m-%d')
        
        query = """SELECT fecha_devolucion_estimada, usuario_id FROM prestamos WHERE id = %s"""
        prestamo_info = obtener_datos(query, (prestamo_id,))
        
        if prestamo_info:
            fecha_devolucion_estimada, usuario_id = prestamo_info[0]
            fecha_devolucion_estimada = datetime.strptime(fecha_devolucion_estimada, '%Y-%m-%d')
            
            query = """UPDATE prestamos SET fecha_devolucion_real = %s WHERE id = %s"""
            ejecutar_consulta(query, (fecha_devolucion_real, prestamo_id))
            input("Fecha de devolución real actualizada.")
            
            if fecha_devolucion_real > fecha_devolucion_estimada:
                query = """UPDATE usuarios SET estado = 0 WHERE id = %s"""
                ejecutar_consulta(query, (usuario_id,))
                input("Usuario desactivado por devolución fuera del tiempo estimado.")
        else:
            input("No se encontró el préstamo con el ID proporcionado.")
    
    except ValueError:
        input("Error: Formato de fecha inválido. Utilice el formato (AAAA-MM-DD).")
    except Exception as e:
        input(f"Ocurrió un error al actualizar la fecha de devolución real: {e}")

# Tablas

def mostrar_tabla(tabla, columna_orden):
    limpiar_consola()
    db = conectar()
    if db is None:
        input("No se pudo conectar a la base de datos.")
        return

    try:
        cursor = db.cursor()
        query = f"SELECT * FROM {tabla} ORDER BY LENGTH({columna_orden}) ASC"
        cursor.execute(query)
        resultados = cursor.fetchall()
        columnas = [descripcion[0] for descripcion in cursor.description]

        print(tabulate(resultados, headers=columnas, tablefmt="fancy_grid"))
        input("Presione ENTER para continuar...")

    except Exception as e:
        input(f"Ocurrió un problema al mostrar la tabla: {e}")
    
    finally:
        db.close()

def tabla_usuarios():
    limpiar_consola()
    mostrar_tabla("usuarios", "nombre")

def tabla_libros():
    limpiar_consola()
    db = conectar()
    cursor = db.cursor()

    cursor.execute("SELECT id, nombre_libro, autor, fecha_lanzamiento, id_genero, creado_el, actualizado_el, estado FROM libros ORDER BY LENGTH(nombre_libro)")
    libros = cursor.fetchall()

    cursor.close()
    db.close()

    print(f"{'ID':<5} {'Libro':<30} {'Autor':<25} {'Lanzamiento':<15} {'Genero ID':<10} {'Creado':<20} {'Actualizado':<20} {'Estado':<6}")
    print("=" * 140)

    for libro in libros:
        id, nombre_libro, autor, fecha_lanzamiento, id_genero, creado_el, actualizado_el, estado = libro
        print(f"{id:<5} {nombre_libro[:30]:<30} {autor[:25]:<25} {str(fecha_lanzamiento):<15} {id_genero:<10} {str(creado_el):<20} {str(actualizado_el):<20} {estado:<6}")
    input("Presione ENTER para continuar...")

def tabla_generos():
    limpiar_consola()
    mostrar_tabla("generos", "genero")

def tabla_prestamos():
    limpiar_consola()
    mostrar_tabla("prestamos", "fecha_prestamo")


def menu():
    limpiar_consola()
    opciones = {
        1: crear_usuario,
        2: actualizar_usuario,
        3: onoff_usuario,
        4: crear_libro,
        5: actualizar_libro,
        6: onoff_libro,
        7: crear_genero,
        8: actualizar_genero,
        9: crear_prestamo,
        10: actualizar_fecha_devolucion_real,
        11: tabla_usuarios,
        12: tabla_libros,
        13: tabla_generos,
        14: tabla_prestamos,
        15: exit,
    }

    while True:
        os.system("cls")
        print("""
            =========== LIBRARY MANAGER UTN ==========
            |USUARIOS:                               |
            |- 1) Crear Usuario.                     |
            |- 2) Actualizar Usuario.                |
            |- 3) Activar/Desactivar Usuario.        |
            |                                        |
            |LIBROS:                                 |
            |- 4) Crear Libro.                       |
            |- 5) Actualizar Libro.                  |
            |- 6) Activar/Desactivar Libro.          |
            |                                        |
            |GÉNEROS:                                |
            |- 7) Crear Género Literario.            |
            |- 8) Actualizar Género Literario.       |
            |                                        |
            |PRÉSTAMOS:                              |
            |- 9) Crear Préstamo.                    |
            |- 10) Actualizar Entrega de Libro.      |
            |                                        |
            |TABLAS:                                 |
            |- 11) Mostrar Tabla de Usuarios.        |
            |- 12) Mostrar Tabla de Libros.          |
            |- 13) Mostrar Tabla de Generos.         |
            |- 14) Mostrar Tabla de Préstamos.       |
            |                                        |
            |SALIR:                                  |
            |- 15) Salir del programa.               |   
            """)
        
        try:
            opcion = int(input("            |Elija una opción: "))
            funcion = opciones.get(opcion)
            if funcion:
                funcion()
            else:
                print("Opción no válida.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

menu()