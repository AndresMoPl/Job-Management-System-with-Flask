from models.empleo import Empleo
from views.empleo_view import serializar_empleo
from flask import jsonify

def get_all_empleos():
    empleos = Empleo.query.all() # Consulta todos los empleos en la base de datos
    return jsonify([serializar_empleo(e) for e in empleos]) # Convierte una lista de empleos de la base de datos serializados en formato JSON

def get_empleo_by_id(id):
    empleo = Empleo.query.get_or_404(id) # Consulta un empleo por su ID, si no existe devuelve un error 404
    return jsonify(serializar_empleo(empleo)) # Devuelve el empleo serializado en formato JSON