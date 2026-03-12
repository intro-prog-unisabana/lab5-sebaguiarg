
def promedio_estudiante(calificaciones):
    """Definir el nombre de la funcion en base a la entrada en la lista notas"""
    if len(calificaciones) <= 0:
        print("Debes agregar las calificaciones")
    else:
        return float(sum(calificaciones)/len(calificaciones))