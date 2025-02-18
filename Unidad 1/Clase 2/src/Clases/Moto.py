from Clases.Vehiculo import Vehiculo

class Moto(Vehiculo):
    def __init__(self, marca, modelo, anio, tipo):
        super().__init__(marca, modelo, anio)
        self.tipo = tipo    

    def informacionDetallada(self):
        print(f"-"*63)
        print(f"|{"Moto":^61}|")
        print(f"|"+"-"*30 + "|" +"-"*30+"|")
        print(f"|{"Marca":<30}|{self.marca:<30}|")
        print(f"|{"Modelo":<30}|{self.modelo:<30}|")
        print(f"|{"Año":<30}|{self.anio:<30}|")
        print(f"|{"Disponible":<30}|{self.disponible:<30}|")
        print(f"|{"Tipo":<30}|{self.tipo:<30}|")
        print(f"-"*63)

    #Encapsulamiento
    def getTipo(self):
        return self.tipo
    
    def setTipo(self, tipo):
        self.tipo = tipo