from cosas import Alumno
from cosas import Perro
def main():
    #ALUMNO
    al1 = Alumno("jose",19,"ICO")
    print(vars(al1))
    al1.__nombre = "Diego"
    print(vars(al1))
    al1.set_nombre("Maria")
    print(vars(al1))
    print("----TO STRING----")
    print(al1)
    al1.estudiar(8)

    #PERRO
    perro1 = Perro("Poddle",2,0.35)
    print(vars(perro1))
    perro1.raza= "De la calle"
    print(vars(perro1))
    perro1.__raza = "Otra"
    print(vars(perro1))
    print(perro1)
    Perro.ladra(5)
    Perro.dormir(4)
    print(Perro.es_cachorro(3))
    danes = Perro.perro_grande(0.8)
    print(danes)
main()