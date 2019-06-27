# services/users/project/api/models.py

from project import db

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
   
    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'active': self.active
        }

    def __init__(self, username, email):
        self.username = username
        self.email = email

class Paciente(db.Model):
    __tablename__ = 'pacientes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=True)
    email = db.Column(db.String(128), nullable=True)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }

    def __init__(self, name, email):
        self.name = name
        self.email = email
