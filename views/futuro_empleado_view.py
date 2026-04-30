from models.futuro_empleado import FuturoEmpleado

def serializar_futuro_empleado(FuturoEmpleado):
    return {
        "id": FuturoEmpleado.id,
        "nombre": FuturoEmpleado.nombre,
        "experiencia_años": FuturoEmpleado.experiencia_años
    }
        
    