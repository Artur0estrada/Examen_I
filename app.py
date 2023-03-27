from flask import Flask, render_template, request, redirect, session, jsonify, url_for

app = Flask(__name__)
app.secret_key = 'quiensabekaja'

@app.route('/')
def index():
    return redirect('./login')

@app.route('/index')
def inicio():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        return redirect('./login')

@app.route('/login', methods=['GET', 'POST'])
def login():  # put application's code here
    if request.method == 'GET':
        return render_template("login.html")
    else:
        if request.method == 'POST':
            return redirect('./index')
        else:
            msg = f'Usuario o contraseña incorrectos.'
            return render_template("login.html", mensaje=msg)
        

@app.route('/renta', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("renta.html")
    else:
        if request.method == 'POST':
            #Nombre = request.form['username']
            #Primer_apellido = request.form['password']
            #Segundo_apellido = request.form['first_name']
            #correo = request.form['last_name']
            #telefono = request.form['phone']
            #Bicicleta = request.form['respuesta']
            return redirect('./index')
            
@app.route('/estado', methods=['GET'])
def estado():
    if request.method == 'GET':
        return render_template("estado.html")
    else:
        return redirect('./index')


if __name__ == '__main__':
    app.run(debug=True)