from tarea11 import app
from flask import render_template, redirect, session, request 
from tarea11.modelos.clases_dojo import Dojos

#RUTAS FORMULARIO READ Y ACTUALIZAR LISTA

@app.route("/") 
def raiz():
    return redirect("/dojos") #pidieron que redigiera a dojos

@app.route("/dojos") 
def formulario():
    todos_dojos = Dojos.obtener_todo()
    return render_template("dojos.html", lista_dojos=todos_dojos) #Pagina inicio se dirige a html hijo

#RUTA CREAR
@app.route("/crear_dojo", methods=["POST"]) #ruta formulario
def crear_dojo():
    datos = {
        "nombre":request.form["nombre"],
    }
    id_dojo = Dojos.nuevo_dojo(datos) #no coloca id_dojo=
    session["id_dojo"] = id_dojo #no coloca eso
    return redirect("/")


@app.route("/dojos/<int:id_dojo>") 
def info_dojos(id_dojo):
    datos = {"id":id_dojo}
    un_dojo = Dojos.obtener_un_dojo(datos) #variable para obtener el dojo
    un_dojo_un_ninja = Dojos.obtener_ninja_con_dojo(datos) #variable para obtener el  ninja asociado al dojo
    return render_template("info_dojo.html", dojo=un_dojo, dojo_y_ninja=un_dojo_un_ninja) #estamos enviando dos variables. #Pagina inicio se dirige a html hijo

@app.errorhandler(404)
def pagina_no_encontrada():
    return  'ESTA RUTA NO FUE ENCONTRADA', 404  
