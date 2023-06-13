from cosas import Alumno

def main():
    """
    al1 = Alumno()
    print(al1)
    al2 = Alumno()
    print(al1.facultad)
    print(al2.facultad)
    print(Alumno.facultad)
    al1.facultad = "FES Aragón EDOMEX"
    print("-----")
    print(al1.facultad)
    print(al2.facultad)
    print(Alumno.facultad)
    print("-----Un vistazo a los objetos")
    print(vars(al1))
    print(vars(al2))
    al1.edad = 999
    """
    al1 = Alumno("Diego",19,"ICO")
    al2 = Alumno("Monste",20,"Derecho")
    al1.__edad = 33
    print(al1.__edad)

    print(vars(al1))
main()