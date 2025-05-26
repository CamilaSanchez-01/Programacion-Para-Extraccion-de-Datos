# Agrupamiento, Tablas Resumen y Transformación de Datos

#Libreria
import pandas as pd

# Datos
tabla = {
    "tienda":["A","A","A","B","B","B","C","C","C"],
    "producto":["Manzana","Platano","Naranja","Manzana","Platano","Naranja","Manzana","Platano","Naranja"],
    "categoría":["Fruta","Fruta","Fruta","Fruta","Fruta","Fruta","Fruta","Fruta","Fruta"],
    "precio":[30,20,35,25,30,45,35,20,25],
    "cantidad_vendida":[50,30,20,60,25,35,55,20,30],
    "calificacion":["A","B","C","A","B","A","C","B","A"]
}
df = pd.DataFrame(tabla)

#Ejercicio 1
# Alumna: Sanchez Parra Camila Grupo: 951
# Fecha de realizacion: 17 de Mayo del 2025
# Descripcion del problema: Se crean nuevas columnas codigo_columna y cal_numerica
# La funcion map() se usa para tranformar valores de columnas a df con pandas
df["codigo_tienda"] = df['tienda'].map({'A': 1,'B': 2, 'C': 3})
df["cal_numerica"] = df['calificacion'].map({'A': 3,'B': 2, 'C': 1})

print(df)

#Ejercicio 2
# Alumna: Sanchez Parra Camila Grupo: 951
# Fecha de realizacion: 17 de Mayo del 2025
# Descripcion del problema: Funcion de total de ventas por tienda
df['venta_total'] = df['precio'] * df['cantidad_vendida']
venta_tiendas = df.groupby('tienda')['venta_total'].sum()
print("\nTotal de Ventas por Tienda")
for tienda,total in venta_tiendas.items():
    print(f"Tienda {tienda}: {total}")


#Ejercicio 3
# Alumna: Sanchez Parra Camila Grupo: 951
# Fecha de realizacion: 17 de Mayo del 2025
# Descripcion del problema: Funcion de precio promedio por producto por tienda
precio_prom = df.groupby(['tienda','producto'])['precio'].mean()
print("\nPrecio Promedio por Producto y Tienda")
for clave in precio_prom.index:
    tienda, producto = clave
    print(f"Tienda {tienda}: Producto {producto} :{precio_prom[clave]}")


#Ejercicio 4
# Alumna: Sanchez Parra Camila Grupo: 951
# Fecha de realizacion: 17 de Mayo del 2025
# Descripcion del problema: Pivot_table() para cantidad vendida por producto y tienda
cantidades_vendida = pd.pivot_table(df, index ='producto',columns='tienda',values='cantidad_vendida',
                                    aggfunc='sum')
print("\nCantidad Vendida por Producto y Tienda")
print(cantidades_vendida)


#Ejercicio 5
# Alumna: Sanchez Parra Camila Grupo: 951
# Fecha de realizacion: 17 de Mayo del 2025
# Descripcion del problema: pivot_table() para total de ventas por tienda y producto
ventas_productos = pd.pivot_table(df, index ='producto',columns='tienda',values='venta_total',
                                    aggfunc='sum')
print("\nTotal de Ventas por Producto y Tienda")
print(ventas_productos)




