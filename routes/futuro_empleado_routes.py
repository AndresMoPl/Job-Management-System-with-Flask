from flask import Blueprint
from controllers.futuro_empleado_controller import get_all_futuros_empleados
from controllers.futuro_empleado_controller import get_futuro_empleado_by_id

futuro_empleado_bp = Blueprint('futuros_empleados', __name__)

@futuro_empleado_bp.route('/api/futuros-empleados', methods=['GET'])
def listar_futuros_empleados():
    return get_all_futuros_empleados()

@futuro_empleado_bp.route('/api/futuros-empleados/<int:id>', methods=['GET'])
def obtener_futuro_empleado(id):
    return get_futuro_empleado_by_id(id)