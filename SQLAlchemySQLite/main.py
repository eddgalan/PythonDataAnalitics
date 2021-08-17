import sqlite
from models import Producto

def run():
    # ..:: Insertar Datos ::..
    prod1 = Producto('Arroz', 1.25)
    prod2 = Producto('Tacos', 2.50)
    prod3 = Producto('Pan', 0.50)
    sqlite.session.add(prod1)
    sqlite.session.add(prod2)
    sqlite.session.add(prod3)
    sqlite.session.commit()
    print("Se agregó un nuevo registro. ID: " + str(prod1.id))
    print("Se agregó un nuevo registro. ID: " + str(prod2.id))
    print("Se agregó un nuevo registro. ID: " + str(prod3.id))
    # ..:: Consulta de Datos ::..
    ob = sqlite.session.query(Producto).get(1)
    print("Producto con Id = 1: " + str(ob))

    productos = sqlite.session.query(Producto).all()
    print("Todos los productos: " + str(productos))

    primer_producto = sqlite.session.query(Producto).first()
    print("Primer resultado del Query: " + str(primer_producto))

    num_productos = sqlite.session.query(Producto).count()
    print("Num de Productos: " + str(num_productos))

    arroz = sqlite.session.query(Producto).filter_by(nombre='Arroz')
    print("Query : " + str(arroz))

    arroz = sqlite.session.query(Producto).filter_by(nombre='Arroz').first()
    print("Producto arroz : " + str(arroz.id))

    mayor_1 = sqlite.session.query(Producto).filter(Producto.precio > 1).all()
    print("Productos con precio mayor a 1: " + str(mayor_1))

    # ..:: Actualizar un registro ::..
    obj1 = sqlite.session.query(Producto).get(1)
    obj1.nombre = "Pollo Frito"
    sqlite.session.commit()
    print("Registro actualizado")
    productos = sqlite.session.query(Producto).all()
    print("Todos los productos: " + str(productos))

if __name__ == '__main__':
    sqlite.Base.metadata.drop_all(sqlite.engine) # Límpia la base de datos (La elimina)
    sqlite.Base.metadata.create_all(sqlite.engine)
    run()
