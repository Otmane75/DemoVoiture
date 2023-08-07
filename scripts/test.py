from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

'''
user = 'root'
password = ''
host = 'localhost'  
port = '3306'  
database = 'car2db_fra_cut'

engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}')

Session = sessionmaker(bind=engine)
session = Session()
'''


Base = declarative_base()

class Car(Base):
    __tablename__ = 'car_make'
    id_car_make = Column(Integer, primary_key=True)
    name = Column(String(255))
    #date_create = Column(Integer)
   # date_update = Column(Integer)
   # id_car_type = Column(Integer)

class Model(Base):
    __tablename__ = 'car_model'
    id_car_model = Column(Integer, primary_key=True)
    id_car_make = Column(Integer)
    name = Column(String(255))
    #date_create = Column(Integer)
   # date_update = Column(Integer)
   # id_car_type = Column(Integer)
class Serie(Base):
    __tablename__ = 'car_serie'
    id_car_serie = Column(Integer, primary_key=True)
    id_car_model = Column(Integer)
    
    name = Column(String(255))
    #date_create = Column(Integer)
   # date_update = Column(Integer)
   # id_car_type = Column(Integer)


def get_cars():
    user = 'root'
    password = ''
    host = 'localhost'  
    port = '3306'  
    database = 'car2db_fra_cut'

    engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}')

    Session = sessionmaker(bind=engine)
    session = Session()
    cars = session.query(Car).all()
    for car in cars:
        print(f"ID: {car.id_car_make}, Marque: {car.name}")
    session.close()

def get_model(target_id):
    user = 'root'
    password = ''
    host = 'localhost'  
    port = '3306'  
    database = 'car2db_fra_cut'

    engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}')

    Session = sessionmaker(bind=engine)
    session = Session()
    cars = session.query(Model).filter(Model.id_car_make == target_id).all()
    for car in cars:
        print(f"ID: {car.id_car_model}, Model: {car.name}")
    session.close()
def get_serie(target_id):
    user = 'root'
    password = ''
    host = 'localhost'  
    port = '3306'  
    database = 'car2db_fra_cut'

    engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}')

    Session = sessionmaker(bind=engine)
    session = Session()
    cars = session.query(Serie).filter(Serie.id_car_model == target_id).all()
    for car in cars:
        print(f"Model: {car.id_car_model},id: {car.id_car_serie},  Serie: {car.name}")
    session.close()


get_cars()
print("------------------------------------------------------------")
get_model(76)
print("------------------------------------------------------------")
get_serie(810)

