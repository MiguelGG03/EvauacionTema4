class ArbolNodo(object):
    def __init__(self):
        self.letra=None
        self.fre=None
        self.izq=None
        self.der=None

def crear_arbol(raiz):
    '''Crea el arbol binario'''
    pass

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

def orden(dict):
    '''Introduces un diccionario y 
    devuelve una lista de nodos arbol con ramas none ordenado por frecuencias'''
    letras=[]
    lista=[]
    for j in dict.items():
        aux=ArbolNodo()
        aux.letra,aux.fre=j[0],j[1]
        lista.append(aux)
    for i in lista:
        print(i.letra)
        print(i.fre)
    '''
    for i in dict.keys():
        lista.append(dict[i])
    bubble_sort(lista)
    print(lista)
    '''

if __name__=='__main__':
    dict={'A':0.2,'F':0.17,'1':0.13,'3':0.21,'0':0.05,'M':0.09,'T':0.15}
    orden(dict)
