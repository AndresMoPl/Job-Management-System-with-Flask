from models.futuro_empleado import FuturoEmpleado
from views.futuro_empleado_view import serializar_futuro_empleado
from flask import jsonify

def get_all_futuros_empleados():
    empleadosfuturos = FuturoEmpleado.query.all()
    return jsonify([serializar_futuro_empleado(e) for e in empleadosfuturos])

def get_futuro_empleado_by_id(id):
    empleadofuturo = FuturoEmpleado.query.get_or_404(id)
    return jsonify(serializar_futuro_empleado(empleadofuturo))