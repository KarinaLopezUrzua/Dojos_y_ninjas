from tarea11.config.mysqlconnection import conectarMySQL

class Ninjas:
    def __init__(self, data): #en cada uno de los atributos de objetos estamos almacenando el valor de la clave de ese diccionario que obtenemos de la bd de nuestra tabla 
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.edad = data["edad"]
        self.created_at = data["created_at"]
        self.update_at = data["update_at"]
        self.dojo_id = data["dojo_id"]

    @classmethod
    def nuevo_ninja(cls, data):
        query = "INSERT INTO ninjas (nombre, apellido, edad, dojo_id) VALUES(%(nombre)s, %(apellido)s, %(edad)s,  %(ubicacion)s);"  #values tiene el nombre igual al nombre que hemos puesto en el input en el html
        return conectarMySQL("dojosyusuarios_schema1").query_db(query,data)

#obtener un ninja
    @classmethod
    def obtener_un_ninja(cls, data):
        query = "SELECT * FROM ninjas WHERE id=%(id)s;"
        result = conectarMySQL("dojosyusuarios_schema1").query_db(query,data) 
        return cls(result[0]) #como el id es unico, solo debemos recibir un valor, es decir una lista de UN diccionario, y lo retornamos como un objeto asi [0]

