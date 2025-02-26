class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoble:
    def __init__(self):
        self.primero = None
        self.ultimo = None  # Agregar puntero al último nodo
        self.largo = 0
    
    def insertar(self, dato):
        nodo = Nodo(dato)
        if self.primero is None:  # Si la lista está vacía
            self.primero = nodo
            self.ultimo = nodo  # El último nodo es el primero
        else:
            self.ultimo.siguiente = nodo  # El siguiente del último nodo apunta al nuevo
            nodo.anterior = self.ultimo  # El anterior del nuevo nodo es el último
            self.ultimo = nodo  # Actualizamos el último nodo
        self.largo += 1

    def cambiarEstadoInerte(self, posicion):
        actual = self.primero
        while actual:
            if actual.dato.getPosicion() == posicion:
                actual.dato.setInerte(True)
                return True
            actual = actual.siguiente
        return False

    def recorrer(self):
        actual = self.primero
        # Recorrer en una dirección (hacia adelante)
        while actual:
            print(actual.dato)
            actual = actual.siguiente

        # Si quieres recorrer hacia atrás, aquí lo puedes hacer sin recorrer hacia adelante primero
        actual = self.ultimo
        while actual:
            print(actual.dato)
            actual = actual.anterior

    def datos(self):
        return self.primero

    def longitud(self):
        return self.largo
    