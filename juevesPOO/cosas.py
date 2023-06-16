class Autor:
    def __init__(self, nom, pseudo):
        self.__nombre = nom
        self.__pseudonimo = pseudo

    #acceso nombre
    @property
    def nombre(self):
        return self.__nombre

    #set nombre
    @nombre.setter
    def nombre(self, nom):
        self.__nombre = nom

    #acceso psudonimo
    @property
    def pseudonimo(self):
        return self.__pseudonimo

    #set pseudonimo
    @pseudonimo.setter
    def pseudonimo(self,pseudo):
        self.__pseudonimo = pseudo

    #toString

    def __str__(self):
        return f"Nombre: {self.__nombre} pseudonimo: {self.__pseudonimo}"

    #metodo escribir
    def escribir(self):
        print(f"{self.__pseudonimo} esta escribiendo su siguiente obra")

class Libro:

    def __init__(self,tit,aut,an,ed):
        self.__titulo = tit
        self.__autor = aut
        self.__anio = an
        self.__editorial = ed

    #método acceso titulo
    @property
    def titulo(self):
        return self.__autor

    #metodo set titulo
    @titulo.setter
    def titulo(self,tit):
        self.__titulo = tit

    #metodo acceso autor
    @property
    def autor(self):
        return self.__autor

    #metodo set autor
    @autor.setter
    def autor(self,aut):
        self.__autor = aut

    #metodo acceso año
    @property
    def anio(self):
        return self.__anio

    #metodo set año
    @anio.setter
    def anio(self,an):
        self.__anio = an

    #metodo acceso editorial
    @property
    def editorial(self):
        return self.__editorial

    #metodo set editorial
    @editorial.setter
    def editorial(self,ed):
        self.__editorial = ed

    #toString
    def __str__(self):
        return f"""
Titulo:     {self.__titulo}
Autor:      {self.__autor}
Año:        {self.__anio}
Editorial:  {self.__editorial}
"""

    @classmethod
    def libro_planeta(cls,titulo,autor,anio):
        return cls(titulo,autor,anio,"Planeta")

    def leer(self,minutos):
        print(f"Leyendo por {minutos} minutos")

class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nom):
        self.__nombre = nom

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, ed):
        self.__edad = ed

class Alumno(Persona):
    def __init__(self,nombre,edad,no_cuenta,carrera,promedio):
        super().__init__(nombre,edad)
        self.__numero_cuenta = no_cuenta
        self.__carrera = carrera
        self.__promedio = promedio

    def __str__(self):
        return  f"""
Nombre:     {self.nombre}
Edad:       {self.edad}
Cuenta:     {self.__numero_cuenta}
Carrera:    {self.__carrera}
Promedio:   {self.__promedio}
"""
