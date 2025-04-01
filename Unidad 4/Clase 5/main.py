#Element Tree
import xml.etree.ElementTree as ET
# Importar Tkinter para obtener la ruta de los archivos XML
from tkinter import filedialog, messagebox
from clases.usuario import Usuario
from estructuras.lista_simple.listaSimple import ListaSimple
lista_usuarios = ListaSimple()


def menu():
    opcion = 0
    while True:
        print('------------LISTAS-------------')
        print('1. Carga masiva')
        print('2. Ver lista simple enlazada')
        print('3. Ver lista doblemente enlazada')
        print('4. Obtener libro')
        print('5. Obtener usuario')
        print('6. Validar que tipo es')
        print('7. Salir')
        opcion = input('Ingrese la opción que desee: ')
        if opcion == '1':
            carga_masiva()
        elif opcion == '2':
            lista_usuarios.imprimirLista()
        elif opcion == '3':
            pass
        elif opcion == '4':
            pass
        elif opcion == '5':
            id_user = input('Ingrese el ID del usuario: ')
            usuario = lista_usuarios.obtenerUsuario(id_user)
            if usuario != None:
                print(str(usuario))
            else:
                print("No se encontró el usuario")
        elif opcion == '6':
            pass
        elif opcion == '7':
            break
        else:
            print('Opción no válida')

def carga_masiva():
    ruta = filedialog.askopenfilename(title="Cargar Archivo", filetypes=(('Text files', '*.xml'), ('All files','*.*')))
   
    tree = ET.parse(ruta)
    root = tree.getroot()

    if root.tag == 'usuarios':
        for usuario in root:
            id = usuario.attrib['id']
            password = usuario.attrib['password']
            nombre = ''
            edad = ''
            correo = ''
            telefono = ''
            for hijo in usuario:
                if hijo.tag == 'nombre':
                    nombre = hijo.text
                elif hijo.tag == 'edad':
                    edad = hijo.text
                elif hijo.tag == 'email':
                    correo = hijo.text
                elif hijo.tag == 'telefono':
                    telefono = hijo.text
            nuevo = Usuario(id,password,nombre,edad,correo,telefono)
            lista_usuarios.insertar(nuevo)


if __name__ == '__main__':
    menu()