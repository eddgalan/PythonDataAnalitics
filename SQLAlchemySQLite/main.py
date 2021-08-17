import sqlite
from models import Producto

def run():
    pass

if __name__ == '__main__':
    sqlite.Base.metadata.create_all(sqlite.engine)
    run()
