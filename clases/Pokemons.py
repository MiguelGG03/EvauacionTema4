import pandas as pd
class nodoRaiz(object):

    def __init__(self):
        self.nombre=None
        self.numero=None
        self.tipo=None

class Pokemon(object):

    def __init__(self):
        self.id=None
        self.name=None
        self.type1=None
        self.type2=None
        self.total=None
        self.hp=None
        self.attack=None
        self.defense=None
        self.sp_atk=None
        self.sp_def=None
        self.speed=None
        self.generation=None
        self.legendary=None

    def __str__(self):
        print(f'Nombre > {self.name} \n'
             f'ID > {self.id} \n'
             f'Tipo 1 > {self.type1}\n'
             f'Tipo 2 > {self.type2} \n'
             f'HP > {self.hp} \n'
             f'Ataque > {self.attack} \n'
             f'Defensa > {self.defense} \n'
             f'Ataque Especial > {self.sp_atk} \n'
             f'Defensa Especial > {self.sp_def} \n'
             f'Velocidad > {self.speed} \n'
             f'Generacion > {self.generation} \n'
             f'Legendario > {self.legendary} \n')
        


def leer_csv_pkemons(variable):
    variable=pd.read_csv('data/pokemon.csv')
    return variable

#ID,Name,Type 1,Type 2,Total,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed,Generation,Legendary

def main_ej2():
    data=None
    pokemons_lst=[]
    data=leer_csv_pkemons(data)
    for i in range(len(data)):
        pokemon=Pokemon()
        pokemon.id=data['#'].iloc[i]
        pokemon.name=data.Name.iloc[i]
        pokemon.type1=data['Type 1'].iloc[i]
        pokemon.type2=data['Type 2'].iloc[i]
        pokemon.total=data.Total.iloc[i]
        pokemon.hp=data.HP.iloc[i]
        pokemon.attack=data.Attack.iloc[i]
        pokemon.defense=data.Defense.iloc[i]
        pokemon.sp_atk=data['Sp. Atk'].iloc[i]
        pokemon.sp_def=data['Sp. Def'].iloc[i]
        pokemon.speed=data.Speed.iloc[i]
        pokemon.generation=data.Generation.iloc[i]
        pokemon.legendary=data.Legendary.iloc[i]
        pokemons_lst.append(pokemon)
    tree=nodoRaiz()
    tree.nombre=pokemons_lst
    tree.numero=pokemons_lst
    tree.tipo=pokemons_lst
    pr1=input('Que tipo de busqueda desea hacer\n(1 - Nombre)\n(2 - Numero)\n(3 - Tipo)\n>>>')
    if(pr1=='1'):
        pr2=input('Ingrese el nombre del pokemon que desea buscar\n>>>')
        for i in range(len(tree.nombre)):
            if(tree.nombre[i].name==pr2):
                print()
                tree.nombre[i].__str__()









if __name__=='__main__':
    main_ej2()