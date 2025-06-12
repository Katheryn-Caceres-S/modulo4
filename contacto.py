import os

#creacion de clases
#el doble guion bajo entrega la seguridad

class Contacto:
    def __init__(self, nombre:str, email:str, telefono:str) -> None:
        self._nombre =  nombre
        self._email = email
        self._telefono = telefono
    
#metodos con el decorador property. el interprete trata la fucnion como una variable
    @property
    def nombre(self):
        return self._nombre
    @property
    def email(self):
        return self._email
    @property
    def telefono(self):
        return self._telefono
    
#cambiar de formato de objeto a texto para que se pueda imprimir
    def __repr__(self):
        return repr([self.nombre,self.email,self.telefono])
    

    #(contacto) dice que hereada cosas de la clase contacto
class ContactoTrabajo(Contacto):

    #constructor del ContactoTrabajo()
    def __init__(self, nombre, email, telefono, empresa, oficio):
        # contructor de Contacto ()
        super().__init__(nombre, email, telefono)
        self._empresa = empresa
        self._oficio = oficio

    @property
    def empresa(self):
        return self._empresa
    
    @property
    def oficio (self):
        return self._oficio
    
    #esto es un metodo
    def __repr__(self):
        return repr([f"{self.nombre},{self.email},{self.telefono},{self.empresa},{self.oficio}"])

#esta clase  es el manejador   
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
    
    def actualizar_contacto(self, nombre , telefono , email):
        c = self.buscar_contacto(nombre)
        if c is not None:
        
            c._telefono = telefono
            c._email = email
            return c
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
        empresa = input("empresa: ")
        oficio = input("oficio: ")
        return ContactoTrabajo(nombre,email,telefono,empresa,oficio)

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
                
            elif opcion == "2":
                ct = Pedir_datos.contacto_empresa()
                self.manejador.agregar_contacto(ct)
                print("contacto agregado!!")


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
    

            elif opcion == "4":
                nombre = input("nombre contacto : ")
                c = self.manejador.buscar_contacto(nombre)
                if c:
                     print(c)
                else:
                    print("contacto no encontrado!")


            elif opcion == "5":
                nombre = input("nombre a actualizar")
                telefono = input("nuevo telefono")
                email = input("nuevo correo")
                c = self.manejador.actualizar_contacto(nombre, telefono, email)            
                print("contacto actualizado")

            elif opcion == "6":
                nombre = input("contacto a borrar")
                c = self.manejador.borrar_contacto(nombre)
                print("contacto borrado")

            elif opcion == "7":
                Consola_menu.limpiar_consola()
                print("adiossss")
                exit()
                

            else:
                print("opcion no valida")


app = App()
app.run()