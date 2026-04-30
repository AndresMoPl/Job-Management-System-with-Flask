import pandas as pd
from database import db
from models.empleo import Empleo
from models.futuro_empleado import FuturoEmpleado
from models.empleado_contratado import EmpleadoContratado

def cargar_csv():
    #solo carga si las tablas estan vacias
    if Empleo.query.first():
        print("La base de datos ya tiene datos, no se cargará el CSV.")
        return
    
    # Lectura empleos
    df_empleos = pd.read_csv('data/empleos.csv')
    for _, row in df_empleos.iterrows(): #iterrows devuelve un iterador que produce tuplas de (índice, fila)
        db.session.add(Empleo(
            id=int(row['id']),
            empleo=row['empleo'],
            salario=float(row['salario'])
        #db.session.add es una función de SQLAlchemy que se utiliza para agregar una instancia de modelo a la sesión actual. En este caso, se está agregando una instancia de Empleo creada a partir de cada fila del DataFrame.
        ))
        
    db.session.commit()# Guarda los cambios en la base de datos después de agregar los empleos
    print("Empleos cargados exitosamente desde el archivo CSV.")
        
        # Lectura futuros empleados
        
    df_futuros = pd.read_csv('data/futuros_empleados.csv')
    for _, row in df_futuros.iterrows():
            # db.session.add es una función de SQLAlchemy que se utiliza para agregar una instancia de modelo a la sesión actual. En este caso, se está agregando una instancia de FuturoEmpleado creada a partir de cada fila del DataFrame.
            db.session.add(FuturoEmpleado(
                id=int(row['id']),
                nombre=row['nombre'],
                experiencia_años=int(row['experiencia_años'])
            ))
        
    db.session.commit()
    print("Futuros empleados cargados exitosamente desde el archivo CSV.")
        
        # Lectura empleados contratados
        
    df_contratados = pd.read_csv('data/empleados_contratados.csv')
    for _, row in df_contratados.iterrows():
            db.session.add(EmpleadoContratado(
                id=int(row['id']),
                nombre=row['nombre'],
                experiencia_años=int(row['experiencia_años']),
                empleo_id=int(row['empleo_id']),
                fecha_contratacion=row['fecha_contratacion']
            ))
            
    db.session.commit()
    print("Datos cargados exitosamente desde los archivos CSV.")