from flask import Flask 
from config import Config
from database import db
from services.csv_loader import cargar_csv

# Modelos
from models.empleo import Empleo
from models.empleado_contratado import EmpleadoContratado
from models.futuro_empleado import FuturoEmpleado

from routes.empleo_routes import empleo_bp # Importamos el blueprint de rutas para empleos
from routes.empleado_routes import empleado_bp # Importamos el blueprint de rutas para empleados contratados
from routes.futuro_empleado_routes import futuro_empleado_bp # Importamos el blueprint de rutas para futuros empleados


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app) # Inicializa la extensión de la base de datos con la aplicación Flask

# Registramos el blueprint de rutas para empleos en la aplicación Flask
app.register_blueprint(empleo_bp) 
app.register_blueprint(empleado_bp)
app.register_blueprint(futuro_empleado_bp)




with app.app_context(): # Crea un contexto de aplicación para ejecutar código que requiere acceso a la aplicación
    db.create_all() # Crea las tablas en la base de datos
    cargar_csv() # Carga los datos desde los archivos CSV a la base de datos
    
if __name__ == '__main__':
    app.run(debug=True)