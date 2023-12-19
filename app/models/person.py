from app.extensions import db

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def __repr__(self):
        return f'<Person "{self.name}">'
    
    def to_dict(self):
        return {'id': self.id, 'name': self.name}