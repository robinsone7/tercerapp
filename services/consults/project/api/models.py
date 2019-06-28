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

class Consulta(db.Model):
    __tablename__ = 'consultas'
    id = db.Column(db.Integer, primary_key=True)
    idpaciente = db.Column(db.Integer, db.ForeignKey('pacientes.id'), index=True)
    detalle = db.Column(db.String(128), nullable=False)
    verificacion = db.Column(db.String(1), nullable=True) 
    recompensa = db.Column(db.Integer)

    def to_json(self):
        return {
            'id': self.id,
            'idpaciente': self.idpaciente,
            'detalle': self.detalle,
            'verificacion': self.verificacion,
            'recompensa': self.recompensa
        }

    def __init__(self, idpaciente, detalle, verificacion, recompensa):
        self.idpaciente = idpaciente
        self.detalle = detalle
        self.verificacion = verificacion
        self.recompensa = recompensa    

class Doctor(db.Model):
    __tablename__ = 'doctors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    email = db.Column(db.String(128), nullable=False)
    coddoctor = db.Column(db.String(128), nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'coddoctor': self.coddoctor
        }

    def __init__(self, name, email, coddoctor):
        self.name = name
        self.email = email
        self.coddoctor = coddoctor

class Detconsulta(db.Model):
    __tablename__ = 'detconsultas'
    id = db.Column(db.Integer, primary_key=True)
    iddoctor = db.Column(db.Integer, db.ForeignKey('doctors.id'), index=True)
    idconsulta = db.Column(db.Integer, db.ForeignKey('consultas.id'),index= True)
    respuesta = db.Column(db.String(128), nullable=False)
    estado = db.Column(db.String(1), nullable=True)
    
    def to_json(self):
        return {
            'id': self.id,
            'iddoctor': self.iddoctor,
            'idconsulta': self.idconsulta,
            'respuesta': self.respuesta,
            'estado': self.estado
        }

    def __init__(self, iddoctor, idconsulta, respuesta, estado):
        self.iddoctor = iddoctor
        self.idconsulta = idconsulta
        self.respuesta = respuesta
        self.estado = estado
        