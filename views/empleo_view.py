from models.empleo import Empleo

def serializar_empleo(empleo):
    return {
        "id": empleo.id,
        "empleo": empleo.empleo,
        "salario": empleo.salario        
    }