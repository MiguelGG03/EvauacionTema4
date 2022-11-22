class ArbolNodo(object):
    def __init__(self):
        self.letra=None
        self.fre=None
        self.val=None
        self.izq=None
        self.der=None

def junta_prim_nodos(lista):
    while(len(lista)>1):
        aux=ArbolNodo()
        aux.fre=lista[0].fre+lista[1].fre
        aux.letra=lista[0].letra+lista[1].letra
        aux.izq,aux.der=lista[0],lista[1]
        if(aux.izq.val==None):
            aux.izq.val='0'
        if(aux.der.val==None):
            aux.der.val='1'
        lista.pop(0)
        lista.pop(0)
        lista.append(aux)
        orden_nodos(lista)
    return lista


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

def orden_nodos(lista):
    '''Introduces una lista de nodos arbol y te la ordena por frecuencias'''
    length = len(lista)
    for i in range(length - 1):
        swapped = False
        for j in range(length - 1 - i):
            if lista[j].fre > lista[j + 1].fre:
                swapped = True
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
        if not swapped:
            break
    return lista

def orden_primero(dict):
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
    return lista

def busqueda(dato,raiz,codificado):
    codificado=''
    while(len(dato)>0):
        if(raiz.izq.letra==dato[0]):
            codificado=codificado+raiz.izq.val
            dato.pop(0)
            busqueda(dato,raiz,codificado)
        try:
            raiz.izq.letra.split()
            for letra in raiz.izq.letra.split():
                if(letra==dato[0]):
                    codificado=codificado+raiz.izq.val
                    raiz=raiz.izq
                    busqueda(dato,raiz,codificado)
        except:
            print('Llegaste a la hoja del arbol')
    return codificado

def main_ej1():
    dict={'A':0.2,'F':0.17,'1':0.13,'3':0.21,'0':0.05,'M':0.09,'T':0.15}
    lista=orden_primero(dict)
    for j in lista:
        print(f'CLAVE: {j.letra} ; FRECUENCIA: {j.fre}')
    lista=orden_nodos(lista)
    print('___________\n')
    lista_ord=junta_prim_nodos(lista)
    if(lista_ord[0].fre==1):
        print('Arbol creado')
        print(f'LETRAS RAIZ: {lista_ord[0].letra} ; FREC: {lista_ord[0].fre}')
        print(f'RAMA IZQ : {lista_ord[0].izq.letra} {lista_ord[0].izq.fre} ; RAMA DER : {lista_ord[0].der.letra} {lista_ord[0].der.fre}')
    print()
    print('____________\n')
    palabra='HOLA'
    for letra in palabra.split():
        print(letra)
    print([*palabra])
    '''
    cadena=input('Cadena de caracteres a codificar (AMFT013)\n>>> ')
    cadenasplited=cadena.split()
    resultado=busqueda(cadenasplited,lista_ord[0],'')
    print(resultado)
    '''




if __name__=='__main__':
    main_ej1()