###################################

>> Fecha: 2024-07-05
>> Autores: Juanma, Luis, Carlos, Lander

###################################

>> Link a la web para crear ERD:
>> DBDiagram.io

###################################

>> Tablas de la BD implementada:
>> https://dbdiagram.io/d/Team_Sherlock_BD_2-6687b8609939893dae20f954

###################################

>> CÓDIGO fuente para dibujar el ERD (en caso de no tener permiso de edición en el link anterior):

// Use DBML to define your database structure
// Docs: https://dbml.dbdiagram.io/docs

Table suministros {
  suministro_id int [primary key]
  pieza_id int
  proveedor_id int
  cantidad int
  fecha timestamp
}

Table proveedores {
  proveedor_id int [primary key]
  nombre char
  direccion char
  cuidad char
}

Table ciudades {
  ciudad char [primary key]
  provincia char
}

Table piezas {
  pieza_id int [primary key]
  nombre char
  color_id int
  precio float
  categoria_id int
}

Table categorias {
  categoria_id int [primary key]
  nombre char
}

Table colores {
  color_id int [primary key]
  color char
}

Ref: proveedores.proveedor_id < suministros.proveedor_id // one-to-many
Ref: categorias.categoria_id < piezas.categoria_id
Ref: suministros.pieza_id > piezas.pieza_id
Ref: proveedores.cuidad > ciudades.ciudad
Ref: piezas.color_id > colores.color_id