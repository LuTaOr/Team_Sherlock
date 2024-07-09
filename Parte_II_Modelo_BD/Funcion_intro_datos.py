import pandas as pd
import sqlite3

def intro_datos(tabla, ruta, cursor, sep = ";"):


    df_csv = pd.read_csv(ruta, sep=";") # convierte el csv en un DataFrame
    lista_dict = list(df_csv.keys()) # saca la info de los nombres de las columnas pasandolas a una lista
    df_csv.set_index(lista_dict, inplace = True) # quitamos el indice implicito y dejamos solo las columnas, no hay columna indice
    columnas = tuple(df_csv.index.names) # pasa a tupla los nombres de las columnas para poder ser usado directamente en la query

    for i in range(0,len(df_csv.index)):  # recorre el bucle tantas veces como filas haya que introducir  
        
        query = f'''INSERT INTO {tabla} {columnas}
                    VALUES {df_csv.index[i]}'''
        
        cursor.execute(query)


# ruta = "./CSVs_para_migrar_a_BD/ciudades.csv" # sera uno de los argumentos de la funcion
# tabla = "ciudades" # sera uno de los argumentos de la funcion

# intro_datos (tabla, ruta)