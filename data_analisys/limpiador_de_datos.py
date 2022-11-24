import pandas as pd

def main_cleaner():
    data= pd.read_csv('data/pokemon.csv')
    print(data.columns)
    print(data.head(1))
    print(data['#'].head(10))
    cols=['#']
    data.drop(columns=cols)
    print(data.columns)





if __name__=='__main__':
    main_cleaner()