from flask_restful import Resource, reqparse
from models.favorito import FavoritoModel

class Favoritos(Resource):
    def get(self):
        return {'favoritos': [favorito.json() for favorito in FavoritoModel.query.all()]}


class Favorito(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str, required=True, help = "The field 'nome' cannot be left blank")
    argumentos.add_argument('link')

    def get(self, id):
        favorito = FavoritoModel.find_favorito(id)
        if favorito:
            return favorito.json()
        return {'message': 'Favorito not found'}, 404

    def post(self, id):
        if FavoritoModel.find_favorito(id):
            return {'message': 'Favorito id "{}" already exists'.format(id)}, 400

        dados = Favorito.argumentos.parse_args()
        favorito = FavoritoModel(id, **dados)
        try:
            favorito.save_favorito()
        except:
            return {'message': 'An internal error ocurred trying to save'},500
        return favorito.json()


    def put(self, id):
        dados = Favorito.argumentos.parse_args()
        favorito_encontrado = FavoritoModel.find_favorito(id)

        if favorito_encontrado:
            favorito_encontrado.update_favorito(**dados)
            favorito_encontrado.save_favorito()
            return favorito_encontrado.json(), 200
        hotel= FavoritoModel(id, **dados)
        try:
            hotel.save_favorito()
        except:
            return {'message': 'An internal error ocurred trying to save'},500
        return favorito.json(), 201

    def delete(self, id):
        favorito = FavoritoModel.find_favorito(id)
        if favorito:
            try:
                favorito.delete_hotel()
            except:
                return {'message': 'An internal error ocurred trying to delete'},500
            return {'message': 'Favorito deleted'}
        return {'message': 'Favor not found', 404}
