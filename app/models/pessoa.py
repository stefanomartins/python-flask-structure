from app.extensions import db


class Pessoa(db.Model):
    __tablename__ = "pessoas"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    casa_id = db.Column(db.Integer, db.ForeignKey("casas.id"))

    casa = db.relationship("Casa", back_populates="residentes")

    def __repr__(self):
        return f'<Pessoa "{self.nome}">'

    def to_dict(self):
        return {"id": self.id, "name": self.nome}
