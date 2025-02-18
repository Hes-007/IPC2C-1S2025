#from Clases.Vehiculo import Vehiculo

#nuevo = Vehiculo("Toyota", "Corolla", 2020)
#uevo.informacionDetallada()

from Clases.Carro import Carro
from Clases.Moto import Moto
from Clases.Camion import Camion
from Clases.Concesionario import Concesionario
import time

sistema = Concesionario()

def agregarVehiculo():
   print("|             AGREGAR VEHICULO             |")
   print("|------------------------------------------|")
   print("| 1. Agregar Carro                         |")
   print("| 2. Agregar Moto                          |")
   print("| 3. Agregar Camion                        |")
   print("| 4. Volver                                |")
   print("|------------------------------------------|")
   print("Ingresa tu opcion: ")
   opcion = int(input("> "))
   match opcion:
      case 1:
         agregarCarro()
      case 2:
         agregarMoto()
      case 3:
         agregarCamion()
      case 4:
         print("Volviendo al menu principal...")
         time.sleep(1)
         print("")

def agregarCarro():
    print("|             AGREGAR CARRO              |")
    print("|----------------------------------------|")
    print("| Agrega el modelo del carro             |")
    modelo = input()
    print("| Agrega la marca del carro              |")
    marca = input()
    print("| Agrega el año del carro                |")
    año = int(input())
    print("| Agrega el numero máximo de pasajeros   |")
    pasajeros = int(input())

    nuevoCarro = Carro(marca, modelo, año, pasajeros)
    sistema.agregarVehiculo(nuevoCarro)
    print("|----------------------------------------|")
    print("|      Carro agregado exitosamente       |")
    print("|----------------------------------------|")
    time.sleep(1)
    print("")

def agregarMoto():
    print("|             AGREGAR MOTO               |")
    print("|----------------------------------------|")
    print("| Agrega el modelo de moto               |")
    modelo = input()
    print("| Agrega la marca de moto                |")
    marca = input()
    print("| Agrega el año de moto                  |")
    año = int(input())
    print("| Agrega el tipo de moto                 |")
    tipo = input()

    nuevaMoto = Moto(marca,modelo,año,tipo)
    sistema.agregarVehiculo(nuevaMoto)
    print("|----------------------------------------|")
    print("|       Moto agregada exitosamente       |")
    print("|----------------------------------------|")
    time.sleep(1)
    print("")

def agregarCamion():
    print("|             AGREGAR CAMION             |")
    print("|----------------------------------------|")
    print("| Agrega el modelo de camion             |")
    modelo = input()
    print("| Agrega la marca de camion              |")
    marca = input()
    print("| Agrega el año de camion                |")
    año = int(input())
    print("| Agrega la capacidad de camion          |")
    capacidad = float(input())

    nuevoCamion = Camion(marca, modelo, año, capacidad)
    sistema.agregarVehiculo(nuevoCamion)

    print("|----------------------------------------|")
    print("|     Camion agregado exitosamente       |")
    print("|----------------------------------------|")
    time.sleep(1)
    print("")

def mostrarVehiculosPorMarca():
    print("|             VEHICULOS POR MARCA        |")
    print("|----------------------------------------|")
    marca = input("Ingrese la marca del vehiculo: ")
    sistema.buscarPorMarca(marca)
    print("")

def eliminarVehiculo():
    print("|             ELIMINAR VEHICULOS         |")
    print("|----------------------------------------|")
    modelo = input("Ingrese el modelo del vehiculo: ")
    sistema.eliminarVehiculo(modelo)
    print("|----------------------------------------|")
    print("|     Vehiculo eliminado exitosamente    |")
    print("|----------------------------------------|")

def mantenerVehiculo():
    print("|             MANTENER VEHICULO         |")
    print("|----------------------------------------|")
    modelo = input("Ingrese el modelo del vehiculo: ")
    sistema.mantenerVehiculo(modelo)

def disponibilizarVehiculo():
    print("|        DISPONIBILIZAR VEHICULO         |")
    print("|----------------------------------------|")
    modelo = input("Ingrese el modelo del vehiculo: ")
    sistema.disponibilizarVehiculo(modelo)


def Menu():
    opcion = 0
    try:
       while opcion != 8:
        print("|             MENU PRINCIPAL             |")
        print("|----------------------------------------|")
        print("| 1. Agregar Vehiculo                    |")
        print("| 2. Mostrar Vehiculos                   |")
        print("| 3. Mostrar Vehiculos por Marca         |")
        print("| 4. Eliminar Vehiculo                   |")
        print("| 5. Mantener Vehiculo                   |")
        print("| 6. Disponibilizar Vehiculo             |")
        print("| 7. Salir                               |")
        print("|----------------------------------------|")
        print("Ingresa tu opcion: ")
        opcion = int(input("> "))
        match opcion:
           case 1:
              agregarVehiculo()
           case 2:
               sistema.mostrarVehiculos()
           case 3: 
               mostrarVehiculosPorMarca()
           case 4:
               eliminarVehiculo()
           case 5:
               mantenerVehiculo()
           case 6:
               disponibilizarVehiculo()
           case 7:
              print("Saliendo del sistema...")
              time.sleep(1)
              print("Adios!")
              break  
           case _:
              print("Opción no valida, por favor intente de nuevo")
    except:
       print("Ocurrio un error, por favor intente de nuevo")

if __name__ == "__main__":
    Menu()