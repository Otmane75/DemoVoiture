from flask import Flask
import scripts.gestionDB as db
from flask_restful import Api
from flask_restful import Resource,reqparse

import jsonify

app = Flask(__name__)
api = Api(app)



class getCar(Resource):
    
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('param', type=str, required=True)
        super(getCar, self).__init__()

    def get(self):
        contacts = db.lire_contacts()
        return contacts

    def post(self):
        args = self.parser.parse_args()
        arg1 = args['param']
        certificat=db.lire_certificat(int(arg1))
        # Logique pour créer un nouvel utilisateur
        #return {'user_id': param, 'name': 'John Doe'}
        return certificat
api.add_resource(getCar, '/car', '/car/<int:param>')



# Données pour remplir les sélecteurs
#select1_options = db.get_cars()
#select2_options = db.get_model(80)
#select3_options = db.get_carosserie(753)




class Options(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('model', type=int)
        super(Options, self).__init__()
   
    def get(self, marque=None,model=None):
        if model is None:
            if marque is None:
                select1_options = db.get_cars()
                return select1_options
            else:
                
                select2_options = db.get_model(marque)
                #model_options = get_model_options(model)
                return select2_options
        else:
            select3_options = db.get_carosserie(model)
            return select3_options
        

api.add_resource(Options, '/api/options','/api/options/<int:marque>','/api/options/<int:marque>/<int:model>')

class Insertion(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('model', type=str)
        self.parser.add_argument('marque', type=str)
        self.parser.add_argument('carosserie', type=str)
        super(Insertion, self).__init__()
   
    def get(self, marque=None,model=None,carosserie=None):
        if (model is None) or (marque is None) or (carosserie is None):
            reponse = "Veuillez remplir tt les champs"
            return reponse
        else:
            reponse = db.add_carosserie(marque, model,carosserie)
            return reponse
        

api.add_resource(Insertion, '/api/insertion/<string:marque>/<string:model>/<string:carosserie>')





@app.route('/')
def index():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run()
