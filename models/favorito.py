from sql_alchemy import banco

class FavoritoModel(banco.Model):
    __tablename__ = 'favoritos'

    id = banco.Column(banco.String, primary_key=True)
    nome = banco.Column(banco.String(40))
    link = banco.Column(banco.String(40))

    def __init__(self, id, nome, link):
        self.id = id
        self.nome = nome
        self.link = link


    def json(self):
        return {
        'id': self.id,
        'nome': self.nome,
        'link': self.link,
        }

    @classmethod
    def find_favorito(cls, id):
        favorito = cls.query.filter_by(id=id).first()
        if favorito:
            return favorito
        return None

    def save_favorito(self):
        banco.session.add(self)
        banco.session.commit()

    def update_favorito(self, nome, link):
        self.nome = nome
        self.link = link

    def delete_favorito(self):
        banco.session.delete(self)
        banco.session.commit()
