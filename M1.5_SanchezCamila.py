# Librerias
import pandas as pd

# Ejercicios
# Alumna: Sanchez Parra Camila Grupo: 951
# Fecha de realizacion: 8 de Marzo del 2025
# Descripcion del problema: Para este ejercicio se creo un diccionario con los datos
# el diccionario se volvio un dataframe y se mando a llamar
def ejercicio1():
    print("         Ejercicio 1")
    datos = {
        "Mes" : ["Enero", "Febrero", "Marzo","Abril"],
        "Ventas" : [30500, 35600, 28300, 33900],
        "Gastos" : [22000, 23400, 18100, 20700]
    }

    df_data = pd.DataFrame(datos)

    return df_data



# Alumna: Sanchez Parra Camila Grupo: 951
# Fecha de realizacion: 8 de Marzo del 2025
# Descripcion del problema: Para este ejercicio se llamo al csv, siguiente se quitaron los signos europeos
# mediante el uso de sep, thousand y decimal
# se crearon variables que guardaron los datos de minimo, maximo y media de cada una de las columnas solo aquellas que cuenten con numeros
# por ende se descarta la fila nombre
# se crea un diccionario que guarde los datos y este se vuelve un DataFrame
# se pide que se regrese el valor del dataframe
def ejercicio2():
    print("         Ejercicio 2")
    df_1 = pd.read_csv("cotizacion.csv", sep=";", thousands=".", decimal=",")

    minimo = df_1.min(numeric_only=True)
    maximo = df_1.max(numeric_only=True)
    media = df_1.mean(numeric_only=True)

    dataf = {
        "Minimo" : minimo,
        "Maximo" : maximo,
        "Media" : media
    }

    data = pd.DataFrame(dataf)
    return data


# Alumna: Sanchez Parra Camila Grupo: 951
# Fecha de realizacion: 8 de Marzo del 2025
# Descripcion del problema: Para este ejercicio se llamo al df titanic se previo posibles errores en el codigo y se uso sep, thousands y decimal
# se usaron funciones como info, columns, head, tail y sample que bien hacen lo requerido para las instrucciones
def ejercicio3():
    print("         Ejercicio 3")
    df_titanic = pd.read_csv("titanic.csv", sep=";", thousands=".", decimal=",")

    print("Informacion de dataframe titanic:")
    df_titanic.info()
    print("Nombre de las columnas:\n", df_titanic.columns)
    print("\nPrimeros 10\n", df_titanic.head(10))
    print("\nUltimos 10\n", df_titanic.tail(10))
    print("\n10 Aleatorios\n", df_titanic.sample(10))


if __name__ == "__main__":
    df = ejercicio1()
    print(df, "\n")
    data = ejercicio2()
    print(data)
    ejercicio3()
