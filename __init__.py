from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/admin')
def dashboard():
    return render_template('dashboard.html', mactive_dash='active')

@app.route('/admin/adduser')
def adduser():
    return render_template('adduser.html', mactive_admin='active', mexpand='true')

app.run(host='0.0.0.0', port='8081', debug=True)