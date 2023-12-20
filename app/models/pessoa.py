from app.extensions import db
from app.models.carros_pessoas import CarrosPessoas


class Pessoa(db.Model):
    __tablename__ = "pessoas"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    casa_id = db.Column(db.Integer, db.ForeignKey("casas.id"))

    casa = db.relationship("Casa", back_populates="residentes")
    carros = db.relationship(
        "Carro", secondary="carros_pessoas", back_populates="pessoas"
    )

    def __repr__(self):
        return f'<Pessoa "{self.nome}">'

    def to_dict(self):
        return {"id": self.id, "name": self.nome}
