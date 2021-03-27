

MATERIAS = 1



nombre = input("Nombre completo: ")
materia = input("nombre de la materia: ")
nota = input("nota: ")




contador = 1
sumatoria = 0
while contador <=5 MATERIAS:
    nombre_materia = input("Nombre de la materia {}: ".format(contador))
    calificacion = float(input("Calificación en {}: ".format(nombre_materia)))
    
    sumatoria = sumatoria + calificacion
    
    contador = contador + 1


contador = 2
sumatoria = 0
while contador <=5 MATERIAS:
    nombre_materia = input("Nombre de la materia {}: ".format(contador))
    calificacion = float(input("Calificación en {}: ".format(nombre_materia)))
    
    sumatoria = sumatoria + calificacion
    
    contador = contador + 1    



# Hacer cálculos e imprimir resultados
promedio = sumatoria / MATERIAS
print("""***** Resultados *****
Alumno: {} | {} {}
*******************************
* Promedio: {}
*******************************
""".format(nombre, matria, nota))