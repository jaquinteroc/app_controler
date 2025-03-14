from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    #return "hola asdasd mundo!"
    cursos = ['PHP', 'PYTHON', 'JAVA']
    data={
        'titulo':'IndexTitulo',
        'bienvenida':'carechimbita',
        'cursos': cursos,
        'numero_cursos': len(cursos)
    }
    return render_template("index.html", data=data)

@app.route('/contacto/<nombre>/<int:edad>')
def contacto(nombre, edad):
    data ={
        'titulo':'contacto',
        'nombre': nombre,
        'edad' : edad,
    }
    return render_template('contacto.html', data=data)
    
def query_string():
    print(request)
    return 'ok'

if __name__ == '__main__':
    app.add_url_rule('/query_string', view_func=query_string)
    app.run(debug=True,port=5000)
