import sqlite
from models import Producto

def run():
    arroz = Producto('Arroz', 1.25)
    tacos = Producto('Tacos', 2.50)
    sqlite.session.add(arroz)
    sqlite.session.add(tacos)
    sqlite.session.commit()
    print("Se agregó un nuevo registro. ID: " + str(arroz.id))
    print("Se agregó un nuevo registro. ID: " + str(tacos.id))

if __name__ == '__main__':
    sqlite.Base.metadata.drop_all(sqlite.engine) # Límpia la base de datos (La elimina)
    sqlite.Base.metadata.create_all(sqlite.engine)
    run()
