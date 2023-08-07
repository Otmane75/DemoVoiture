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
class Trim(Base):
    __tablename__ = 'car_trim'
    id_car_trim = Column(Integer, primary_key=True)
    id_car_serie = Column(Integer)
    id_car_model = Column(Integer)
    #name = Column(String(255))
    #date_create = Column(Integer)
   # date_update = Column(Integer)
   # id_car_type = Column(Integer)

class Specification(Base):
    __tablename__ = 'car_specification_value'
    id_car_specification_value = Column(Integer, primary_key=True)
    id_car_trim = Column(Integer)
    id_car_specification = Column(Integer)
    value = Column(String(255))


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
    cars_list=[]
    for car in cars:
        print(f"ID: {car.id_car_make}, Marque: {car.name}")
        ele={"id": car.id_car_make, "Marque": car.name}
        cars_list.append(ele)
    session.close()
    return cars_list

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
    model_list=[]
    for car in cars:
        #print(f"ID: {car.id_car_model}, Model: {car.name}")
        #model_list.append(car.name)
        ele={"id": car.id_car_model, "Model": car.name}
        model_list.append(ele)
    session.close()
    return model_list

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
def get_trim(target_id):
    user = 'root'
    password = ''
    host = 'localhost'  
    port = '3306'  
    database = 'car2db_fra_cut'

    engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}')

    Session = sessionmaker(bind=engine)
    session = Session()
    cars = session.query(Trim).filter(Trim.id_car_model == target_id).all()
    for car in cars:
        print(f"Model: {car.id_car_model},serie: {car.id_car_serie},  Trim: {car.id_car_trim}")
    session.close()
def get_carosserie(target_id):
    user = 'root'
    password = ''
    host = 'localhost'  
    port = '3306'  
    database = 'car2db_fra_cut'

    engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}')

    Session = sessionmaker(bind=engine)
    session = Session()
    geted=[]
    trims = session.query(Trim).filter(Trim.id_car_model == target_id).all()

    carosseries_list=[]
    for trim in trims:
        #print(f"Model: {trim.id_car_model},serie: {trim.id_car_serie},  Trim: {trim.id_car_trim}")

        cars = session.query(Specification).filter(Specification.id_car_trim == trim.id_car_trim).filter(Specification.id_car_specification == 2).all()
        
        for car in cars:
            if car.value not in geted:
                #print(f"Carosserie: {car.value},spec: {car.id_car_specification},  Trim: {car.id_car_trim}")
                geted.append(car.value)
                ele={"id": car.id_car_specification, "Carosserie": car.value}
                carosseries_list.append(ele)
    #carosseries_list=geted
        
    session.close()
    return carosseries_list

'''
get_cars()
print("------------------------------------------------------------")
get_model(76)
print("------------------------------------------------------------")
#get_serie(810)
#get_trim(810)
print("------------------------------------------------------------")
get_carosserie(754)

'''