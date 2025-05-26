#Libreria
from mysql.connector import connect, Error

# Ejercicio 1
class MySQLConnect:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password =  password
        self.database =  database

    def conectar(self):
        try:
            dbConexion = connect(
                host= self.host,
                user = self.user,
                password = self.password,
                database = self.database
            )
            print("Conexion Establecida")
            return dbConexion
        except Error as e:
            print(e)
            return False

    def desconectar(self, dbConexion):
        if dbConexion:
            dbConexion.close()
            print("Conexion Cerrada")

# Ejercicio 2
class PaisMySQL(MySQLConnect):
    def __init__(self, host, user, password, database):
        super().__init__(host, user, password, database)

    def insertar(self, dbConexion, nombre):
        try:
            cursor = dbConexion.cursor()
            sql = "SELECT * FROM pais WHERE nombre = %s"
            valores = (nombre,)
            cursor.execute(sql, valores)
            v = cursor.fetchall()

            if v:
                print(f"Ya existe ese nombre {v}")
            else:
                cursor = dbConexion.cursor()
                sql = "INSERT INTO PAIS(nombre) VALUES(%s)"
                valores = (nombre, )
                cursor.execute(sql, valores)
                dbConexion.commit()
                print("Pais insertado correctamente")
                cursor.close()
                return True

        except Error as e:
            print(e)
            return False

    def editar(self,dbConexion, id, new_nombre):
        try:
            cursor = dbConexion.cursor()
            sql = "SELECT * FROM pais WHERE nombre = %s"
            valores = (new_nombre,)
            cursor.execute(sql, valores)
            v = cursor.fetchall()
            dbConexion.commit()
            cursor.close()

            if v:
                print(f"Ya existe ese nombre {v}")
            else:
                cursor = dbConexion.cursor()
                sql = "UPDATE pais SET nombre = %s WHERE id = %s"
                valores = (new_nombre, id)
                cursor.execute(sql, valores)
                dbConexion.commit()
                print("Pais actualizado correctamente")
                cursor.close()
                return True
        except Error as e:
            print(e)
            return False

    def eliminar(self, dbConexion, id):
        try:
            cursor = dbConexion.cursor()
            sql = "SELECT * FROM pais WHERE id = %s"
            valores = (id,)
            cursor.execute(sql, valores)
            v = cursor.fetchall()
            dbConexion.commit()
            cursor.close()

            if v:
                cursor = dbConexion.cursor()
                sql = "Delete FROM pais WHERE id = %s"
                valores = (id,)
                cursor.execute(sql, valores)
                dbConexion.commit()
                print(f"Pais {valores} Eliminado correctamente")
                cursor.close()
                return True
            else:
                print(f"Ya existe ese nombre {v}")

        except Error as e:
            print(e)
            return False

    def consultar(self, dbConexion, f):
        try:
            cursor = dbConexion.cursor()
            sql = f"SELECT * FROM pais WHERE {f}"
            cursor.execute(sql)
            results = cursor.fetchall()
            dbConexion.commit()
            cursor.close()
            return results
        except Error as e:
            print(e)
            return False

# Ejercicio 3
class OlimpiadaMySQL(MySQLConnect):
    def __init__(self, host, user, password, database):
        super().__init__(host, user, password, database)

    def insertar(self, dbConexion, y_olimpiada):
        try:
            cursor = dbConexion.cursor()
            sql = "SELECT * FROM olimpiada WHERE year_olimpiada = %s"
            valores = (y_olimpiada,)
            cursor.execute(sql, valores)
            v = cursor.fetchall()

            if v:
                print(f"Ya existe ese year_olimpiada {v}")
            else:
                cursor = dbConexion.cursor()
                sql = "INSERT INTO olimpiada(year_olimpiada) VALUES(%s)"
                valores = (y_olimpiada,)
                cursor.execute(sql, valores)
                dbConexion.commit()
                print("year_olimpiada insertado correctamente")
                cursor.close()
                return True

        except Error as e:
            print(e)
            return False

    def editar(self, dbConexion, id, new_n):
        try:
            cursor =dbConexion.cursor()
            sql = "SELECT * FROM olimpiada WHERE id = %s"
            valores = (id,)
            cursor.execute(sql, valores)
            v = cursor.fetchall()
            dbConexion.commit()
            cursor.close()

            if v:
                cursor = dbConexion.cursor()
                sql = "UPDATE olimpiada SET year_olimpiada = %s WHERE id = %s"
                valores = (new_n, id)
                cursor.execute(sql, valores)
                dbConexion.commit()
                print("Año actualizado correctamente")
                cursor.close()
            else:
                print(f"No existe ese year_olimpiada {v}")
        except Error as e:
            print(e)
            return False

    def eliminar(self, dbConexion, year_olimpiada):
        try:
            cursor = dbConexion.cursor()
            sql = "SELECT * FROM olimpiada WHERE year_olimpiada = %s"
            valores = (year_olimpiada,)
            cursor.execute(sql, valores)
            v = cursor.fetchall()
            dbConexion.commit()
            cursor.close()

            if v:
                cursor = dbConexion.cursor()
                sql = "Delete FROM olimpiada WHERE year_olimpiada = %s"
                valores = (year_olimpiada,)
                cursor.execute(sql, valores)
                dbConexion.commit()
                print(f"Año {valores} Eliminado correctamente")
                cursor.close()
                return True
            else:
                print(f"Ese Año {v} no existe")

        except Error as e:
            print(e)
            return False

    def consultar(self,dbConexion, f):
        try:
            cursor = dbConexion.cursor()
            sql = f"SELECT * FROM olimpiada WHERE {f}"
            cursor.execute(sql)
            results = cursor.fetchall()
            print(results)
            dbConexion.commit()
            cursor.close()
            return results
        except Error as e:
            print(e)
            return False


# Ejercicio 4
class ResultadosMySQL(MySQLConnect):
    def __init__(self, host, user, password, database):
        super().__init__(host, user, password, database)

    def insertar(self,dbConexion, idOlimpiada, idPais, idGenero, oro, plata, bronce):
        try:
            cursor = dbConexion.cursor()
            sql = "INSERT INTO resultados(idOlimpiada, idPais, idGenero, oro, plata, bronce) VALUES(%s,%s,%s,%s,%s,%s)"
            valores = (idOlimpiada, idPais, idGenero, oro, plata, bronce,)
            cursor.execute(sql, valores)
            dbConexion.commit()
            print("Datos insertados correctamente")
            cursor.close()
            return True

        except Error as e:
            print(e)
            return False

    def editar(self, dbConexion, idOlimpiada, idPais, idGenero, oro, plata, bronce):
        try:
            cursor = dbConexion.cursor()
            sql = "SELECT * FROM resultados WHERE idOlimpiada = %s and idPais = %s and idGenero = %s"
            valores = (idOlimpiada, idPais, idGenero)
            cursor.execute(sql, valores)
            v = cursor.fetchall()
            dbConexion.commit()
            cursor.close()

            if v:
                if oro >0 and plata >0 and  bronce>0:
                    cursor = dbConexion.cursor()
                    sql = "UPDATE resultados SET oro = %s, plata = %s, bronce = %s WHERE idOlimpiada = %s and idPais = %s and idGenero = %s"
                    valores = (oro, plata, bronce, idOlimpiada, idPais, idGenero)
                    cursor.execute(sql, valores)
                    dbConexion.commit()
                    print("Datos actualizados correctamente")
                    cursor.close()
                    return True
                print(f"Los datos deben ser numeros positivos")
            else:
                print("No existen datos")

        except Error as e:
            print(e)
            return False

    def eliminar(self, dbConexion, idOlimpiada, idPais, idGenero):
        try:
            cursor = dbConexion.cursor()
            sql = "SELECT * FROM resultados WHERE idOlimpiada = %s and idPais = %s and idGenero = %s"
            valores = (idOlimpiada, idPais, idGenero)
            cursor.execute(sql, valores)
            v = cursor.fetchall()
            dbConexion.commit()
            cursor.close()

            if v:
                cursor = dbConexion.cursor()
                sql = "Delete FROM resultados WHERE idOlimpiada = %s and idPais = %s and idGenero = %s"
                valores = (idOlimpiada, idPais, idGenero)
                cursor.execute(sql, valores)
                dbConexion.commit()
                print(f"Datos con {valores} Eliminado correctamente")
                cursor.close()
                return True
            else:
                print(f"Esos datos no existen")

        except Error as e:
            print(e)
            return False

    def consultar(self, dbConexion, idOlimpiada, idPais, idGenero):
        try:
            cursor = dbConexion.cursor()
            sql = f"SELECT * FROM resultados WHERE idOlimpiada = %s and idPais = %s and idGenero = %s"
            valores = (idOlimpiada, idPais, idGenero)
            cursor.execute(sql, valores)
            results = cursor.fetchall()
            print(results)
            dbConexion.commit()
            cursor.close()
            return results
        except Error as e:
            print(e)
            return False


#Se crea el menu
if __name__== "__main__":
    # pais
    pais = PaisMySQL("localhost", "root","123456789", "olimpiadas")
    conexion = pais.conectar()
    pais.insertar(conexion, "Mexico")
    pais.insertar(conexion, "Suiza")
    pais.editar(conexion, 1,"Colombia")
    pais.eliminar(conexion, 2)
    pais.consultar(conexion, "nombre = Colombia")
    pais.consultar(conexion, "id = 1")
    pais.desconectar(conexion)

    # olimpiada
    olimpiada = OlimpiadaMySQL("localhost", "root","123456789", "olimpiadas")
    conexion = olimpiada.conectar()
    olimpiada.insertar(conexion, 2004)
    olimpiada.insertar(conexion, 2000)
    olimpiada.editar(conexion, 1,2005)
    olimpiada.eliminar(conexion, 2000)
    olimpiada.consultar(conexion, "id = 1")
    olimpiada.desconectar(conexion)

    # resultados
    resultados = ResultadosMySQL("localhost", "root","123456789", "olimpiadas")
    conexion = resultados.conectar()
    resultados.insertar(conexion, 1, 14, 23, 12, 67, 3.4)
    resultados.insertar(conexion, 2, 13, 33, -12, 7, 7)
    resultados.editar(conexion, 2, 17, 32, 13, 7, 7)
    resultados.eliminar(conexion, 3, 15, 36)
    resultados.consultar(conexion, 1, 14, 23)
    resultados.desconectar(conexion)
