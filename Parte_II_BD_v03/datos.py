# Ejemplo de cómo se podrían introducir los datos en la BD en un 
# diccionario de diccionario
#
# OJO: Es una propuesta y los valores no tienen porque estar en el orden
# correcto para que se interprete en el main.py

datos = {
  'ciudades' : {'Getafe':'madrid',
                'Vilareal' : 'Castellon'
                },
  'colores' : {000 : 'Negro',
               100 : 'Blanco',
               050 : 'Rojo',
               158 : 'Azul'
               },
  'suministros' : {1 : (1, 30, '2024-02-30', 3),
                   2 : (30, 40, '2022-12-05', 23),
                   3 : (122, 5, '2023-04-13', 44)
                   }
  }