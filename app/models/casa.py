from app.extensions import db


class Casa(db.Model):
    __tablename__ = "casas"
    id = db.Column(db.Integer, primary_key=True)
    logradouro = db.Column(db.String(255))
    numero = db.Column(db.Integer)
    complemento = db.Column(db.String(255))
    
    residentes = db.relationship("Pessoa", back_populates="casa")

    def __repr__(self):
        return (
            f'<Casa "{self.id}, {self.logradouro}, {self.numero}, {self.complemento}, {self.residentes}">'
        )