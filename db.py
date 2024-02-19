from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#engine: Permite a SQLAlchemy comunicarse con la bd


engine=create_engine('sqlite:///database/pacientes.db',connect_args={'check_same_thread':False})
#Advertencia: Crear el engine no conecta directamente a la bd
#Ahora creamos la sesion lo que nos permite realizar transacciones (operaciones) dentro de la bd
Session=sessionmaker(bind=engine)
session=Session()
#Ahora vamos a models.py y en los modelos(clases) donde queramos que se transformen en tablas,
#le añadiremos esta variable ,y esto se encargará de mapear y vincular la tabla
Base=declarative_base()