# libreria
import pandas as pd

# Ejercicios
# Alumna: Sanchez Parra Camila Grupo: 951
# Fecha de realizacion: 14 de Abril del 2025
# Descripcion del problema: Crear tres funciones que realicen pruebas de estadistica como lo es el min_max de columnas,
# Z-score y escalado simple, cada funcion sirve con un for para que pase por las columnas del df elegido, y creara
# columnas nuevas con la informacion nueva de cada funcion.

# x = (x1 - min) / (max - min)
def min_max(df, columnas):
    for col in columnas:
        max_valor = df[col].max()
        min_valor = df[col].min()
        df[f"min_max_{col}"] = (df[col] - min_valor) / (max_valor - min_valor)
    print(df)
    return df

# x = (xi - promedio) / std
def z_score(df, columnas):
    for col in columnas:
        prom = df[col].mean()
        dv = df[col].std()
        df[f"z_score_{col}"] = (df[col] - prom) / dv
    print(df)
    return df

def escalado_simple(df, columnas):
    for col in columnas:
        max_valor = df[col].max()
        df[f"escalado_simple_{col}"] = df[col] / max_valor
    print(df)
    return df

if __name__ == "__main__":
    d = {
        "nombre": ["Viridiana", "Ana", "Pablo", "Jackeline", "Jose", "Juan", "Manuel"],
        "edad": [20, 18, 20, 22, 20, 22, 32],
        "promedio": [76, 96, 96, 84, 85, 78, 65],
        "semestre": [4, 1, 5, 4, 2, 7, 2]
    }
    df = pd.DataFrame(d)
    columnas = ["edad", "promedio", "semestre"]
    print("****** MIN-MAX *******")
    min_max(df, columnas)
    print("****** Z-SCORE *******")
    z_score(df, columnas)
    print("****** ESCALADO SIMPLE *******")
    escalado_simple(df, columnas)