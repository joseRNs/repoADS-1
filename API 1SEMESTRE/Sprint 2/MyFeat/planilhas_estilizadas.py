import pandas as pd

df = pd.read_csv("data_tratada.csv", sep=';')
df = pd.DataFrame(df)
df.style.to_html

def df_formatado(DataFrame):
    DataFrame = df
    DataFrame = df.replace(True, "SIM").replace(False, "NÃO")
    return DataFrame
print(df_formatado(df))