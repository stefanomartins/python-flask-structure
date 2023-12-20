from app.extensions import db
from app.models.carros_pessoas import CarrosPessoas


class Carro(db.Model):
    __tablename__ = "carros"
    placa = db.Column(db.String(7), primary_key=True)
    marca = db.Column(db.String(255))
    modelo = db.Column(db.String(255))

    pessoas = db.relationship(
        "Pessoa", secondary="carros_pessoas", back_populates="carros"
    )

    def __repr__(self):
        return f'<Carro "{self.placa}">'
