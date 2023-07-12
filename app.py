from flask import Flask, redirect, render_template, session, request, url_for, session, make_response, flash
from flask.wrappers import Request
from MySQLdb.cursors import Cursor
from datetime import date
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configurar la conexión a la base de datos
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Rolex.b1'
app.config['MYSQL_DB'] = 'feedback'


mysql = MySQL(app)
app.secret_key = 'ghjklñ'

# Ruta para mostrar el formulario
@app.route('/')
def mostrar_formulario():
    cursor = mysql.connection.cursor()
    sql = "SELECT * FROM comentarios"
    cursor.execute(sql)
    date = cursor.fetchall()
    return render_template('index.html', date = date)

# Ruta para guardar los datos en la base de datos
@app.route('/guardar', methods=['POST'])
def guardar_datos():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        puntuacion = request.form['puntuacion']
        
        # Crear el cursor para ejecutar consultas
        cursor = mysql.connection.cursor()

        # Crear la consulta SQL para guardar los datos
        consulta = "INSERT INTO comentarios (nombre, apellido, puntuacion) VALUES (%s, %s, %s)"
        cursor.execute(consulta, (nombre, apellido, puntuacion))
        mysql.connection.commit()

        # Obtener los datos guardados desde la base de datos
        consulta = "SELECT * FROM comentarios"
        cursor.execute(consulta)
        date = cursor.fetchall()
        date = date

        # Cerrar el cursor
        cursor.close()
    return render_template('index.html', date=date)





if __name__ == '__main__':
    app.run(port=5000, debug=True)
