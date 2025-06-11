import os

#creacion de clases
#el doble guion bajo entrega la seguridad

class Contacto:
    def __init__(self, nombre:str, email:str, telefono:str) -> None:
        self.__nombre =  nombre
        self.__email = email
        self.__telefono = telefono
    
#metodos con el decorador property. el interprete trata la fucnion como una variable
    @property
    def nombre(self):
        return self.__nombre
    @property
    def email(self):
        return self.__email
    @property
    def telefono(self):
        return self.__telefono
    
#cambiar de formato de objeto a texto para que se pueda imprimir
    def __repr__(self):
        return repr([self.nombre,self.email,self.telefono])
    

    #(contacto) dice que hereada cosas de la clase contacto
class ContactoTrabajo(Contacto):

    #constructor del ContactoTrabajo()
    def __init__(self, nombre, email, telefono, empresa, oficio):
        # contructor de Contacto ()
        super().__init__(nombre, email, telefono)
        self.__empresa = empresa
        self.__oficio = oficio

    @property
    def empresa(self):
        return self.__empresa
    
    @property
    def oficio (self):
        return self.__oficio
    
    #esto es un metodo
    def __repr__(self):
        return repr([f"{self.nombre},{self.email},{self.telefono},{self.empresa},{self.oficio}"])

#esta clase     
class Manejador:

    def __init__(self):
        self.contactos:list[Contacto] = []

    def agregar_contacto(self, contacto:Contacto):
        self.contactos.append(contacto)

    def listar_contacto(self)-> list [Contacto]:
        return self.contactos
    
    def buscar_contacto(self, nombre):
        nombre_minuscula = nombre.lower()
        for i in self.contactos:
            if i.nombre.lower() == nombre_minuscula:
                return i
        return None
    
    def borrar_contacto(self,nombre):
        contacto=self.buscar_contacto(nombre)
        if contacto is not None:
            self.contactos.remove(contacto) 



class Consola_menu:
    #1 limpiar la consola
    #2 mostrar menu

    @staticmethod
    def limpiar_consola():
        #esta linea de menu es genericaa, siempre igual
        os.system("cls" if os.name =="nt" else "clear")

    @staticmethod
    def mostrar_menu():
        print("""
== menu contactos ==
1. agregar contacto
2. agrgar contacto trabajo
3. listar contactos   
4. buscar usuario
5. actualizar usuario
6.eliminar usuario
7. salir
""")

#no es necesario el print para usar la linea siguiente
#Consola_menu.limpiar_consola()

class Pedir_datos():

    @staticmethod
    def contacto_normal():
        nombre = input("nombre: ")
        email = input("email: ")
        telefono = input("telefono: ")
        return Contacto(nombre,email,telefono)
    
    @staticmethod
    def contacto_empresa():
        nombre = input("nombre: ")
        email = input("email: ")
        telefono = input("telefono: ")
        empresa = input("email: ")
        oficio = input("telefono: ")
        return Contacto(nombre,email,telefono,empresa,oficio)

class App:
    def __init__(self):
        self.manejador = Manejador()

    def run(self):
        while True:
            Consola_menu.limpiar_consola()
            Consola_menu.mostrar_menu()

            opcion = input("elige un opcion: ")

            if opcion == "1":
                c = Pedir_datos.contacto_normal()
                self.manejador.agregar_contacto(c)
                print("contacto agregado!!")
                input("enter oara continuar")
            elif opcion == "2":
                ct = Pedir_datos.contacto_empresa()
                self.manejador.agregar_contacto(ct)
                print("contacto agregado!!")
                input("enter oara continuar")

            elif opcion == "3":
                #listar contacto
                contactos = self.manejador.listar_contacto()
                #esto es para preguntar si hay contactos
                if contactos:
                    #cara cada nombre en contactos imprimir
                    for i in contactos:
                        print(i)
                else:
                    print("sin contactos")
            input("enter para continuar")


app = App()
app.run()