from models.empleado_contratado import EmpleadoContratado

def serializar_empleado(empleado_contratado):
    return {
        "id": empleado_contratado.id,
        "nombre": empleado_contratado.nombre,
        "experiencia_años": empleado_contratado.experiencia_años,
        "fecha_contratacion": empleado_contratado.fecha_contratacion,
        "empleo_id": empleado_contratado.empleo_id
    }