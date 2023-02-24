#Vamos importar o sklearn
from sklearn import datasets
#Agora vamos carregar a base de dados das íris de flores
iris = datasets.load_iris()
print(type(iris))
#Dê uma primeira olhada nos dados
#Cada linha é uma observação (também conhecida como: amostra, exemplo, instância, registro)
#Cada coluna é um recurso (também conhecido como: feature, preditor, atributo, variável independente, entrada, regressor, covariável)
print(iris.data)
print('-'*40)
#Imprima os nomes dos quatro recursos (features)
print(iris.feature_names)
#Liste as classes alvo da classificação
print(list(iris.target_names))
#O comando a seguir imprime inteiros representando as espécies de cada observação: 0, 1 e 2 representam espécies diferentes.
print(iris.target)
print('Type data')
print(type(iris.data))
print('Type target')
print(type(iris.target))
print('_-' * 20)
#Verifique o formato das features ( primeira dimensão = número de observações, segunda dimensão = número de features )
print(iris.data.shape)
#numero de observacoes
print(iris.target.shape)
#Armazena a matriz de recurso (feature) em “x”
x = iris.data
#Armazena o vetor de resposta em “y”
y = iris.target
#Primeira dimensão = (LINHAS) ou seja, número de observações.
#Segunda dimensões = (COLUNAS) ou seja, número de features.
print(x.shape)
#Verifique a forma da resposta (dimensão única correspondente ao número de observação)
print(y.shape)
print(y.reshape(y.shape[0],-1))
print(y.shape)
print('Gráfico de dispersão com o conjunto de dados Iris')
featuresAll=[]
features = iris.data[: , [0,1,2,3]]
print(features.shape)
print(iris.feature_names)
print('-' * 40)
#Toda observação será anexada na lista assim que for lida.
#Um loop for é usado para o processo de iteração.
#Para cada linha lida, os valores das features são somados.
for observation in features:
    featuresAll.append([observation[0] + observation[1] + observation[2] + observation[3]])
print(featuresAll)
print('_'*40)
import matplotlib.pyplot as plt
plt.scatter(featuresAll, y, color='red', alpha =1.0)
plt.rcParams['figure.figsize'] = [10,8]
plt.title('Iris Dataset scatter Plot')
plt.xlabel('Features')
plt.ylabel('Targets')
print('Gráfico')
print(plt.show())
print('fim do gráifco')
print('#'*30)
#Encontrando o relacionamento entre o comprimento e a largura da sépala
sepal_len = []
sepal_width = []
for feature in features:
    sepal_len.append(feature[0]) #Comprimento da sépala
    sepal_width.append(feature[1]) #Largura da sépala

groups = ('Iris-setosa','Iris-versicolor','Iris-virginica')
colors = ('blue', 'green','red')
data = ((sepal_len[:50], sepal_width[:50]), (sepal_len[50:100], sepal_width[50:100]), 
        (sepal_len[100:150], sepal_width[100:150]))


for item, color, group in zip(data, colors, groups): 
    #item = (sepal_len[:50], sepal_width[:50]), (sepal_len[50:100], sepal_width[50:100]), 
    #(sepal_len[100:150], sepal_width[100:150])
    x0, y0 = item
    plt.scatter(x0, y0,color=color,alpha=1)
    plt.title('Iris Dataset scatter Plot')

plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
print(plt.show())
print('-'*30)
#Encontrando o relacionamento entre o comprimento e a largura da pétala
petal_len = []
petal_width = []
for feature in features:
    petal_len.append(feature[2]) #Comprimento da pétala
    petal_width.append(feature[3]) #Largura da pétala
groups = ('Iris-setosa','Iris-versicolor','Iris-virginica')
colors = ('blue', 'green','red')
data = ((petal_len[:50], petal_width[:50]), (petal_len[50:100], petal_width[50:100]), 
        (petal_len[100:150], petal_width[100:150]))

for item, color, group in zip(data,colors,groups): 
    #item = (petal_len[:50], petal_width[:50]), (petal_len[50:100], petal_width[50:100]), 
    #(petal_len[100:150], petal_width[100:150])
    x0, y0 = item
    plt.scatter(x0, y0,color=color,alpha=1)
    plt.title('Iris Dataset scatter Plot')

plt.xlabel('Petal length')
plt.ylabel('Petal width')
print(plt.show())

