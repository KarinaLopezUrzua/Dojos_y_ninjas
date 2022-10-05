from unittest import result
from tarea11.config.mysqlconnection import conectarMySQL

class Dojos:
    def __init__(self, data): #en cada uno de los atributos de objetos estamos almacenando el valor de la clave de ese diccionario que obtenemos de la bd de nuestra tabla 
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.created_at = data["created_at"]
        self.update_at = data["update_at"] 

    @classmethod #métodos de clase para leer bd
    def obtener_todo(cls):
        query = "SELECT * FROM dojos;" #nombre tabla de bd
        results = conectarMySQL('dojosyusuarios_schema1').query_db(query) #result serian un diccionario en donde conectamos con la bd y llama a la función conectarMySQL
        dojos_instancias = []   # creamos una lista vacía para agregar nuestras instancias de dojos
        for diccionario in results: # Iterar sobre los resultados de la bd y crear instancias con cls
            dojos_instancias.append(cls(diccionario)) #convertimos una lista de diccionarios en una lista de objetos
        return dojos_instancias #retornamos una lista de objetos

    @classmethod
    def nuevo_dojo(cls, data):
        query = "INSERT INTO dojos (nombre) VALUES(%(nombre)s);" #nombre de la llave del diccionario en la ruta
        return conectarMySQL("dojosyusuarios_schema1").query_db(query,data) 

    @classmethod #metodo leer
    def obtener_un_dojo(cls,data):
        query = "SELECT * FROM dojos WHERE id=%(id)s;" #id nombre del diccionario en ruta /dojos/<int:id_dojo>")
        result = conectarMySQL("dojosyusuarios_schema1").query_db(query,data) 
        return cls(result[0]) #como el id es unico, solo debemos recibir un valor, es decir una lista de UN diccionario, y lo retornamos como un objeto asi [0]

    #JOIN consulta para obtener los ninjas con el id del dojo 
    @classmethod
    def obtener_ninja_con_dojo(cls, data): #data serian los datos que estamos pasando en ruta /dojos
        query = "SELECT * FROM ninjas JOIN dojos ON ninjas.dojo_id=dojos.id WHERE dojos.id=%(id)s;" #toma el nombre id pq asi se llama el diccinario que creamos en ruta /dojos
        result = conectarMySQL("dojosyusuarios_schema1").query_db(query,data) 
        return result