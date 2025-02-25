# importar Tkinder para obtener la ruta de los archivos xml
from tkinter import filedialog, messagebox

# importar la libreria ElementTree
import xml.etree.ElementTree as ET

#importar la libreria Minidom
from xml.dom import minidom

def menu_principal():
    ruta = 'C:/Users/rossm/OneDrive/Escritorio/Clases/Unidad 3/entrada/reservaciones.xml'
    while True:
        print('--------- MENU PRINCIPAL ---------')
        print('- 1. Cargar XML                  -')
        print('- 2. Leer XML con miniDOM        -')
        print('- 3. Leer XML con ElementTree    -')
        print('- 4. Escribir XML con miniDOM    -')
        print('- 5. Escribir XML con ElementTree-')
        print('- 6. Salir                       -')
        print('----------------------------------')
        opcion = int(input('Seleccione una opción: '))
        match opcion:
            case 1:
                '''
                ruta = cargar_xml()
                if ruta == '':
                    messagebox.showerror('Error', 'No se ha seleccioando ningún archivo')
                else:
                    messagebox.showinfo("Exito", "Archivo cargado con éxito")
                    print(ruta)
                '''
                
            case 2:
                leerConMiniDOM(ruta)
            case 3:
                leerConET(ruta)
            case 4:
                pass
            case 5:
                pass
            case 6:
               pass
            case _:
               pass

def cargar_xml():
    ruta_archvo = filedialog.askopenfilename(title="Cargar archivo", filetypes=(("text files", "*.xml"), ("All files", "*.*")))
    return ruta_archvo

def leerConMiniDOM(ruta):
    #vamos a parser el archivo xml
    doc = minidom.parse(ruta)
    #obtener el elemento raiz
    root = doc.documentElement
    print(root.nodeName)
    #validar para diferenciar una etiqueta con otra
    if root.nodeName == 'libros':
        #vamos a obtener los nodos hijos de la raiz y retornar una lista
        libros = root.getElementsByTagName('libro')
        #recorremos los nodos de los libros
        for libro in libros:
            #Obtenemos el atributo
            id = libro.getAttribute('id')
            titulo = libro.getElementsByTagName('titulo')[0].firstChild.nodeValue
            autor = libro.getElementsByTagName('autor')[0].firstChild.nodeValue
            precio = libro.getElementsByTagName('precio')[0].firstChild.nodeValue
            imagen = libro.getElementsByTagName('imagen')[0].firstChild.nodeValue

            print('-'*20)
            print('ID:', id)
            print('Titulo:', titulo)
            print('Autor:', autor)
            print('precio:', precio)
            print('imagen:', imagen)

    elif root.nodeName == 'reservaciones':
        reservaciones = root.getElementsByTagName('reservacion')
        for reservacion in reservaciones:
            id = reservacion.getAttribute('id')
            descripcion = reservacion.getElementsByTagName('descripcion')[0].firstChild.data
            libro = reservacion.getElementsByTagName('libro')[0].firstChild.data
            usuario = reservacion.getElementsByTagName('usuario')[0].firstChild.data
            dia = reservacion.getElementsByTagName('dia')[0].firstChild.data
            hora = reservacion.getElementsByTagName('dia')[0].getAttribute('hora')
            print('-'*20)
            print('ID:', id)
            print('Descripción:', descripcion)
            print('Libro:', libro)
            print('Usuario:', usuario)
            print('Dia:', dia)
            print('Hora:', hora)

def leerConET(ruta):
    #primero parseamos el archivo xml
    tree = ET.parse(ruta)
    #obtenemos el elemento raiz 
    root = tree.getroot()
    #print(len(root))
    if root.tag == 'libros':
        for libro in root:
            id = libro.attrib['id']
            titulo = libro.find('titulo').text
            autor = libro.find('autor').text
            precio = libro.find('precio').text
            imagen = libro.find('imagen').text
            print('-'*20)
            print('ID:', id)
            print('Titulo:', titulo)
            print('Autor:', autor)
            print('Precio:', precio)
            print('Imagen:', imagen)
    elif root.tag == 'reservaciones':
        for reservacion in root:
            id = reservacion.attrib['id']
            descripcion = ''
            libro = ''
            usuario = ''
            dia = ''
            hora = ''
            for hijo in reservacion:
                match hijo.tag:
                    case 'descripcion':
                        descripcion = hijo.text
                    case 'libro':
                        libro = hijo.text
                    case 'usuario':
                        usuario = hijo.text
                    case 'dia':
                        dia = hijo.text
                        hora = hijo.attrib['hora']
            
            print('*'*20)
            print('ID:', id)
            print('Descripción:', descripcion)
            print('Libro:', libro)
            print('Usuario:', usuario)
            print('Día:', dia)
            print('Hora:', hora)
    


if __name__ == '__main__':
    menu_principal()

