def busqueda_binaria(arr: List, target):
    izquierda, derecha = 0, len(arr) - 1
    while izquierda <= derecha:
        medio = izquierda + (derecha - izquierda) // 2
        if arr[medio] == target:
            return medio
        elif arr[medio] < target:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1
