from nodo import Nodo

class ListaSimple:
    def __init__(self):
        self.primero = None
        self.tamanio = 0

    #len(lista)
    def __len__(self):
        return self.tamanio

    def insertar(self, valor):
        #Primero creamos el nodo
        nuevo = Nodo(valor) # puede ser un valor, un numero, objeto, etc. 
        #Verificamos si la lista esta vacía
        if self.primero == None:
            self.primero = nuevo
            #Si la lista no esta vacía
        else:
            actual = self.primero
            #Recorremos
            while actual != None:
                if actual.siguiente == None:
                    actual.siguiente = nuevo
                    break
                actual = actual.siguiente

    def imprimirLista(self):
        actual = self.primero
        while actual != None:
            print(actual.valor)
            actual = actual.siguiente #Acá se reccore la flechita


