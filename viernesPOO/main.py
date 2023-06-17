from cosas import Profesor, Alumno, AyudanteProfesor


def main():
    a1 = Alumno("Zabdiel",23,"316282893","ICO")
    print(a1)
    a1.nombre = "Emilio"
    print(a1)
    a2 = Alumno.constructor_defecto()
    print(a2)
    a2.nombre = "Emilio"
    print(a2)
    a2.dormir()

    print("-------PROFESOR------")
    prof1 = Profesor("Jesus",30+16,67546,"Ingenieria de software")
    print(prof1)
    prof1.dormir()

    print("-----AYUDANTE--------")
    ayudante = AyudanteProfesor("Adrian",20,"252525","ICO",232342,"Ing. de Software",4)
    print(ayudante)
    ayudante.dormir()
    ayudante.nombre="Abraham"
    ayudante.dar_clase("POO")
main()
