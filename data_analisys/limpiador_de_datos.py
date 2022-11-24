import pandas as pd

def main_cleaner():
    data= pd.read_csv('data/pokemon.csv')
    print(data.columns)
    print(data.head(1))





if __name__=='__main__':
    main_cleaner()