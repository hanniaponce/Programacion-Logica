#Dominio
D = {
    "Estudiantes": {
        "Ana": ["Programacion", "Redes"],
        "Hannia": ["Calculo"],
        "Dora":["Ingles"]
    },

    "Profesores": {
        "Lopez": ["Programacion"],
        "Torres": ["Calculo"],
        "Garcia": ["Redes"]

    },

    "Materias": [

        "Programacion",
        "Calculo",
        "Redes",
        "Ingles"
    ],

    "Carreras": [
        "Sistemas",
        "Contabilidad"
    ],

    "Semestres": [
        "Primero",
        "Septimo"
    ]

}
#1. Estudiante(x)
#Estudiante(x): x es un estudiante.
def Estudiante(x):
    for Estudiantes in D["Estudiantes"].items():
        if Estudiantes[0] == x:
            return True
    return False
print("ESTUDIANTES")
print(Estudiante("Ana"))
print(Estudiante("Lopez"))

#2. Profesor(x)
#Profesor(x): x es un profesor.
def Profesor(x):
 for Profesores in D["Profesores"].items():
        if Profesores[0] == x:
            return True
 return False
print("PROFESORES")
print(Profesor("Lopez"))
print(Profesor("Ana"))

#3. Materia(x)
#Materia(x): x es una materia.
def Materia(x):
    for Materias in D["Materias"]:
        if Materias == x:
            return True
    return False

print("MATERIAS")
print(Materia("Programacion"))
print(Materia("Lopez"))


#4. Carrera(x)
#Carrera(x): x es una carrera.
def Carrera(x):
    for Carreras in D["Carreras"]:
        if Carreras == x:
            return True
    return False

print("CARRERAS")
print(Carrera("Sistemas"))
print(Carrera("Programacion"))


#5. Semestre(x)
#Semestre(x): x es un semestre.
def Semestre(x):
    for Semestres in D["Semestres"]:
        if Semestres == x:
            return True
    return False

print("SEMESTRES")
print(Semestre("Septimo"))
print(Semestre("Programacion"))     

#6. Cursa(x,y)
#Cursa(x,y): x cursa la materia y.
def Cursa(x,y):
    for Estudiante, Materia in D["Estudiantes"].items():
        if Estudiante == x:
             if y in Materia:
                  return True
    return False
print("CURSA")
print(Cursa("Ana", "Programacion"))
print(Cursa("Ana", "Calculo"))

#7. Imparte(x,y)
#Imparte(x,y): x imparte la materia y.
def Imparte(x,y):
    for Profesor, Materia in D["Profesores"].items():
         if Profesor == x:
              if y in Materia:
                   return True
    return False
print("IMPARTE")
print(Imparte("Lopez", "Programacion"))
print(Imparte("Lopez", "Calculo"))

         