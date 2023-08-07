from flask import Flask
import scripts.gestionDB as db
from flask_restful import Api
from flask_restful import Resource,reqparse

import json

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

class manCert(Resource):
    
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('csr', type=str)
        self.parser.add_argument('nom', type=str)
        self.parser.add_argument('prenom', type=str)
        self.parser.add_argument('cert_ed25519', type=str)
        self.parser.add_argument('cert_eccp256', type=str)
        super(manCert, self).__init__()

    def get(self):
        
        # Crée un dictionnaire Python
        data = {
            "nom": "John",
            "age": 30,
            "marié": True,
            "hobbies": ["lecture", "voyages", "natation"]
        }

        
        return data

   
    
    def put(self):
        args = self.parser.parse_args()
        nom = args['nom']
        prenom = args['prenom']
        cert_ed25519 = args['cert_ed25519']
        cert_eccp256 = args['cert_eccp256']
        if db.ajouter_contact(nom,prenom,cert_ed25519,cert_eccp256):
            data = {
                "ret": "contact ajouté avec succes",
                
            }
        
        # Logique pour créer un nouvel utilisateur
        #return {'user_id': param, 'name': 'John Doe'}
        return data
api.add_resource(manCert, '/csr', '/csr/<string:csr>')



'''
@app.route('/')
def hello():
    contacts = db.lire_contacts()
    return contacts
'''
if __name__ == '__main__':
    app.run()
