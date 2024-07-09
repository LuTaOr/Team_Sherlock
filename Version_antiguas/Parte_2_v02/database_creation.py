import pandas as pd
import sqlite3

nombre_db = "./Parte_2_v02/proveedores.db"

try:
    connection = sqlite3.connect(nombre_db) # Si no existe lo crea
    error = False
except sqlite3.Error as e:
    print(e)
finally:
    if connection and error:
        connection.close()


cursor = connection.cursor()

#Creamos la funcion
def sql_create(query):
    #crea_tabla
    cursor.execute(query)

#Creamos la funcion
def sql_query(query):
    #Ejecuta la query con el cursor
    cursor.execute(query) 

    # Almacena los datos de la query en respuesta
    respuesta = cursor.fetchall()

    # Obtenemos los nombres de las columnas de la tabla
    names = [description[0] for description in cursor.description]

    return pd.DataFrame(respuesta,columns=names)


# ############################# WARNING #############################
# Las dos funciones anteriores se pueden simplificar si simplemente utilizamos las llamadas:
# cursor.execute(query)     ó      pd.read_sql(query, connection)
# donde corresponda
# ############################# WARNING #############################

# CREAMOS TABLAS.

# ##### TABLA COLORES #####
query  = '''
  CREATE TABLE IF NOT EXISTS colores (
    color_id INTEGER PRIMARY KEY, 
    color text NOT NULL
    )
  '''
sql_create(query)

# print(pd.read_sql('SELECT * FROM colores', connection))
# cursor.execute('SELECT * FROM colores')
# cursor.fetchall()

# Insertamos valores en tabla "colores"
query  = '''
  INSERT INTO colores (color_id, color)
  VALUES (1,"rojo")
  '''
sql_create(query)
query  = '''
  INSERT INTO colores (color_id, color)
  VALUES (2,"azul")
  '''
sql_create(query)


# ##### TABLA CATEGORIAS #####
query  = '''
  CREATE TABLE IF NOT EXISTS categorias (
    categoria_id INTEGER PRIMARY KEY, 
    nombre text NOT NULL
  )
  '''
sql_create(query)

# Insertamos valores en tabla "categorias"
query  = '''
  INSERT INTO categorias (categoria_id, nombre)
  VALUES (1,"piezas_plasticas")
  '''
sql_create(query)
query  = '''
  INSERT INTO categorias (categoria_id, nombre)
  VALUES (2,"piezas_metálicas")
  '''
sql_create(query)


# ##### TABLA CIUDADES #####
query  = '''
  CREATE TABLE IF NOT EXISTS ciudades (
  ciudad text PRIMARY KEY, 
  provincia text NOT NULL
  )
  '''
sql_create(query)

# Insertamos valores en tabla "ciudades"
query  = '''
  INSERT INTO ciudades (ciudad, provincia)
  VALUES ("Caceres","Extremadura")
  '''
sql_create(query)
query  = '''
  INSERT INTO ciudades (ciudad, provincia)
  VALUES ("Zaragoza","Aragón")
  '''
sql_create(query)

# ##### TABLA PROVEEDORES #####
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
sql_create(query)

# Insertamos valores en tabla "proveedores"
query  = '''
  INSERT INTO proveedores (proveedor_id,nombre,direccion,ciudad)
  VALUES (1,"Jose García","calle mayor, 5", "Zaragoza")
  '''
sql_create(query)
query  = '''
  INSERT INTO proveedores (proveedor_id,nombre,direccion,ciudad)
  VALUES (2,"Javier Fernandez","Gran Vía, 22", "Madrid")
  '''
sql_create(query)


# ##### TABLA PIEZAS #####
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
sql_create(query)

# Insertamos valores en tabla "piezas"
query  = '''
  INSERT INTO piezas (pieza_id,nombre,color_id,precio,categoria_id)
  VALUES (1,"palanca",1,23.5,2)
  '''
sql_create(query)
query  = '''
  INSERT INTO piezas (pieza_id,nombre,color_id,precio,categoria_id)
  VALUES (2,"tapa",2,1.5,1)
  '''
sql_create(query)


# ##### TABLA SUMINISTROS #####
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
sql_create(query)

# Insertamos valores en tabla "suministros"
query  = '''
  INSERT INTO suministros (suministro_id,pieza_id,cantidad,fecha,proveedor_id)
  VALUES (1,1,30,"2024-02-30",1)
  '''
sql_create(query)
query  = '''
  INSERT INTO suministros (suministro_id,pieza_id,cantidad,fecha,proveedor_id)
  VALUES (2,2,452,"2024-05-14",2)
  '''
sql_create(query)
query  = '''
  INSERT INTO suministros (suministro_id,pieza_id,cantidad,fecha,proveedor_id)
  VALUES (3,3,42,"2024-06-14",1)
  '''
sql_create(query)

# ##### COMPROBAMOS QUE SE HAN INTRODUCIDO LOS VALORES #####
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

# ############################# WARNING #############################
# Si queremos limpiar más el código podemos hacer una FUNCIÓN, que coja todos
# los datos de un .json y los vaya introduciendo en las tablas según corresponda
#
# El siguiente código solo cargo datos en la tabla "ciudades", pero se puede 
# extrapolar a todas las demás ciudades.
# Como ejemplo por completar queda el fichero datos.py del que se puede coger más datos

datos = {
    "Getafe": "Madrid",
    "Vilareal": "Castellon"
    }

for ciudad, provincia in datos.items():
  query = f'''INSERT INTO Ciudades (ciudad, provincia)
              VALUES ("{ciudad}", "{provincia}");
              '''
  cursor.execute(query)

query = '''
SELECT *
FROM ciudades
'''

print(pd.read_sql(query, connection))

# ############################# WARNING #############################

# ############################# WARNING #############################
# No hay ningún connection.commint()
# Por tanto ninguno de los campos que hemos añadido se quedará guardado al cerrar la conexión
# ############################# WARNING #############################

connection.close()