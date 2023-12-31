######
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


user = 'dbu1622292'
password = '^vD=SoKvJR2dd!;cV,G%'
host = 'db5014081360.hosting-data.io'  
port = '3306'  
database = 'dbs11750439'


url : db5014081360.hosting-data.io
user : dbu1622292
password : ^vD=SoKvJR2dd!;cV,G%
port : 3306
database : dbs11750439


user = 'freedb_kemado'
password = 'XX2?%egTkt?*hH#'
host = 'sql.freedb.tech'  
port = '3306'  
database = 'freedb_voitures'


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
    id_car_type= Column(Integer)


def get_cars():
    user = 'freedb_kemado'
    password = 'XX2?%egTkt?*hH#'
    host = 'sql.freedb.tech'  
    port = '3306'  
    database = 'freedb_voitures'

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
    user = 'freedb_kemado'
    password = 'XX2?%egTkt?*hH#'
    host = 'sql.freedb.tech'  
    port = '3306'  
    database = 'freedb_voitures'

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
    user = 'freedb_kemado'
    password = 'XX2?%egTkt?*hH#'
    host = 'sql.freedb.tech'  
    port = '3306'  
    database = 'freedb_voitures'

    engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}')

    Session = sessionmaker(bind=engine)
    session = Session()
    cars = session.query(Serie).filter(Serie.id_car_model == target_id).all()
    for car in cars:
        print(f"Model: {car.id_car_model},id: {car.id_car_serie},  Serie: {car.name}")
    session.close()
def get_trim(target_id):
    user = 'freedb_kemado'
    password = 'XX2?%egTkt?*hH#'
    host = 'sql.freedb.tech'  
    port = '3306'  
    database = 'freedb_voitures'

    engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}')

    Session = sessionmaker(bind=engine)
    session = Session()
    cars = session.query(Trim).filter(Trim.id_car_model == target_id).all()
    for car in cars:
        print(f"Model: {car.id_car_model},serie: {car.id_car_serie},  Trim: {car.id_car_trim}")
    session.close()
def get_carosserie(target_id):
    user = 'freedb_kemado'
    password = 'XX2?%egTkt?*hH#'
    host = 'sql.freedb.tech'  
    port = '3306'  
    database = 'freedb_voitures'

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

######################################################################################
def add_carosserie(make, model,carosserie):
    user = 'freedb_kemado'
    password = 'XX2?%egTkt?*hH#'
    host = 'sql.freedb.tech'  
    port = '3306'  
    database = 'freedb_voitures'

    engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}')

    Session = sessionmaker(bind=engine)
    session = Session()

    # Vérifier si la marque existe
    car_make = session.query(Car).filter_by(name=make).first()
    
    if car_make:
        reponse=f"Marque {make} trouvée. \n"
        #print(f"Marque {make} trouvée") 
        make_id = car_make.id_car_make
    else:
        #print(f"Insertion de la nouvelle marque {make}")
        reponse=f"Insertion de la nouvelle marque {make}. \n"
        car_make = Car(name=make)
        session.add(car_make)
        session.commit()
        make_id = car_make.id_car_make

    # Vérifier si le modèle existe pour cette marque
    car_model = session.query(Model).filter_by(name=model, id_car_make=make_id).first()

    if car_model:
        #print(f"Modèle {model} de la marque {make} trouvé")
        reponse+=f"Modèle {model} de la marque {make} trouvé. \n"
        model_id = car_model.id_car_model
    else:
       # print(f"Insertion du nouveau modèle {model} pour la marque {make}")
        reponse+=f"Insertion du nouveau modèle {model} pour la marque {make}. \n"
        car_model = Model(name=model, id_car_make=make_id)  
        session.add(car_model)
        session.commit()

        car_model = session.query(Model).filter_by(name=model, id_car_make=make_id).first()
        model_id = car_model.id_car_model
    

    Carosseries=get_carosserie(model_id)
    print(Carosseries)
    n=0
    for ele in Carosseries:
        if carosserie.casefold()==ele['Carosserie'].casefold():

            n+=1
        
    if n==0:
        #print("add carosserie")
        reponse+=f"add carosserie. \n "
        
        trim = session.query(Trim).filter(Trim.id_car_model == model_id).first()
        id_trim=trim.id_car_trim
        #print(id_trim)

        car_carosserie = Specification(id_car_trim=id_trim, id_car_specification=2,value=carosserie,id_car_type=1)  
        session.add(car_carosserie)
        session.commit()
        #print("carosserie ajouté avec succes")



    else:
        #print("carosserie existante")
        reponse+=f"carosserie existante. \n"
    #print(reponse)
            
    return reponse

    #print("Marque et modèle existants dans la base")

# Exemple d'appel
#check_and_insert("Renault", "clio","wagon test")

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