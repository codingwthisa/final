import pickle

def guardar_datos(clientes):
    with open('clientes.pickle', 'wb') as f:
        pickle.dump(clientes, f)

def cargar_datos():
    try:
        with open('clientes.pickle', 'rb') as f:
            clientes = pickle.load(f)
    except FileNotFoundError:
        clientes = {}
    return clientes



