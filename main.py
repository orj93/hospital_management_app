
from sqlalchemy import or_

from flask import Flask, render_template, request, redirect, url_for
from models import Paciente
import db
from datetime import date, datetime
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/crear-paciente", methods=["POST"])
def crear():
    paciente=Paciente(especialidad=request.form["contenido_especialidad"], enfermedad=request.form["contenido_enfermedad"],
                      nombre=request.form["contenido_nombre"], apellidos=request.form["contenido_apellidos"],
                      fecha_ingreso=datetime.now(),sexo=request.form["contenido_sexo"],
                      edad=request.form["contenido_edad"], activo=True, fecha_alta=None, dias=None)


    paciente.fecha_ingreso = paciente.fecha_ingreso.strftime('%d-%m-%Y')
    print(type(paciente.fecha_ingreso))
    db.session.add(paciente)
    db.session.commit()
    return redirect(url_for('home'))



@app.route("/ingresos",methods=["POST","GET"])
def ver_ingresos():

    todos_los_pacientes = db.session.query(Paciente).all()

    return render_template("ingresos.html", lista_de_pacientes=todos_los_pacientes)


@app.route("/borrar-paciente/<id>")
def desactivar(id):
    paciente = db.session.query(Paciente).filter_by(id_paciente=id).first()
    paciente.activo = not(paciente.activo)
    paciente.fecha_alta = datetime.now()
    print("Alta", paciente.fecha_alta)
    print(type(paciente.fecha_alta))
    paciente.fecha_ingreso =datetime.strptime(paciente.fecha_ingreso, '%d-%m-%Y')
    print("Ingreso",paciente.fecha_ingreso)
    print(type(paciente.fecha_ingreso))
    paciente.dias = paciente.fecha_alta-paciente.fecha_ingreso
    paciente.dias=paciente.dias.days
    print("dias",paciente.dias)
    print(type(paciente.dias))
    paciente.fecha_alta = paciente.fecha_alta.strftime('%d-%m-%Y')
    print("Alta", paciente.fecha_alta)
    print(type(paciente.fecha_alta))
    paciente.fecha_ingreso = paciente.fecha_ingreso.strftime('%d-%m-%Y')
    print("Ingreso",paciente.fecha_ingreso)
    print(type(paciente.fecha_ingreso))
    db.session.commit()
    return redirect(url_for("ver_ingresos"))

@app.route("/altas",methods=["POST","GET"])
def ver_altas():
    todos_los_pacientes = db.session.query(Paciente).all()

    return render_template("altas.html", lista_de_pacientes=todos_los_pacientes)

@app.route("/filtros",methods=["POST","GET"])
def ver_filtros():
    if request.method == 'POST':

        print("Hola estoy en el if")
        busqueda = db.session.query(Paciente).filter_by(nombre=request.form["contenido_nombre"]).all()

        #busqueda = db.session.query(Paciente).filter(or_(Paciente.nombre == request.form["contenido_nombre"]),Paciente.especialidad == request.form["contenido_especialidad"])

        conexion = sqlite3.connect(r"C:\Users\user\PycharmProjects\proyecto_final\database\pacientes.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT * from paciente")
        pacientes = cursor.fetchall()
        print(pacientes)

        busqueda = db.session.query(Paciente).filter(or_(Paciente.nombre == request.form["contenido_nombre"],Paciente.especialidad == request.form["contenido_especialidad"])).all()
        print("Hola",busqueda)
        conexion.close()
        return render_template('filtros.html', i=busqueda)

    else:
        return render_template("filtros.html")

@app.route("/eliminar-paciente/<id>")
def eliminar(id):
    paciente = db.session.query(Paciente).filter_by(id_paciente=id).delete()
    db.session.commit()
    return redirect(url_for("ver_altas"))


@app.route("/editar-paciente/<id>")
def editar(id):
    return render_template("editar.html",id_paciente=id)

@app.route("/editar-paciente",methods=["POST"])
def modificar():
    paciente = db.session.query(Paciente).filter_by(id_paciente=int(request.form["contenido_id_paciente"])).first()
    paciente.nombre = request.form["contenido_nombre"]
    paciente.apellidos = request.form["contenido_apellidos"]
    paciente.enfermedad = request.form["contenido_enfermedad"]
    paciente.especialidad = request.form["contenido_especialidad"]
    paciente.edad = request.form["contenido_edad"]
    paciente.sexo = request.form["contenido_sexo"]
    try:
        db.session.commit()
    except:
        db.session.rollback()
    return redirect(url_for("ver_ingresos"))

if __name__=="__main__":
    db.Base.metadata.create_all(db.engine)
    app.run(debug=True)




