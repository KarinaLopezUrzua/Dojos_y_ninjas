from tarea11 import app
from flask import render_template, redirect, session, request 
from tarea11.modelos.clases_ninja import Ninjas
from tarea11.modelos.clases_dojo import Dojos #importamos dojos para pder usarlo en ninjas.html


#RUTAS FORMULARIO READ

@app.route("/ninja") #ruta formulario
def ninja():
    todos_dojos = Dojos.obtener_todo()
    return render_template("ninjas.html", lista_dojos=todos_dojos) #podemos usar la informacion obtenida de dojos

""" REVISAR UBICACION
@app.route("/crear_ninja", methods=["POST"]) 
def crear_ninja():
    datos = {
        "nombre":request.form["nombre"],
        "apellido":request.form["apellido"],
        "edad":request.form["edad"],
        "dojo_id":request.form["ubicacion"],
    }
    id_ninja = Ninjas.nuevo_ninja(datos)
    session["id_ninja"] = id_ninja
    return ("/") #Pagina inicio se dirige a html hijo
"""

@app.route("/crear_ninja", methods=["POST"]) 
def crear_ninja():
    #print(request.form, "ACA ESTA EL DICCIONARIO") ESTA LINEA NOS AYUDA A IDENTIFICAR EL NOMBRE DE LA CLAVE DEL DICCIONARIO
    id_ninja = Ninjas.nuevo_ninja(request.form) #lo guardamos en el id_ninja que es lo que nos retorna
    datos = {
        "id":id_ninja
    }
    un_ninja = Ninjas.obtener_un_ninja(datos) #enviamos el id del ninja que esta en un diccionario
    return redirect(f"/dojos/{un_ninja.dojo_id}") #ocupamos format para concatenar la variable con el dojo_id

@app.errorhandler(404)
def pagina_no_encontrada():
    return  'ESTA RUTA NO FUE ENCONTRADA', 404 