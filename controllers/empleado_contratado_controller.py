from models.empleado_contratado import EmpleadoContratado
from views.empleado_view import serializar_empleado
from flask import jsonify

def get_all_empleados():
    empleados = EmpleadoContratado.query.all()
    return jsonify([serializar_empleado(e) for e in empleados])

def get_empleado_by_id(id):
    empleado = EmpleadoContratado.query.get_or_404(id)
    return jsonify(serializar_empleado(empleado))