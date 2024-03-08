"""Configuracion de la conexion"""
from configparser import ConfigParser


def configuration(filename="database.ini", section="postgresql"):
    """create a parser"""
    parser = ConfigParser()
    # read config file
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
        return db  # Añade esta línea para devolver el diccionario completo
    else:
        raise ImportError(f"Section '{section}' not found in the '{filename}' file")
