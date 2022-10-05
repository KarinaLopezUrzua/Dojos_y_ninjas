from tarea11 import app
from tarea11.controladores import controlador_ninja
from tarea11.controladores import controlador_dojo

app.secret_key = 'mantener en secreto'

if __name__=="__main__":
    app.run(debug=True)  