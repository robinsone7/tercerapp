# services/users/project/api/users.py

from flask import Blueprint, jsonify, request, render_template
# from flask import Blueprint, jsonify, request
from sqlalchemy import exc

from project.api.models import Paciente, Consulta, Doctor, Detconsulta
from project import db


# users_blueprint = Blueprint('users', __name__)
consults_blueprint = Blueprint('consults', __name__, template_folder='./templates')


@consults_blueprint.route('/consults/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })

# @users_blueprint.route('/', methods=['GET'])
# def index():
#     return render_template('index.html')
#
# @users_blueprint.route('/', methods=['GET'])
# def index():
#     users = User.query.all()
#     return render_template('index.html', users=users)
#
@consults_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        db.session.add(Doctor(name=name, email=email))
        db.session.commit()
    doctors = Doctor.query.all()
    return render_template('index.html', doctors=doctors)

# @users_blueprint.route('/users', methods=['POST'])
# def add_user():
#     post_data = request.get_json()
#     username = post_data.get('username')
#     email = post_data.get('email')
#     db.session.add(User(username=username, email=email))
#     db.session.commit()
#     response_object = {
#         'status': 'success',
#         'message': f'{email} ha sido agregado!'
#     }
#     return jsonify(response_object), 201
#
@consults_blueprint.route('/doctors', methods=['POST'])
def add_doctor():
    post_data = request.get_json()
    response_object = {
        'status': 'falló',
        'message': 'Carga inválida.'
    }
    if not post_data:
        return jsonify(response_object), 400
    name = post_data.get('name')
    email = post_data.get('email')
    try:
        doctor = Doctor.query.filter_by(email=email).first()
        if not user:
            db.session.add(Doctor(name=name, email=email))
            db.session.commit()
            response_object['status'] = 'success'
            response_object['message'] = f'{email} ha sido agregado!'
            return jsonify(response_object), 201
        else:
            response_object['message'] = 'Disculpa. El email ya existe.'
            return jsonify(response_object), 400
    except exc.IntegrityError:
        db.session.rollback()
        return jsonify(response_object), 400

# @users_blueprint.route('/users/<user_id>', methods=['GET'])
# def get_single_user(user_id):
#     """Obteniendo detalles de un único usuario"""
#     user = User.query.filter_by(id=user_id).first()
#     response_object = {
#         'status': 'success',
#         'data': {
#             'id': user.id,
#             'username': user.username,
#             'email': user.email,
#             'active': user.active
#         }
#     }
#     return jsonify(response_object), 200
@consults_blueprint.route('/users/<user_id>', methods=['GET'])
def get_single_user(user_id):
    """Obteniendo detalles de un usuario único"""
    response_object = {
        'status': 'falló',
        'message': 'Usuario no existe'
    }
    try:
        user = User.query.filter_by(id=int(user_id)).first()
        if not user:
            return jsonify(response_object), 404
        else:
            response_object = {
                'status': 'success',
                'data': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'active': user.active
                }
            }
            return jsonify(response_object), 200
    except ValueError:
        return jsonify(response_object), 404


@consults_blueprint.route('/doctors', methods=['GET'])
def get_all_doctors():
    """Get all doctores"""
    response_object = {
        'status': 'success',
        'data': {
            'doctors': [doctor.to_json() for doctor in Doctor.query.all()]
        }
    }

    return jsonify(response_object), 200

@consults_blueprint.route('/pacientes', methods=['GET'])
def get_all_pacientes():
    """Get all pacientes"""
    response_object = {
        'status': 'success',
        'data': {
            'pacientes': [paciente.to_json() for paciente in Paciente.query.all()]
        }
    }

    return jsonify(response_object), 200

@consults_blueprint.route('/consultas', methods=['GET'])
def get_all_consultas():
    """Get all pacientes"""
    response_object = {
        'status': 'success',
        'data': {
            'consultas': [consulta.to_json() for consulta in Consulta.query.all()]
        }
    }

    return jsonify(response_object), 200

@consults_blueprint.route('/detconsulta', methods=['GET'])
def get_all_detconsultas():
    """Get all detconsulta"""
    response_object = {
        'status': 'success',
        'data': {
            'detconsultas': [detconsulta.to_json() for detconsulta in Detconsulta.query.all()]
        }
    }

    return jsonify(response_object), 200
