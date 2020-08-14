# Importa as bibliotecas necessarioas
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

#melhorar a visualização
pd.set_option('max_columns',170)
%matplotlib inline
%config inlinebackend.figure_format = 'svg'

#Carrega um arquivo CSV
df = pd.read_csv("/content/datahackers-survey-2019-anonymous-responses.csv")

# extrair o nome da variável da tupla
df.columns = [eval(col)[1] for col in df.columns]

#cria um grafico que mostra os cientsitas de dados por estado
# countplot de estado onde mora - Analise de Cientitsa de dados por estado
plt.figure(figsize=(15,10))#Configura o tamanho da figura onde o grafico ficara
#variavel ax recebe um metodo countplot( sendo eixo x o estado, em que a coluna se e cientista de dados =1, ordenado por etsado)
ax = sns.countplot(x="living_state", data=df[df['is_data_science_professional'] == 1], order=df['living_state'].value_counts().index)
plt.title('Cientistas de Dados por Estado', size=14)#altera o titulo do grafico
plt.xlabel('Estados', size=12)
plt.show()#plota grafico

# lista as 5 primeiras linhas da tabela
df.head()
#Cria grafico que verifica cientista de dados por genero

# countplot de estado onde mora - Analise de Cientitsa de dados por estado
plt.figure(figsize=(8,6))#Configura o tamanho da figura onde o grafico ficara
#variavel ax recebe um metodo countplot( sendo eixo x o estado, em que a coluna se e cientista de dados =1, ordenado por etsado)
ax = sns.countplot(x="gender", data=df[df['is_data_science_professional'] == 1], order=df['gender'].value_counts().index)
plt.title('Divisao por Genero', size=14)#altera o titulo do grafico
plt.xlabel('Genero', size=12)
plt.show()#plota grafico
