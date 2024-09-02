numero_Calificaciones = int(input("¿Cuantas materias tienes? ")) 
    
if numero_Calificaciones < 0:
    raise ValueError("El numero no puede ser negativo")
try:
    calificaciones = []
    conteo = 0
    
    for i in range(1, numero_Calificaciones+1):
        x=int(input("Introduce tu primera calificacion: "))
        calificaciones.append(x)
        conteo += x
    print(conteo/numero_Calificaciones)
    print(calificaciones)
    
except ValueError:
    print("Debes introducir un numero valido")
    
except ZeroDivisionError:
    print("No sea wey no hay divicion en 0")