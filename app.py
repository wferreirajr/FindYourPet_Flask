import sqlite3
import os

# from crypt import methods
from flask import Flask, render_template, request, url_for, flash, redirect
from importlib_metadata import files
from werkzeug.utils import secure_filename
from datetime import datetime

UPLOAD_FOLDER = './static'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
DATA_FORMAT = datetime.now()

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_db_connection():
    conn = sqlite3.connect('db/findyourpet.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/sair')
def sair():
    return '<h1>TEM QUE SAIR DO SISTEMA</h1>'

@app.route('/admin')
def dashboard():
    return render_template('dashboard.html', mactive_dash='active')

@app.route('/admin/adduser')
def adduser():
    return render_template('adduser.html', mactive_admin='active', mexpand='true')

@app.route('/admin/addanimal')
def addanimal():
    return render_template('reg_aminalzinho.html', mactive_animal='active')

@app.route('/gatos')
def list_cats():
    conn = get_db_connection()
    gatos = conn.execute('SELECT * FROM animals WHERE Especie IS "Gato"').fetchall()
    conn.close()
    return render_template('gatos.html', gatos=gatos)

@app.route('/cachorros')
def list_dogs():
    conn = get_db_connection()
    cachorros = conn.execute('SELECT * FROM animals WHERE Especie IS "Cachorro"').fetchall()
    conn.close()
    return render_template('cachorros.html', cachorros=cachorros)

@app.route('/createusr/', methods=('GET', 'POST'))
def create_user():
    if request.method == 'POST':
        nome = request.form['nome_completo']
        email = request.form['email']
        senha = request.form['senha']
        type = request.form['tipo']

        if not nome:
            flash('O nome ?? requedido!')
        elif not email:
            flash('O email ?? requedido!')
        elif not senha:
            flash('O senha ?? requedido!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO accounts (NomeCompleto, Email, Tipo, Senha) VALUES (?, ?, ?, ?)',
                            (nome, email, type, senha))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('registro.html')

@app.route('/createusradmin/', methods=('GET', 'POST'))
def create_user_admin():
    if request.method == 'POST':
        nome = request.form['psaNomeCompleto']
        email = request.form['psaEmail']
        type = request.form['psaTipo']
        celular = request.form['psaTelCelular']
        fixo = request.form['psaTelFixo']
        senha = request.form['psasenha']

        cep = request.form['edrCep']
        endereco = request.form['edrRua']
        numero = request.form['edrNumero']
        complemento = request.form['edrComplemento']
        bairro = request.form['edrBairro']
        cidade = request.form['edrCidade']
        estado = request.form['edrEstado']

        if not nome:
            flash('O nome ?? requedido!')
        elif not email:
            flash('O email ?? requedido!')
        elif not senha:
            flash('O senha ?? requedido!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO accounts (NomeCompleto, Email, Tipo, Senha, TelCelular, TelFixo, Cep, Rua, Numero, Complemento, Bairro, Cidade, Estado) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (nome, email, type, senha, celular, fixo, cep, endereco, numero, complemento, bairro, cidade, estado))
            conn.commit()
            conn.close()
            return redirect(url_for('adduser'))

    return render_template('registro.html')

@app.route('/registeranimal/', methods=('GET', 'POST'))
def register_aminal():
    if request.method == 'POST':
        nome = request.form['amnNomeCompleto']
        especie = request.form['amnEspecie']
        sexo = request.form['amnSexo']
        idade = request.form['amnIdade']
        porte = request.form['amnPorte']
        sobre = request.form['amnSobre']

        cep = request.form['edrCep']
        endereco = request.form['edrRua']
        numero = request.form['edrNumero']
        complemento = request.form['edrComplemento']
        bairro = request.form['edrBairro']
        cidade = request.form['edrCidade']
        estado = request.form['edrEstado']

        send_file = request.files['file']
        if send_file and allowed_file(send_file.filename):
            filename = DATA_FORMAT.strftime('%d-%m-%Y_%H_%M_%S') + '_' + secure_filename(send_file.filename)
            send_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        if not nome:
            flash('O nome ?? requedido!')
        else:
            foto = filename
            conn = get_db_connection()
            conn.execute('INSERT INTO animals (NomeCompleto, Foto, Especie, Sexo, Idade, Porte, Sobre, Cep, Rua, Numero, Complemento, Bairro, Cidade, Estado) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (nome, foto, especie, sexo, idade, porte, sobre, cep, endereco, numero, complemento, bairro, cidade, estado))
            conn.commit()
            conn.close()
            return redirect(url_for('addanimal'))

    return render_template('registro.html')

if __name__ == '__main__':
   app.run()