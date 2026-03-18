
def promedio_estudiante(calificaciones):
    if calificaciones is None or len(calificaciones) == 0:
        return 0.0
    else:
        return float(sum(calificaciones)/len(calificaciones))

print(promedio_estudiante)