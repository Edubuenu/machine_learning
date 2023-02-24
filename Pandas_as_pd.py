#importa a biblioteca pandas como pd
import pandas as pd
#importa o numpy como np
import numpy as np

#Cria um array numpy
data = np.array(['a','b','c','d'])

#Usa o array numpy criado acima para 
#gerar um objeto Series do pandas
s1 = pd.Series(data)

print(s1)

#Cria um array numpy
data2 = np.array(['a','b','c','d'])
s2 = pd.Series(data2, index = [70, 71, 72, 73])
print(s2)

data3 = {'a' : 0., 'b' : 1., 'c' : 2.}
s3 = pd.Series(data3)
print(s3)

data4 = {'a' : 0., 'b' : 1., 'c' : 2.}
s4 = pd.Series(data4, index = ['b','c','d','a'])
print(s4)

print('-'* 30)

s = pd.Series([1, 2, 3, 4, 5], index = ['a','b','c','d','e'])

#recupera um único elemento
print(s['a'])

#recupera vários elementos
print(s[['a','c','d']])

#recupera vários elementos
print(s['e']) #chave que n existe dá erro

print('*'*30)
#Vamos criar um DataFrame vazio
print('Vamos criar um DataFrame vazio')
df = pd.DataFrame()
print(df)
print()
data = [1, 2, 3, 4, 5]
df = pd.DataFrame(data)
print(df)

print()

data = [ ['Maria', 10], ['Carlos', 12], ['Paulo', 13] ]
df = pd.DataFrame(data, columns = ['Nome', 'Idade'])
print(df)

df = pd.DataFrame(data, columns = ['Nome', 'Idade'], dtype = float)
print(df)

data = {'Nome':['Marcos', 'Paula', 'Lia', 'Carlos'], 'Idade':[28, 34, 29, 42]}
df = pd.DataFrame(data)
print(df)

df = pd.DataFrame(data, index = ['rank1', 'rank2', 'rank3', 'rank4'])
print(df)

print('*'*30)

data = [ {'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20} ]
df = pd.DataFrame(data)
print(df)
print()
df = pd.DataFrame(data, index = ['primeiro', 'segundo'])
print(df)
print()
data = [ {'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20} ]

#Com dois índices de colunas, os valores são iguais aos das chaves do dicionário
df1 = pd.DataFrame(data, index = ['primeiro', 'segundo'], columns = ['a', 'b'])

#Com dois índices de colunas com um índice com outro nome
df2 = pd.DataFrame(data, index = ['primeiro', 'segundo'], columns = ['a', 'b1'])
print(df1)
print(df2)

print('Series')
print('*'*30)

dic = {'um' : pd.Series([1, 2, 3], index = ['a', 'b', 'c']),
   'dois' : pd.Series([1, 2, 3, 4], index = ['a', 'b', 'c', 'd'])}

df = pd.DataFrame(dic)
print(df)

dic = {'um' : pd.Series([1, 2, 3], index = ['a', 'b', 'c']),
   'dois' : pd.Series([1, 2, 3, 4], index = ['a', 'b', 'c', 'd'])}

df = pd.DataFrame(dic)
print(df ['um'])

print()


dic = {'um' : pd.Series([1, 2, 3], index = ['a', 'b', 'c']),
   'dois' : pd.Series([1, 2, 3, 4], index = ['a', 'b', 'c', 'd'])}

df = pd.DataFrame(dic)

# Adicionando uma nova coluna a um objeto DataFrame existente 
# com rótulo de coluna passando nova Series

print ("Adicionando uma nova coluna passando como Série:")
df['três'] = pd.Series([10, 20, 30], index = ['a','b','c'])
print(df)

print ("Adicionando uma nova coluna usando as colunas existentes no DataFrame")
df['quatro'] = df['um'] + df['três']

print(df)

print()

print('-'*30)

d = {'um' : pd.Series([1, 2, 3], index = ['a', 'b', 'c']), 
   'dois' : pd.Series([1, 2, 3, 4], index = ['a', 'b', 'c', 'd']), 
   'três' : pd.Series([10,20,30], index = ['a','b','c'])}

df = pd.DataFrame(d)
print ("Nosso dataframe é:")
print(df)

# usando a função del
print ("Excluindo a primeira coluna usando a função DEL:")
del df['um']
print(df)

# usando a função pop
print ("Excluindo outra coluna usando a função POP:")
df.pop('dois')
print(df)

dic = {'um' : pd.Series([1, 2, 3], index = ['a', 'b', 'c']), 
   'dois' : pd.Series([1, 2, 3, 4], index = ['a', 'b', 'c', 'd'])}

df = pd.DataFrame(dic)
print(df.loc['b'])


dic = {'um' : pd.Series([1, 2, 3], index = ['a', 'b', 'c']),
   'dois' : pd.Series([1, 2, 3, 4], index = ['a', 'b', 'c', 'd'])}

df = pd.DataFrame(dic)
print(df.iloc[2])

print()
df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])

df = df.append(df2)
print(df)

df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])

df = df.append(df2)

#Deleta as linhas com o rótulo 0
df = df.drop(0)

print(df)

