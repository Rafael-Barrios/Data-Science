""" Este algoritmo nos facilita el ordenamiento
    de los ítems de una lista, de menor a mayor """

import random

def ordenamiento_por_mezcla(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        
        print (izquierda, '*' * 5, derecha)

        # Se hace la llamada de manera recursiva de cada mitad
        ordenamiento_por_mezcla(izquierda)
        ordenamiento_por_mezcla(derecha)

        # Iteradores para las listas necesarias (3)
        i = 0
        j = 0

        # En esta lista se genera para los ítems ya organizados
        k = 0

        # Aplicamos los bucles comparativos de las diferentes listas
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                # Comparado el valor menor se procede a ubicar en la lista k
                lista[k] = izquierda[i]
                i += 1
            else:
                # Al no ser True la primera comparación se ubica esta asignación en la lista k
                lista[k] = derecha[j]
                j += 1
            
            # Se cierra el incremento de k para evitar que sea infinito el bucle
            k += 1

        """ Aquí se confirma la organización realizada en el bucle anterior,
            y si es necesario se reorganizan los ítems según su valor """
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

            print (f'Se comparan y ordenan las listas resultantes {izquierda} y {derecha}')
            print (lista) # Se muestra como va quedando la lista k
            print ('*' * 20)

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

            print (f'Se comparan y ordenan las listas resultantes {izquierda} y {derecha}')
            print (lista) # Se muestra como va quedando la lista k
            print ('*' * 20)

    return lista

if __name__ == '__main__':

    tamano_de_lista = int(input('\n¿Cúantos ítems quieres en la lista?: '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    print ('*' * tamano_de_lista * 10)
    print (f'\nLa lista aleatoria es: {lista} \n')
    print ('*' * tamano_de_lista * 10)
    
    lista_ordenada = ordenamiento_por_mezcla(lista)
    print ('*' * tamano_de_lista * 10)
    print (f'\nLa lista ordenada es: {lista_ordenada} \n')
    print ('*' * tamano_de_lista * 10)

