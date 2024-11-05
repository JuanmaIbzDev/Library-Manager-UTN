# Usamos las bibliotecas "os" que nos permitirá realizar en este caso, la limpieza de la consola para obtener un código
# mucho más limpio. Y también usamos la biblioteca "mysql.connector" que es fundamental para conectar nuestra base de
# datos al programa, esta biblioteca se intala con pip install mysql-connector-python desde la terminal.
import os
import mysql.connector
from tabulate import tabulate


# Realizamos la conexión a la base de datos.
db = mysql.connector.connect(
    user="root",
    password="",
    host="localhost",
    database="gestor_biblioteca"
    )
# Procedemos a crear una variable y le designamos el cursor de la db para facilitar su uso en nuestras operaciones.
cursor = db.cursor()

# APARTADO DE FUNCIONES:
# Designaremos todas las funciones junto a sus parámetros para que el programa las lea primeras y asi luego
# simplemente realizamos el llamado a la función desde el menú interactivo.
# Todas las funciones están acompañadas de un print que avisa que la acción se haya realizado correctamente.

def crear_usuario():
    # =========== FUNCIÓN PARA CREAR UN USUARIO ===========
    # Se crea un usuario nuevo en la base de datos.
    #
    # Solicita al operador que ingrese el nombre, apellido, DNI, teléfono y email.
    # Luego, inserta estos datos en la tabla 'usuarios' añadiendo automáticamente el log "creado_el" y "actualizado_el" con el
    # timestamp actual, además de que se setea automáticamente el valor de "estado" a 1, que significa activo.
    # No se aplican parámetros especiales ni tampoco retorna ningún dato.
    nombre = input("Ingrese el Nombre: ")
    apellido = input("Ingrese el Apellido: ")
    dni = input("Ingrese el DNI: ")
    telefono = input("Ingrese el número de Teléfono: ")
    email = input("Ingrese el Email: ")
    cursor.execute("INSERT INTO usuarios (nombre, apellido, dni, telefono, email, creado_el, actualizado_el, estado) VALUES (%s, %s, %s, %s, %s, NOW(), NOW(), 1)", (nombre, apellido, dni, telefono, email))
    db.commit()
    print("El usuario ha sido creado correctamente.")

def actualizar_usuario():
    # =========== FUNCIÓN PARA ACTUALIZAR UN USUARIO ===========
    # Se modifican los valores de un usuario ya creado en la base de datos.
    #
    # Solicita al operador que ingrese el ID del usuario a modificar, luego los nuevos valores: nombre, apellido, DNI, teléfono y email.
    # Luego, inserta estos datos en la tabla 'usuarios' y se añade automáticamente el log de "actualizado_el" con el timestamp actual.
    # No se aplican parámetros especiales ni tampoco retorna ningún dato.
    usuario_id = input("Ingrese el ID del usuario a actualizar: ")
    nuevo_nombre = input("Ingrese el nuevo nombre: ")
    nuevo_apellido = input("Ingrese el nuevo apellido: ")
    nuevo_dni = input("Ingrese el nuevo DNI: ")
    nuevo_telefono = input("Ingrese el nuevo teléfono: ")
    nuevo_email = input("Ingrese el nuevo email: ")

    # Ejecuta la actualización con todos los datos
    cursor.execute("UPDATE usuarios SET nombre = %s, apellido = %s, dni = %s, telefono = %s, email = %s, actualizado_el = NOW() WHERE id = %s", (nuevo_nombre, nuevo_apellido, nuevo_dni, nuevo_telefono, nuevo_email, usuario_id))
    db.commit()
    print(f"El usuario con el id {usuario_id} ha sido correctamente actualizado.")

def desactivar_usuario():
    # =========== FUNCIÓN PARA DESACTIVAR UN USUARIO ===========
    # Se modifican el estado a 0 (inactivo) de un usuario ya creado en la base de datos.
    #
    # Solicita al operador que ingrese el ID del usuario a modificar, una vez colocado la función 
    # coloca el estado (1) activo del usuario a inactivo (0).
    # No se aplican parámetros especiales ni tampoco retorna ningún dato.
    usuario_id = input("Ingrese el id del usuario que desea desactivar: ")
    cursor.execute("UPDATE usuarios SET estado = 0, actualizado_el = NOW() WHERE id = %s", (usuario_id,))
    db.commit()
    print(f"El usuario con el id {usuario_id} ha sido correctamente desactivado.")

def agregar_libro():
    # =========== FUNCIÓN PARA AGREGAR UN LIBRO ===========
    # Se añade un nuevo libro a la base de datos.
    #
    # Solicita al operador que ingrese el nombre, autor y fecha de lanzamiento del libro, además también se le solicita el id del género
    # al que el libro pertenece.
    # Luego, inserta estos datos en la tabla 'libros' y se añade automáticamente el log de "creado_el" y "actualizado_el" con el timestamp actual.
    # y se añade el estado a 1 (activo).
    # No se aplican parámetros especiales ni tampoco retorna ningún dato.
    nombre_libro = input("Ingrese el nombre del libro: ")
    autor = input("Ingrese el nombre del Autor del libro: ")
    fecha_lanzamiento = input("Ingrese la fecha de lanzamiento (AAAA-MM-DD): ")
    id_genero = input("Ingrese el ID del género: ")
    cursor.execute("INSERT INTO libros (nombre_libro, autor, fecha_lanzamiento, id_genero, creado_el, actualizado_el, estado) VALUES (%s, %s, %s, %s, NOW(), NOW(), 1)", (nombre_libro, autor, fecha_lanzamiento, id_genero))
    db.commit()
    print("El libro ha sido agregado correctamente.")

def actualizar_libro():
    # =========== FUNCIÓN PARA ACTUALIZAR UN LIBRO ===========
    # Se modifican los valores de un libro ya creado en la base de datos.
    #
    # Solicita al operador que ingrese el ID del libro a modificar, luego los nuevos valores: nombre, autor y fecha de lanzamiento.
    # Luego, inserta estos datos en la tabla 'libros' y se añade automáticamente el log de "actualizado_el" con el timestamp actual.
    # No se aplican parámetros especiales ni tampoco retorna ningún dato.
    libro_id = input("Ingrese el id del libro a modificar: ")
    nuevo_nombre_libro = input("Ingrese el nuevo nombre del libro: ")
    nuevo_autor = input("Ingrese el nombre del autor: ")
    nueva_fecha_lanzamiento = input("Ingrese la fecha de lanzamiento (AAAA-MM-DD): ")
    cursor.execute("UPDATE libros SET nombre_libro = %s, autor = %s, fecha_lanzamiento = %s, actualizado_el = NOW() WHERE id = %s",(nuevo_nombre_libro, nuevo_autor, nueva_fecha_lanzamiento, libro_id))
    db.commit()
    print(f"El libro con el id {libro_id} ha sido actualizado correctamente.")

def desactivar_libro():
    # =========== FUNCIÓN PARA DESACTIVAR UN LIBRO ===========
    # Se modifican el estado a 0 (inactivo) de un libro ya creado en la base de datos.
    #
    # Solicita al operador que ingrese el ID del libro a modificar.
    # Luego de esto la función cambia el estado a 0 (inactivo) y crea el log de "actualizado_el" con el
    # timestamp actual.
    # No se aplican parámetros especiales ni tampoco retorna ningún dato.
    libro_id = input("Ingrese el id del libro a desactivar: ")
    cursor.execute("UPDATE libros SET estado = 0, actualizado_el = NOW() WHERE id = %s", (libro_id,))
    db.commit()
    print(f"El libro con el id {libro_id} ha sido desactivado correctamente.")

def agregar_genero():
    # =========== FUNCIÓN PARA AÑADIR UN GÉNERO DE LIBRO ===========
    # Se añade un nuevo género de libro en la base de datos.
    #
    # Solicita al operador que ingrese el nombre del genero a agregar y luego
    # se inserta el dato en la tabla "generos" de la base de datos.
    # No se aplican parámetros especiales ni tampoco retorna ningún dato.
    genero = input("Ingrese el nombre del género a agregar: ")
    cursor.execute("INSERT INTO generos (genero) VALUES (%s)", (genero,))
    db.commit()
    print("El género ha sido agregado correctamente.")

def actualizar_genero():
    # =========== FUNCIÓN PARA ACTUALIZAR UN GÉNERO DE LIBRO ===========
    # Se actualiza el nombre de un género de libro en la base de datos.
    #
    # Solicita al operador que ingrese el ID del género a modificar, luego se pide el nuevo nombre del genero
    # y se inserta el dato en la tabla "generos" de la base de datos.
    # No se aplican parámetros especiales ni tampoco retorna ningún dato.
    genero_id = input("Ingrese el id del género a modificar: ")
    nuevo_nombre_genero = input("Ingrese el nombre del género: ")
    cursor.execute("UPDATE generos SET genero = %s WHERE id = %s", (nuevo_nombre_genero, genero_id))
    db.commit()
    print("El genero ha sido actualizado correctamente.")

def crear_prestamo():
    # =========== FUNCIÓN PARA CREAR UN PRÉSTAMO DE LIBRO ===========
    # Se agrega un nuevo préstamo de libro en la base de datos.
    #
    # Solicita al operador que ingrese el id del usuario al que se realizará el prestamo, luego
    # se solicita el ID del libro que se prestará y por último se solicitan las fechas de:
    # - Prestamo(fecha de cuando se realizó el prestamo). 
    # - Devolución estimada(fecha de finalización del préstamo)
    # - Devolución real(fecha en la cual el usuario devuelve el libro).
    # No se aplican parámetros especiales ni tampoco retorna ningún dato.
    usuario_id = input("Inserte el ID del usuario: ")
    libro_id = input("Ingrese el ID del libro: ")
    fecha_prestamo = input("Ingrese la fecha del prestamo (AAAA-MM-DD): ")
    fecha_devolucion_estimada = input("Ingrese la fecha de devolución estimada(AAAA-MM-DD): ")
    fecha_devolucion_real = input("Ingrese la fecha de devolución real (AAAA-MM-DD): ")
    cursor.execute("INSERT INTO prestamos (usuario_id, libro_id, fecha_prestamo, fecha_devolucion_estimada, fecha_devolucion_real) VALUES (%s, %s, %s, %s, %s)", (usuario_id, libro_id, fecha_prestamo, fecha_devolucion_estimada, fecha_devolucion_real))
    db.commit()
    print("El prestamo ha sido generado correctamente.")

def tabla_usuarios():
    os.system("cls")
    cursor.execute("SELECT * FROM usuarios ORDER BY nombre DESC;")
    resultado = cursor.fetchall()
    
    # Definimos encabezados para la tabla
    headers = ["ID", "Nombre", "Apellido", "DNI", "Teléfono", "Email", "Creado El", "Actualizado El", "Estado"]
    
    # Ahora tenemos que formatear y mostrar los resultados en una tabla
    print(tabulate(resultado, headers=headers, tablefmt="fancy_grid", stralign="center"))
    input("\nTabla de usuarios cargada correctamente. Presione Enter para continuar...")

def tabla_libros():
    cursor.execute("SELECT * FROM libros ORDER BY autor DESC")
    resultado = cursor.fetchall()
    # Volvemos a definir el encabezado para la tabla
    headers = ["ID", "Nombre de Libro", "Autor", "Fecha de Lanzamiento", "ID de Género", "Creado El", "Actualizado El", "Estado"]
    # Volvemos a formatear y mostrar los resultados en una tabla.
    print(tabulate(resultado, headers=headers, tablefmt="fancy_grid", stralign="left"))
    input("\nTabla de libros cargada correctamente. Presione Enter para continuar...")

def tabla_generos():
    cursor.execute("SELECT * FROM generos ORDER BY genero DESC")
    resultado = cursor.fetchall()
    # Definimos el encabezado para la tabla
    headers = ["ID", "Nombre de Género"]
    print(tabulate(resultado, headers=headers, tablefmt="fancy_grid", stralign="center"))
    input("\nTabla de géneros cargada correctamente. Presione Enter para continuar...")

def tabla_prestamos():
    cursor.execute("SELECT * FROM prestamos ORDER BY fecha_prestamo DESC")
    resultado = cursor.fetchall()
    # Definimos el encabezado para la tabla
    headers = ["ID", "USUARIO ID", "LIBRO ID", "Fecha del Préstamo", "Fecha de Devolución Estimada", "Fecha de Devolución Real"]
    # Formateamos y mostramos los resultados en una tabla.
    print(tabulate(resultado, headers=headers, tablefmt="fancy_grid", stralign="center"))
    input("\nTabla de Préstamos cargada correctamente. Presione Enter para continuar...")

while True:
    #========= MENÚ INTERACTIVO ===========
    # Se ofrecen bastantes opciones al operador para poder gestionar el
    # sistema de la biblioteca.
    os.system("cls")
    print("====== GESTOR DE BIBLIOTECA ======")
    print("\nUSUARIOS:")
    print("1 - Crear usuario.")
    print("2 - Actualizar usuario.")
    print("3 - Desactivar usuario.")
    print("\nLIBROS:")
    print("4 - Agregar libro.")
    print("5 - Actualizar libro.")
    print("6 - Desactivar libro.")
    print("\nGENEROS:")
    print("7 - Añadir género.")
    print("8 - Actualizar género.")
    print("\n  PRESTAMOS:")
    print("9 - Crear prestamo.")
    print("\nTABLAS:")
    print("10 - Mostrar tabla de usuarios.")
    print("11 - Mostrar tabla de libros.")
    print("12 - Mostrar tabla de géneros de libros.")
    print("13 - Mostrar tabla de préstamos.")
    
    # Se crea una variable para recibir la respuesta del operador y
    # dependiendo de la opción se realiza un try que comprueba la validez
    # de la respuesta permitiendo así llamar a la función para realizar
    # la debida operación.
    opcion = int(input("\nElija una opción: "))
    try:
        if opcion == 1:
            crear_usuario()
            valor = input("¿Desea realizar otra operación? Responda (Si) o (No): ")
            if valor.lower() == "si":
                continue
            elif valor.lower() == "no":
                break
        elif opcion == 2:
            actualizar_usuario()
            valor = input("¿Desea realizar otra operación? Responda (Si) o (No): ")
            if valor.lower() == "si":
                continue
            elif valor.lower() == "no":
                break
        elif opcion == 3:
            desactivar_usuario()
            valor = input("¿Desea realizar otra operación? Responda (Si) o (No): ")
            if valor.lower() == "si":
                continue
            elif valor.lower() == "no":
                break
        elif opcion == 4:
            agregar_libro()
            valor = input("¿Desea realizar otra operación? Responda (Si) o (No): ")
            if valor.lower() == "si":
                continue
            elif valor.lower() == "no":
                break
        elif opcion == 5:
            actualizar_libro()
            valor = input("¿Desea realizar otra operación? Responda (Si) o (No): ")
            if valor.lower() == "si":
                continue
            elif valor.lewer() == "no":
                break
        elif opcion == 6:
            desactivar_libro()
            valor = input("¿Desea realizar otra operación? Responda (Si) o (No): ")
            if valor.lower() == "si":
                continue
            elif valor.lower() == "no":
                break
        elif opcion == 7:
            agregar_genero()
            valor = input("¿Desea realizar otra operación? Responda (Si) o (No): ")
            if valor.lower() == "si":
                continue
            elif valor.lower() == "no":
                break
        elif opcion == 8:
            actualizar_genero()
            valor = input("¿Desea realizar otra operación? Responda (Si) o (No): ")
            if valor.lower() == "si":
                continue
            elif valor.lower() == "no":
                break
        elif opcion == 9:
            crear_prestamo()
            valor = input("¿Desea realizar otra operación? Responda (Si) o (No): ")
            if valor.lower() == "si":
                continue
            elif valor.lower() == "no":
                break
        elif opcion == 10:
            tabla_usuarios()
            valor = input("¿Desea realizar otra operación? Responda (Si) o (No): ")
            if valor.lower() == "si":
                continue
            elif valor.lower() == "no":
                break
        elif opcion == 11:
            tabla_libros()
            valor = input("¿Desea realizar otra operación? Responda (Si) o (No): ")
            if valor.lower() == "si":
                continue
            elif valor.lower() == "no":
                break
        elif opcion == 12:
            tabla_generos()
            valor = input("¿Desea realizar otra operación? Responda (Si) o (No): ")
            if valor.lower() == "si":
                continue
            elif valor.lower() == "no":
                break
        elif opcion == 13:
            tabla_prestamos()
            valor = input("¿Desea realizar otra operación? Responda (Si) o (No): ")
            if valor.lower() == "si":
                continue
            elif valor.lower() == "no":
                break
        else:
            print("Opción no válida.")
            # Preguntar al usuario si desea realizar otra operación
            valor = input("¿Desea realizar otra operación? Responda (Si) o (No): ")
            if valor.lower() == "no":
                break
    
    # Se añade un except que avisa al operador que el dato ingresado no será válido.
    # A su vez ofrece la oportunidad de realizarlo nuevamente.
    except Exception as e:
        print("Ocurrió un error:", e)
        valor = input("¿Desea intentarlo de nuevo? Responda (Si) o (No): ")
        if valor.lower() == "no":
            break

# Si se sale del bucle, se cierra la conexión a la base de datos automáticamente.
# NOTA: Vi un video que es lo más recomendable ya que se puede evitar la filtración de
# datos y demás, no sé si sea lo mejor realizarlo así.
cursor.close()
db.close()