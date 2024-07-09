# Ejemplo de cómo se podrían introducir los datos en la BD en un 
# diccionario de diccionario
#
# OJO: Es una propuesta y los valores no tienen porque estar en el orden
# correcto para que se interprete en el main.py

datos_2 = {
   "ciudades" : {"ciudad" : ("Getafe", "Vilareal", "Lugo", "Madrid", "Cadiz", "Calatayud"), 
                 "provincia" : ("Castellon, Madrid","Lugo","Madrid","Cadiz","Zaragoza")},
   "proveedores" :{"proveedir_id":(3,34,23,67,6,90), 
                   "nombre":("Grupale","Herraca","Maquinas Navarro","Reparmur","Excavaciones Tomas","Servired"),
                   "direccion":("Buenavista 3","Malavista 4","Rio Ebro 4","Hermanos Martinez 56","Molino 34","Desesperacion 67"),
                   "ciudad" : ("Getafe", "Vilareal", "Lugo", "Madrid", "Cadiz", "Calatayud")
                   },
   "suministros" : {"suministro_id":(1,16,24,41,78,96),
                   "pieza_id":(452,74,895,12,4,89),
                   }}

for columna in datos_2.keys():
    variable1 = variable2
    variable2 = variable3
    variable3 = columna


}

datos_2 = {"ciudades"}


datos = {
  'ciudades' : {'Getafe':'madrid',
                'Vilareal' : 'Castellon'
                },
  'colores' : {000 : 'Negro',
               100 : 'Blanco',
               50 : 'Rojo',
               158 : 'Azul'
               },
  'suministros' : {1 : (1, 30, '2024-02-30', 3),
                   2 : (30, 40, '2022-12-05', 23),
                   3 : (122, 5, '2023-04-13', 44)
                   }
  }

def intro_datos (diccionario):
  for tabla in diccionario.keys():
    valores = diccionario[tabla]
    for columna_1 in valores.keys():
      columna_siguiente = valores[columna_1]
      if type(list(valores.values())[0]) is str:

        query = f'''INSERT INTO {tabla} (ciudad, provincia)
                  #VALUES ("{columna_1}", "{columna_siguiente}");'''

      else:
        numero_columnas = (len(list(valores.values())[0])) 

        if numero_columnas == 3:
            columna_restante_1 = columna_siguiente[1]
            columna_restante_2 = columna_siguiente[2]

            query = f'''INSERT INTO {tabla} (ciudad, provincia)
                  VALUES ("{columna_1}", "{columna_restante_1}", "{columna_restante_2}");'''

        elif numero_columnas == 4:
              columna_restante_1 = columna_siguiente[1]
              columna_restante_2 = columna_siguiente[2]
              columna_restante_3 = columna_siguiente[3]

              query = f'''INSERT INTO {tabla} (ciudad, provincia)
                  VALUES ("{columna_1}", "{columna_restante_1}", "{columna_restante_2}", "{columna_restante_3}");'''

        elif numero_columnas == 5:
              columna_restante_1 = columna_siguiente[1]
              columna_restante_2 = columna_siguiente[2]
              columna_restante_3 = columna_siguiente[3]
              columna_restante_4 = columna_siguiente[4]

              query = f'''INSERT INTO {tabla} (ciudad, provincia)
                  VALUES ("{columna_1}", "{columna_restante_1}", "{columna_restante_2}", "{columna_restante_3}" ,"{columna_restante_4}");'''