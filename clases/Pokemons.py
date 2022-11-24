import pandas as pd
class nodoRaiz(object):
    
    def __init__(self):
        self.nombre=None
        self.numero=None
        self.tipo=None

class Pokemon(object):

    def __init__(self):
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


def leer_csv_pkemons(variable):
    variable=pd.read_csv('data/pokemon.csv')
    return variable

#Name,Type 1,Type 2,Total,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed,Generation,Legendary

def main_ej2():
    data=None
    pokemons_lst=[]
    data=leer_csv_pkemons(data)
    for i in range(len(data)):
        pokemon=Pokemon()
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










if __name__=='__main__':
    main_ej2()