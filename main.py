def quicksort(lista):

    # Si la lista tiene 0 o 1 elementos, ya está ordenada.
    if len(lista) <= 1:
        return lista
    
    # Se elige el primer elemento de la lista como pivote.
    pivote = lista[0]
    
    # Sublistas de elementos menores y mayores que el pivote.
    menores = [x for x in lista[1:] if x <= pivote]
    mayores = [x for x in lista[1:] if x > pivote]
    
    # Se ordenan las sublistas y se combinan con el pivote.
    return quicksort(menores) + [pivote] + quicksort(mayores)

# Prueba de la implementación
lista = [3, 6, 8, 10, 1, 2, 1]
lista_ordenada = quicksort(lista)
print("Lista original:", lista)
print("Lista ordenada:", lista_ordenada)
