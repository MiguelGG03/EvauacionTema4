class ArbolNodo(object):
    def __init__(self):
        self.info=None
        self.izq=None
        self.der=None

def crear_arbol(raiz):
    '''Crea el arbol binario'''

def bubble_sort(collection):
    length = len(collection)
    for i in range(length - 1):
        swapped = False
        for j in range(length - 1 - i):
            if collection[j] > collection[j + 1]:
                swapped = True
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
        if not swapped:
            break  # Stop iteration if the collection is sorted.
    return collection

'''
if __name__=='__main__':
    lista=[3,4,7,1,14,12,8,21,67,2]
    lista_ord=bubble_sort(lista)
    print(lista_ord)
'''