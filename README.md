
**LIBRARY MANAGER - UTN**
Alumno: Juan Manuel Vargas.
Profesor: Federico Malfasi.

# Descripción.
Este programa permite al usuario poder gestionar algunos parámetros fundamentales para la gestión de una biblioteca
mediante operaciones CRUD (create, read, update y delete). Es totalmente escalable por lo que se puede mejorar en
un futuro.

# Dependencias.
Se pueden ver en el apartado #requirements.txt

1. mysql-connector-python==9.1.0
Esta es la biblioteca que utilizo para conectar el programa a la Base de Datos MySQL, aclaro que utilizo Laragon para ello.

2. tabulate==0.9.0
Esta biblioteca nos permite ordenar nuestras tablas al momento de imprimirlas en el menú.

# Uso Básico.
Operaciones CRUD, además de un excelente menú interactivo fácil de utilizar.

# Base de Datos.
Para utilizar este proyecto correctamente, es necesario importar la base de datos que dejé en el apartado "database" en el proyecto. Seguí estos pasos para su instalación:

1. *Instala MySQL*:
   - Podes descargarlo desde [MySQL Downloads](https://dev.mysql.com/downloads/installer/).

2. *Configura la conexión de la BD*:
   - Poner a correr el servidor MySQL, anotar las credenciales de uso (`usuario`, `contraseña`, etc.).

3. *Importa el archivo SQL*:
   - Abrir tu gestor de bases de datos (En mi caso, uso HeidiSQL).
   - Crea una base de datos llamada `gestor_biblioteca`:
     ```sql
     CREATE DATABASE gestor_biblioteca;
     ```
    
   - Importa el archivo `LibraryManagerBD.sql` en esta base de datos:
     - En mi caso usé *HeidiSQL* en su versión Portable 12.1.0.6537:
       1. Selecciona la base de datos `gestor_biblioteca`.
       2. Haz clic en *Archivo* > *Ejecutar Archivo SQL...* y selecciona `LibraryManagerBD.sql`.
       3. Ejecuta el script para cargar los datos.

4. *Verificar la importación de la BD*:
   - Comprueba que la base de datos se haya importado correctamente y que todas las tablas y datos estén presentes.

Con estos pasos la importación debe ser exitosa y debería funcionar correctamente la base de datos en el proyecto.

NOTA: El programa ya crea las tablas automáticamente.
