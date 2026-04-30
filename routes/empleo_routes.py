from flask import Blueprint # Importamos Blueprint para crear un grupo de rutas
from controllers.empleo_controller import get_all_empleos # Importamos la función del controlador que maneja la lógica de negocio
from controllers.empleo_controller import get_empleo_by_id # Importamos la función del controlador que maneja la lógica de negocio para obtener un empleo por ID

# Un blueprint es una forma de organizar un grupo de rutas relacionadas. En este caso, todas las rutas relacionadas con "empleos" estarán bajo este blueprint.

empleo_bp = Blueprint('empleos', __name__) # Creamos un Blueprint llamado 'empleos'

@empleo_bp.route('/api/empleos', methods=['GET']) # Definimos una ruta para obtener todos los empleos
def listar_empleo():
    return get_all_empleos() # Llamamos a la función del controlador para obtener los datos y devolverlos como respuesta

@empleo_bp.route('/api/empleos/<int:id>', methods=['GET']) # Definimos una ruta para obtener un empleo específico por su ID
def obtener_empleo(id):
    return get_empleo_by_id(id) # Llamamos a la función del controlador para obtener el empleo por ID y devolverlo como respuesta