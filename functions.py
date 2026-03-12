notas = [85, 92, 78]
def promedio(notas):
    """Definir el nombre de la funcion en base a la entrada en la lista notas"""
    if len(notas) <= 0:
        print("Debes incluir las notas")
    else:
        return sum(notas)/len(notas)

prom = (promedio(notas))
print(prom)