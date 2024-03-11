from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = request.form.get('nombre', '')
        return render_template('base.html', nombre=nombre)
    else:
        return render_template('base.html')

@app.route('/datos_personales')
def datos_personales():
    return render_template('datos_personales.html')

@app.route('/habilidades_personales')
def habilidades_personales():
    return render_template('habilidades_personales.html')

@app.route('/certificados')
def certificados():
    return render_template('certificados.html')

if __name__ == '__main__':
    app.run(debug=True)
