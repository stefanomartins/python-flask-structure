from app.extensions import db


class CarrosPessoas(db.Model):
    __tablename__ = "carros_pessoas"
    id = db.Column(db.Integer, primary_key=True)
    carro_placa = db.Column(db.String(7), db.ForeignKey("carros.placa"))
    pessoa_id = db.Column(db.Integer, db.ForeignKey("pessoas.id"))