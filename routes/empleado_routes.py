from flask import Blueprint
from controllers.empleado_contratado_controller import get_all_empleados
from controllers.empleado_contratado_controller import get_empleado_by_id

empleado_bp = Blueprint ('empleados', __name__)

@empleado_bp.route('/api/empleados', methods=['GET'])
def listar_empleados():
    return get_all_empleados()

@empleado_bp.route('/api/empleados/<int:id>', methods=['GET'])
def obtener_empleado(id):
    return get_empleado_by_id(id)