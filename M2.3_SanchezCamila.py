# libreria
import pandas as pd
import numpy as np

# Alumna: Sanchez Parra Camila Grupo: 951
# Fecha de realizacion: 10 de abril del 2025
# Descripcion del problema: Crear un dataframe para que sea el parametro
def crear():
    d = {
        "nombre": ["Viridiana", "Ana", "Viridiana", "Jackeline", "Jose",
                   "Juan", "Manuel"],
        "edad": [20, 18, 20, 22, 20, None, 32],
        "promedio": [None, 96, None, 84, None, 78, 65],
        "semestre": [None, 1, None, 4, 2, None, None]
    }
    df = pd.DataFrame(d)
    return df

# Alumna: Sanchez Parra Camila Grupo: 951
# Fecha de realizacion: 10 de abril del 2025
# Descripcion del problema: crear una funcion que nos regrese el porcentaje nulo de cada columna
def porcentajesNulos(df:pd.DataFrame):
    print("*********** NULOS ***********")
    nulosdf = df.isna().sum() / len(df)
    nuloscolumn = df.isna().sum()
    totnulos = df.isna().sum().sum()
    print(f"Columnas Nulos:\n{nulosdf}")
    print(f"\nNulos por columnas:\n{nuloscolumn}")
    print(f"\nNulos totales:\n{totnulos}")

# Alumna: Sanchez Parra Camila Grupo: 951
# Fecha de realizacion: 10 de abril del 2025
# Descripcion del problema: crear funcion que retorne los renglones duplicados
def renglonesDuplicados(df:pd.DataFrame):
    print("\n*********** DUPLICADOS ***********")
    dup = df.duplicated().sum()
    print(f"Renglones duplicados: \n {dup}")

# Alumna: Sanchez Parra Camila Grupo: 951
# Fecha de realizacion: 10 de abril del 2025
# # Descripcion del problema: Funcion que nos de el porcentaje maximo y
# eliminar columnas que superen o igual el porcentaje de calores nulos
def columElimindas(df:pd.DataFrame):
    print("\n*********** ELIMINAR COLUMNAS MAXIMAS ***********")
    new_df = df
    max_column = []
    for col in new_df:
        porcentaje = df[col].isna().mean()
        if 0 < porcentaje <= 1:
            max_column.append(col)
    if max_column:
        new_df = new_df.drop(columns=max_column)
        print(f"DataFrame modificado: \n{new_df}\n"
              f"Y columnas eliminadas son: {max_column}")
    else:
        print("No hay columnas que cumplan con el maximo de % nulo")
    return new_df

# Alumna: Sanchez Parra Camila Grupo: 951
# Fecha de realizacion: 10 de abril del 2025
# Descripcion del problema:Modificar el dataframe usando metodos mean, bfill, ffill
def modificacion(df:pd.DataFrame, metodo, columnas):
    print("\n*********** MODIFICAION ***********")
    met = ['mean','bfill','ffill']
    if metodo not in met:
        print("El metodo no esta disponible")
    new_df = df

    for col in columnas:
        if col not in df.columns:
            print(f"Columna {col} no existe")
    for col in columnas:
        if col in columnas:
            if metodo == 'mean':
                new_df[col] = new_df[col].fillna(new_df[col].mean())
            elif metodo == 'bfill':
                new_df[col] = new_df[col].fillna(method="bfill")
            elif metodo == 'ffill':
                new_df[col] = new_df[col].fillna(method="ffill")
    print(f"DataFrame modificado: \n\n{new_df}")
    return new_df

# Alumna: Sanchez Parra Camila Grupo: 951
# Fecha de realizacion: 10 de abril del 2025
# Descripcion del problema:Eliminar renglones duplicados dentro del dataframe
def cantidadEliminados(df:pd.DataFrame):
    print("\n*********** ELIMINAR RENGLONES ***********")
    dup_2 = df.duplicated().sum()
    print(f"Los renglones duplicados y eliminados son: {dup_2}\n")
    if dup_2 >0:
        df.drop_duplicates(inplace=True)
        print(f"DataFrame limpio: \n{df}")

if __name__ == "__main__":
    df = crear()
    porcentajesNulos(df)
    renglonesDuplicados(df)
    columElimindas(df)
    metodo = 'mean'
    columnas = ['edad','promedio','semestre']
    new_df = modificacion(df, metodo, columnas)
    cantidadEliminados(df)