from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, Float

import db

'''
Creamos una clase llamada Paciente

'''

class Especialidad():
    def __init__(self, especialidad):
        self.especialidad = especialidad
        print("Especialidad creado")

class Enfermedad(Especialidad):
    def __init__(self, especialidad, enfermedad):
        super().__init__(especialidad)
        self.enfermedad = enfermedad
        print("Enfermedad creado")

class Paciente (db.Base, Enfermedad):
    __tablename__ = "paciente"
    id_paciente = Column(Integer, primary_key=True) # Identificador unico de cada paciente
    especialidad = Column(String(100), nullable=False) # Especialidad que trata al paciente
    enfermedad = Column(String(100), nullable=False) # Enfermedad que tiene el paciente
    nombre = Column(String(100), nullable=False) # Nombre del paciente, un texto de maximo 100 caracteres
    apellidos = Column(String(100), nullable=False)  # Apellido del paciente, un texto de maximo 100 caracteres
    fecha_ingreso = Column(String(10), nullable=False) # Fecha que indica el día en que ingresó un paciente en formato xx/xx/xxxx
    sexo = Column(String(1), nullable=False) # Marca del sexo con una letra: H=hombre, M=mujer
    edad = Column(Integer)
    fecha_alta = Column(String(10),nullable=True)  # Fecha que indica el día en que se dio de alta a un paciente en formato xx/xx/xxxx
    activo = Column(Boolean)
    dias = Column(Integer, nullable=True)



    def __init__(self,especialidad, enfermedad, nombre, apellidos, fecha_ingreso, sexo, edad, fecha_alta, activo, dias):
        Enfermedad.__init__(self, especialidad, enfermedad)
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_ingreso = fecha_ingreso
        self.sexo = sexo
        self.edad = edad
        self.fecha_alta = fecha_alta
        self.activo = activo
        self.dias = dias

        print("Paciente creado")


    def __repr__(self):
        return "Paciente {}: {} ({}) {} {} {}".format(self.id_paciente, self.nombre,self.apellidos, self.fecha_ingreso, self.sexo, self.edad)

    def __str__(self):
        return "Paciente {}: {} ({}) {} {} {}".format(self.id_paciente, self.nombre,self.apellidos, self.fecha_ingreso, self.sexo, self.edad)


