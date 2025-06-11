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