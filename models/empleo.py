from database import db

class Empleo(db.Model):
    __tablename__ = 'empleos'
    
    id = db.Column(db.Integer, primary_key=True)
    empleo = db.Column(db.String(100), nullable=False)
    salario = db.Column(db.Float, nullable=False)
    
    contratados = db.relationship('EmpleadoContratado', back_populates='empleo')