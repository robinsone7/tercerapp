# services/users/manage.py

import unittest
import coverage

from flask.cli import FlaskGroup

from project import create_app, db  # nuevo
from project.api.models import Paciente, Consulta, Doctor, Detconsulta  # nuevo


COV = coverage.coverage(
    branch=True,
    include='project/*',
    omit=[
        'project/tests/*',
        'project/config.py',
    ]
)
COV.start()

app = create_app()  # nuevo
cli = FlaskGroup(create_app=create_app)  # nuevo


@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command()
def test():
    """Ejecutando los test sin cobertura de código"""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

@cli.command('seed_db')
def seed_db():
    """Seeds the database."""
    """Seeds Paciente"""
    db.session.add(Paciente(name='fredy', email="abelthf@gmail.com"))
    db.session.add(Paciente(name='abel', email="abel.huanca@upeu.edu.pe"))
    db.session.add(Paciente(name='robinson', email="robinson@gmail.com"))
    db.session.add(Paciente(name='genaro', email="robinson.genaro@upeu.edu.pe"))
    """Seeds Doctor"""
    db.session.add(Doctor(name='noemi', email="nolemi@gmail.com", coddoctor="20102010"))
    db.session.add(Doctor(name='leon', email="noemi.leon@upeu.edu.pe", coddoctor="20102011"))
    db.session.add(Doctor(name='manzanares', email="manzana@gmail.com", coddoctor="20102012"))
    db.session.add(Doctor(name='lucy', email="lucy.asenjo@upeu.edu.pe", coddoctor="20102030"))
    db.session.commit()

@cli.command('seed_db2')
def seed_db2():
    """Seeds Consulta"""
    db.session.add(Consulta(idpaciente='1', detalle='dolor de cabeza constante', verificacion="A", recompensa="10"))
    db.session.add(Consulta(idpaciente='2', detalle='fiebre y dolor de diente', verificacion="B", recompensa="5"))
    """Seeds Detalle de Consulta"""
    db.session.add(Detconsulta(iddoctor='1', idconsulta="1", respuesta="dormir", estado="F"))
    db.session.add(Detconsulta(iddoctor='4', idconsulta="1", respuesta="pastillas", estado="F"))
    db.session.add(Detconsulta(iddoctor='1', idconsulta="2", respuesta="descansar", estado="F"))
    db.session.add(Detconsulta(iddoctor='2', idconsulta="2", respuesta="manzanilla", estado="F"))

    db.session.commit()



@cli.command()
def cov():
    """Ejecuta las pruebas unitarias con coverage."""
    tests = unittest.TestLoader().discover('project/tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Resumen de cobertura:')
        COV.report()
        COV.html_report()
        COV.erase()
        return 0
    sys.exit(result)


if __name__ == '__main__':
    cli()
