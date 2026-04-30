from database import db

class FuturoEmpleado(db.Model):
    __tablename__ = 'futuros_empleados'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    experiencia_años = db.Column(db.Integer, nullable=False)