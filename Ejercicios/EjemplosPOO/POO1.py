class estudiante():
    def __init__(self, nombre, apellidos, grupo, edad, NIA):
        self.nombre= nombre
        self.apellidos= apellidos
        self.grupo= grupo
        self.edad= edad
        self.NIA= NIA

    def mostrar(self):
        print(f'Nombre: {self.nombre}')
        print(f'Nombre: {self.apellidos}')
        print(f'Nombre: {self.grupo}')
        print(f'Nombre: {self.edad}')
        print(f'Nombre: {self.NIA}')

    def Mayor(self):
        if self.edad>=18:
            return True
        if self.edad<18 and self.edad>0:
            return False


alumno1= estudiante("Nicolás", "Rotariu Peña", "B", 17, 10)
alumno1.mostrar()
print(alumno1.Mayor())
