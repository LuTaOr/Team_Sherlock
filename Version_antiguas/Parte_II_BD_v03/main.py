import pandas as pd
import sqlite3

# Importante seleccionar la ruta
nombre_db = "./Parte_2_v03/proveedores.db"

try:
    connection = sqlite3.connect(nombre_db) # Si no existe lo crea
    error = False
except sqlite3.Error as e:
    print(e)
finally:
    if connection and error:
        connection.close()

cursor = connection.cursor()

# ############### CREAMOS TABLAS ###############

# TABLA COLORES
query  = '''
  CREATE TABLE IF NOT EXISTS colores (
    color_id INTEGER PRIMARY KEY, 
    color text NOT NULL
    )
  '''
cursor.execute(query)

# TABLA CATEGORIAS
query  = '''
  CREATE TABLE IF NOT EXISTS categorias (
    categoria_id INTEGER PRIMARY KEY, 
    nombre text NOT NULL
  )
  '''
cursor.execute(query)

# TABLA CIUDADES
query  = '''
  CREATE TABLE IF NOT EXISTS ciudades (
  ciudad text PRIMARY KEY, 
  provincia text NOT NULL
  )
  '''
cursor.execute(query)

# TABLA PROVEEDORES
query  = '''
  CREATE TABLE IF NOT EXISTS proveedores (
    proveedor_id INTEGER PRIMARY KEY, 
    nombre text NOT NULL,
    direccion text NOT NULL,
    ciudad text NOT NULL,
    
    FOREIGN KEY(ciudad)
    REFERENCES ciudades(ciudad)
    )
  '''
cursor.execute(query)

# TABLA PIEZAS
query  = '''
  CREATE TABLE IF NOT EXISTS piezas (
    pieza_id INTEGER PRIMARY KEY, 
    nombre text NOT NULL,
    color_id INTEGER NOT NULL,
    precio REAL NOT NULL,
    categoria_id INTEGER NOT NULL,
    
    FOREIGN KEY(color_id)
    REFERENCES colores(color_id)
    FOREIGN KEY(categoria_id)
    REFERENCES categorias(categoria_id)
    )
  '''
cursor.execute(query)

# TABLA SUMINISTROS
query  = '''
  CREATE TABLE IF NOT EXISTS suministros (
    suministro_id INTEGER PRIMARY KEY, 
    pieza_id INTEGER NOT NULL,
    proveedor_id INTEGER NOT NULL,    
    cantidad INTEGER NOT NULL,
    fecha DATETIME NOT NULL,
    
    FOREIGN KEY(pieza_id)
    REFERENCES piezas(pieza_ids)
    FOREIGN KEY(proveedor_id)
    REFERENCES proveedores(proveedor_id)
    )
  '''
cursor.execute(query)

# Pruebas
#
# print('######################')
# # EJECTUTAR LA CONSULTA PARA SABER LOS NOMBRES DE LAS TABLAS
# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
# print(cursor.fetchall())
# print('######################')

# query = '''
#   SELECT *
#   FROM *
#   '''
# print(pd.read_sql(query, connection))

# print('######################')


# ############### INSERTAR VALORES ###############

# Insertamos valores en tabla "colores"
query  = '''
  INSERT INTO colores (color_id, color)
  VALUES (1,"rojo")
  '''
cursor.execute(query)

query  = '''
  INSERT INTO colores (color_id, color)
  VALUES (2,"azul")
  '''
cursor.execute(query)

# Insertamos valores en tabla "categorias"
query  = '''
  INSERT INTO categorias (categoria_id, nombre)
  VALUES (1,"piezas_plasticas")
  '''
cursor.execute(query)

query  = '''
  INSERT INTO categorias (categoria_id, nombre)
  VALUES (2,"piezas_metálicas")
  '''
cursor.execute(query)


# Insertamos valores en tabla "ciudades"
query  = '''
  INSERT INTO ciudades (ciudad, provincia)
  VALUES ("Caceres","Extremadura")
  '''
cursor.execute(query)

query  = '''
  INSERT INTO ciudades (ciudad, provincia)
  VALUES ("Zaragoza","Aragón")
  '''
cursor.execute(query)

# Insertamos valores en tabla "proveedores"
query  = '''
  INSERT INTO proveedores (proveedor_id,nombre,direccion,ciudad)
  VALUES (1,"Jose García","calle mayor, 5", "Zaragoza")
  '''
cursor.execute(query)

query  = '''
  INSERT INTO proveedores (proveedor_id,nombre,direccion,ciudad)
  VALUES (2,"Javier Fernandez","Gran Vía, 22", "Madrid")
  '''
cursor.execute(query)

# Insertamos valores en tabla "piezas"
query  = '''
  INSERT INTO piezas (pieza_id,nombre,color_id,precio,categoria_id)
  VALUES (1,"palanca",1,23.5,2)
  '''
cursor.execute(query)

query  = '''
  INSERT INTO piezas (pieza_id,nombre,color_id,precio,categoria_id)
  VALUES (2,"tapa",2,1.5,1)
  '''
cursor.execute(query)

# Insertamos valores en tabla "suministros"
query  = '''
  INSERT INTO suministros (suministro_id,pieza_id,cantidad,fecha,proveedor_id)
  VALUES (1,1,30,"2024-02-30",1)
  '''
cursor.execute(query)

query  = '''
  INSERT INTO suministros (suministro_id,pieza_id,cantidad,fecha,proveedor_id)
  VALUES (2,2,452,"2024-05-14",2)
  '''
cursor.execute(query)

query  = '''
  INSERT INTO suministros (suministro_id,pieza_id,cantidad,fecha,proveedor_id)
  VALUES (3,3,42,"2024-06-14",1)
  '''
cursor.execute(query)


# #################### COMPROBAMOS QUE SE HAN INTRODUCIDO LOS VALORES ####################
query = '''
  SELECT *
  FROM colores
  '''
print(pd.read_sql(query, connection))

query = '''
  SELECT *
  FROM categorias
  '''
print(pd.read_sql(query, connection))

query = '''
  SELECT *
  FROM piezas
  '''
print(pd.read_sql(query, connection))

query = '''
  SELECT *
  FROM suministros
  '''
print(pd.read_sql(query, connection))

query = '''
  SELECT *
  FROM proveedores
  '''
print(pd.read_sql(query, connection))

query = '''
  SELECT *
  FROM ciudades
  '''
print(pd.read_sql(query, connection))

# ############################# WARNING #############################
#
# Si queremos limpiar más el código podemos hacer una FUNCIÓN, que coja todos
# los datos de un .json y los vaya introduciendo en las tablas según corresponda
#
# El siguiente código solo cargo datos en la tabla "ciudades", pero se puede 
# extrapolar a todas las demás tablas de la BD.
# Como ejemplo por completar queda el fichero datos.py del que se pueden coger más datos

# datos = {
#     "Getafe": "Madrid",
#     "Vilareal": "Castellon"
#     }

# for ciudad, provincia in datos.items():
#   query = f'''INSERT INTO Ciudades (ciudad, provincia)
#               VALUES ("{ciudad}", "{provincia}");
#               '''
#   cursor.execute(query)

# query = '''
# SELECT *
# FROM ciudades
# '''

# print(pd.read_sql(query, connection))
#
# ############################# WARNING #############################



# ############################# WARNING #############################
#
# No hay ningún connection.commit()
# Por tanto ninguno de los campos que hemos añadido se quedará guardado al cerrar la conexión
#
# ############################# WARNING #############################



connection.close()