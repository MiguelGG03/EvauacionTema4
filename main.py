from clases.ArbolHuffman import main_ej1
from clases.Pokemons import main_ej2

def main():
    pr1=input('Que ejercicio deseas ver (1,2,3): ')

    if pr1=='1':
        main_ej1()
    elif pr1=='2':
        main_ej2()
    elif pr1=='3':
        pass
        #main3()
    else:
        print('Respuesta incorrecta')

if __name__=='__main__':
    main()