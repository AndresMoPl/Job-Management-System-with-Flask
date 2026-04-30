from database import db

class EmpleadoContratado(db.Model):
    __tablename__ = 'empleados_contratados'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    experiencia_años = db.Column(db.Integer, nullable=False)
    fecha_contratacion = db.Column(db.String(20), nullable=False)   
    ## Llave foranea a Empleo
    empleo_id = db.Column(db.Integer, db.ForeignKey('empleos.id'), nullable=False) 
    
    ## Como navegar a Empleo
    
    empleo = db.relationship('Empleo', back_populates='contratados')   