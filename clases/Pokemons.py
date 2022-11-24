import pandas as pd

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
    data=leer_csv_pkemons(data)
    print(data.head())

if __name__=='__main__':
    main_ej2()