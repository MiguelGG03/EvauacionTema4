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
    lista=[]
    for j in dict.items():
        aux=ArbolNodo()
        aux.letra,aux.fre=j[0],j[1]
        lista.append(aux)
    length = len(lista)
    for i in range(length - 1):
        swapped = False
        for j in range(length - 1 - i):
            if lista[j].fre > lista[j + 1].fre:
                swapped = True
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
        if not swapped:
            break
    for i in lista:
        print(f'{i.letra} , {i.fre}')
    return lista
    

if __name__=='__main__':
    dict={'A':0.2,'F':0.17,'1':0.13,'3':0.21,'0':0.05,'M':0.09,'T':0.15}
    orden(dict)
