# %%
# Importar librerias necesarias.
import pandas as pd 
import numpy as np

# %%
# Cargar los Datasets
# Ratins:
df1 = pd.read_csv(r"ratings\1.csv")
df2 = pd.read_csv(r"ratings\2.csv")
df3 = pd.read_csv(r"ratings\3.csv")
df4 = pd.read_csv(r"ratings\4.csv")
df5 = pd.read_csv(r"ratings\5.csv")
df6 = pd.read_csv(r"ratings\6.csv")
df7 = pd.read_csv(r"ratings\7.csv")
df8 = pd.read_csv(r"ratings\8.csv")




# %%
# Csv de plataformas:
amazon = pd.read_csv(r"amazon_prime_titles.csv")
disney = pd.read_csv(r"disney_plus_titles.csv")
hulu = pd.read_csv(r"hulu_titles.csv")
netflix = pd.read_csv(r"netflix_titles.csv")

# %% [markdown]
# Proceso de ETL:

# %%
amazon.head()

# %%
# ajustar los nombres de las id
amazon.show_id = "a" + amazon.show_id
disney.show_id = "d" + disney.show_id
hulu.show_id = "h" + hulu.show_id
netflix.show_id = "n" + netflix.show_id

# %%
# definir celdas NaN
amazon.rating.fillna("G", inplace=True)
disney.rating.fillna("G", inplace=True)
hulu.rating.fillna("G", inplace=True)
netflix.rating.fillna("G", inplace=True)

# %%
# reformatear a datetimes yyyy-mm-dd
amazon["date_added"] = pd.to_datetime(amazon["date_added"])
disney["date_added"] = pd.to_datetime(disney["date_added"])
hulu["date_added"] = pd.to_datetime(hulu["date_added"])
netflix["date_added"] = pd.to_datetime(netflix["date_added"])



# %%
# aplicar lower case a todo lo que sea texto
amazon = amazon.applymap(lambda s: s.lower() if type(s) == str else s)
disney = disney.applymap(lambda s: s.lower() if type(s) == str else s)
hulu = hulu.applymap(lambda s: s.lower() if type(s) == str else s)
netflix = netflix.applymap(lambda s: s.lower() if type(s) == str else s)


# %%
# convertir duration a dos columnas
amazon[["duration_int", "duration_type"]] = amazon['duration'].str.split(' ',expand=True)
disney[["duration_int", "duration_type"]] = disney['duration'].str.split(' ',expand=True)
hulu[["duration_int", "duration_type"]] = hulu['duration'].str.split(' ',expand=True)
netflix[["duration_int", "duration_type"]] = netflix['duration'].str.split(' ',expand=True)
# borrar la columna duration
amazon.drop('duration', axis=1, inplace=True)
disney.drop('duration', axis=1, inplace=True)
hulu.drop('duration', axis=1, inplace=True)
netflix.drop('duration', axis=1, inplace=True)  

# %%
#Funciones API
print(amazon.query('release_year == {year} and duration_type == {duration_type} and duration_int == @amazon["duration_int"].max()')["title"].iloc[0])
    


