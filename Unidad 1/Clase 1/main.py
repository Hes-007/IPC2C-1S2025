# Este es mi primer comentario.

'''
Este
Es un
Comentario
Multilínea
Salu2s
'''

"""
Este
Es otro
Comentario
Multilínea
Saludos 
"""

hola = "hola"

x = 10
y = 30
z = 40
a = True
b = False
c = 9.99
d = []
f = {}
g = None

# Asignación de variables
ipc2 = "IPC2"
ipc2 = "Introducción a la Programación y Computación 2"

variable = 1
variable = "1"
variable = True
variable = 4.5
variable = [1,2,3,4,5]

# Casteos

var1 = "1"
var2 = int(var1)
var3 = 4
var4 = str(var3)
var5 = "2.45"
var6 = float(var5)

# Expresiones Aritméticas

# Suma
suma = 10 + 10

# error
#concatenar = 3 + "hola"

# Correcto
#concatenar = str(3) + "hola"

#Resta
resta = 16-2

# Multiplicaicón 
multiplicar = 5 * 2

#División
division = 10/3

#Modulo
modulo = 4 % 2  # Resultado = 0

# Incremento y Decremento

#Incrementar
x += 1 # x = x + 1

#Disminuir
x += 1 # x = x - 1

# Expresiones Relacionales

#a > b
#c < d
#e >= f
#g <= h
#i == j
#k != l

# Expresiones Lógicas
#a and b # a && b
#b or c # b || c
#not d # !d

#Imprimir
print("Hola Mundo: :D", end = "")
print("Hola de nuevo")

#Input
#Tipado
#entrar = int(input("Ingrese algo: "))

#Sin tipar
#entrar = input("Ingrese su nombre")
#print("Hola, Tu nombre es:", entrar)

#input ("ingrese algo:")

# Condicioanles

# IF

condicional = 7
if condicional > 5:
    print("Es mayor a 5")
elif condicional == 5:
    print("Es igual a 5")
else:
    print("Es menor a 5")

# Match
dia = 0
match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miercoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sabado")
    case 7:
        print("Domingo")
    case _:
        print("No es un día de la semana")