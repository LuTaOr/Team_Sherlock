import pandas as pd
import sqlite3

nombre_db = "suministros"

try:
    conexion = sqlite3.connect(nombre_db)
    error = False
except sqlite3.Error as e:
    print(e)
finally:
    if conexion and error:
        conexion.close()


cursor_db = conexion.cursor()

#Creamos la funcion
def sql_create(query):
    #crea_tabla
    cursor_db.execute(query)

#Creamos la funcion
def sql_query(query):
    #Ejecuta la query con el cursor
    cursor_db.execute(query) 

    # Almacena los datos de la query en respuesta
    respuesta = cursor_db.fetchall()

    # Obtenemos los nombres de las columnas de la tabla
    names = [description[0] for description in cursor_db.description]

    return pd.DataFrame(respuesta,columns=names)

#CREAMOS TABLAS.

#TABLA COLORES
query  = '''
CREATE TABLE IF NOT EXISTS colores (
  codigo_color INTEGER PRIMARY KEY, 
  nombre text NOT NULL
)
'''
sql_create(query)
#Insertamos valores
query  = '''
INSERT INTO colores (codigo_color,nombre)
VALUES (1,"rojo")
'''
sql_create(query)
query  = '''
INSERT INTO colores (codigo_color,nombre)
VALUES (2,"azul")
'''
sql_create(query)


#TABLA CATEGORIAS
query  = '''
CREATE TABLE IF NOT EXISTS categorias (
  codigo_categoria INTEGER PRIMARY KEY, 
  nombre text NOT NULL
)
'''
sql_create(query)
#Insertamos valores
query  = '''
INSERT INTO categorias (codigo_categoria,nombre)
VALUES (1,"piezas_plasticas")
'''
sql_create(query)
query  = '''
INSERT INTO categorias (codigo_categoria,nombre)
VALUES (2,"piezas_metálicas")
'''
sql_create(query)


#TABLA CIUDADES
query  = '''
CREATE TABLE IF NOT EXISTS ciudades (
  nombre_ciudad text PRIMARY KEY, 
  nombre_provincia text NOT NULL
)
'''
sql_create(query)
#Insertamos valores
query  = '''
INSERT INTO ciudades (nombre_ciudad,nombre_provincia)
VALUES ("Caceres","Extremadura")
'''
sql_create(query)
query  = '''
INSERT INTO ciudades (nombre_ciudad,nombre_provincia)
VALUES ("Zaragoza","Aragón")
'''
sql_create(query)


#TABLA PROVEEDORES
query  = '''
CREATE TABLE IF NOT EXISTS proveedores (
  codigo_proveedor INTEGER PRIMARY KEY, 
  nombre text NOT NULL,
  direccion text NOT NULL,
  nombre_ciudad text NOT NULL,
  FOREIGN KEY(nombre_ciudad)
    REFERENCES ciudades(nombre_ciudad)
)
'''
sql_create(query)
#Insertamos valores
query  = '''
INSERT INTO proveedores (codigo_proveedor,nombre,direccion,nombre_ciudad)
VALUES (1,"Jose García","calle mayor, 5", "Zaragoza")
'''
sql_create(query)
query  = '''
INSERT INTO proveedores (codigo_proveedor,nombre,direccion,nombre_ciudad)
VALUES (2,"Javier Fernandez","Gran Vía, 22", "Madrid")
'''
sql_create(query)


#TABLA PIEZAS
query  = '''
CREATE TABLE IF NOT EXISTS piezas (
  codigo_pieza INTEGER PRIMARY KEY, 
  nombre text NOT NULL,
  codigo_color INTEGER NOT NULL,
  precio REAL NOT NULL,
  codigo_categoria INTEGER NOT NULL,
  FOREIGN KEY(codigo_color)
    REFERENCES colores(codigo_color)
  FOREIGN KEY(codigo_categoria)
    REFERENCES categorias(codigo_categoria)
)
'''
sql_create(query)
#Insertamos valores
query  = '''
INSERT INTO piezas (codigo_pieza,nombre,codigo_color,precio,codigo_categoria)
VALUES (1,"palanca",1,23.5,2)
'''
sql_create(query)
query  = '''
INSERT INTO piezas (codigo_pieza,nombre,codigo_color,precio,codigo_categoria)
VALUES (2,"tapa",2,1.5,1)
'''
sql_create(query)


#TABLA SUMINISTROS
query  = '''
CREATE TABLE IF NOT EXISTS suministros (
  codigo_suministro INTEGER PRIMARY KEY, 
  codigo_pieza INTEGER NOT NULL,
  cantidad INTEGER NOT NULL,
  fecha DATETIME NOT NULL,
  codigo_proveedor INTEGER NOT NULL,
  FOREIGN KEY(codigo_pieza)
    REFERENCES piezas(codigo_piezas)
  FOREIGN KEY(codigo_proveedor)
    REFERENCES proveedores(codigo_proveedor)
)
'''
sql_create(query)
#Insertamos valores
query  = '''
INSERT INTO suministros (codigo_suministro,codigo_pieza,cantidad,fecha,codigo_proveedor)
VALUES (1,1,30,"2024-02-30",1)
'''
sql_create(query)
query  = '''
INSERT INTO suministros (codigo_suministro,codigo_pieza,cantidad,fecha,codigo_proveedor)
VALUES (2,2,452,"2024-05-14",2)
'''
sql_create(query)
query  = '''
INSERT INTO suministros (codigo_suministro,codigo_pieza,cantidad,fecha,codigo_proveedor)
VALUES (3,3,42,"2024-06-14",1)
'''
sql_create(query)


# COMPROBAMOS QUE SE HAN INTRODUCIDO LOS VALORES
query = '''
SELECT *
FROM colores
'''
print(sql_query(query))

query = '''
SELECT *
FROM categorias
'''
print(sql_query(query))

query = '''
SELECT *
FROM piezas
'''
print(sql_query(query))

query = '''
SELECT *
FROM suministros
'''
print(sql_query(query))

query = '''
SELECT *
FROM proveedores
'''
print(sql_query(query))

query = '''
SELECT *
FROM ciudades
'''
print(sql_query(query))


conexion.close()