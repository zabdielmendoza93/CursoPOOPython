class Alumno:
    facultad = "FES Aragón"

    def __init__(self, nombre, edad, carrera ):
        self.__nombre = nombre
        self.__edad = edad
        self.__carrera = carrera

    def set_nombre(self, nom):
        self.__nombre = nom

    def get_nombre(self):
        return self.__nombre

    def set_edad(self,ed):
        if ed >=8 and ed < 120:
            self.__edad = ed
        else:
            print("Esa edad no es correcta")
            self.__edad = 0

    def get_edad(self):
        return self.__edad

    def set_carrera(self,carr):
        self.__carrera = carr

    def get_carrera(self):
        return self.__carrera

    def __str__(self):
        cadena = "Nombre: " + self.__nombre
        cadena = cadena + "\nEdad: " + str(self.__edad)
        cadena = cadena + "\ncarrera: " + self.__carrera
        return  cadena

    def estudiar(self, horas=1):
        print(f"El alumno {self.__nombre} esta estudiando por horas {horas}")

class Perro:
    reino = "Canino"
    def __init__(self,raza,edad,estatura):
        self.__raza = raza
        self.__edad = edad
        self.__estatura = estatura

    #método de accesso get
    @property
    def raza(self):
        return self.__raza

    #método de acceso set
    @raza.setter
    def raza(self, raza):
        self.__raza = raza

    #método de acceso edad
    @property
    def edad(self):
        return  self.__edad

    #método set edad
    @edad.setter
    def edad(self, edad):
        if edad > 0 and edad < 20:
          self.__edad = edad
        else:
            print("Esa no es una edad valida")
            self.__edad = 0

    #metodo de acceso estatura
    @property
    def estatura(self):
        return self.__estatura

    #método set estatura
    @estatura.setter
    def estatura(self,estatura):
        if estatura > 0.1 and estatura < 1.1:
            self.__estatura = estatura
        else:
            print("No way")
            self.__estatura = 0.1

    #método string
    def __str__(self):
        return f"""
        --------------------------------
        | Raza: {self.__raza}
        | Edad: {self.__edad}
        | Estatura: {self.__estatura}
        --------------------------------
        """

    #método para que el perro ladre n veces
    @staticmethod
    def ladra(veces):
        for i in range(veces):
            print("woof!")

    #método para verificar si es cachorro
    @staticmethod
    def es_cachorro(edad):
        return edad < 3

    #método para dormir al perro
    @staticmethod
    def dormir(veces =5):
        for n in range(veces):
            print(f"Dando vuelta {n + 1}")
        print("""
        zzz
        zzz
        zzz
        """)

    #método para crear un objeto perro si es grande
    @classmethod
    def perro_grande(cls,estatura):
        if estatura > 0.79:
            return cls("",0,estatura)