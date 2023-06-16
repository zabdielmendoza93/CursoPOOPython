from cosas import Libro, Autor, Persona, Alumno


def main():
    l1 = Libro.libro_planeta("El perfume", Autor("Patrick", "PS"), 1980)
    print(l1)
    l1.autor.pseudonimo = l1.autor.pseudonimo.lower()
    print(l1)
    print("------HERENCIA---------")
    a1 = Alumno("Zabdiel",23,"316282893","ICO",8.9)
    print(a1)
    a1.nombre = "Emilio"
    print(a1)

main()
