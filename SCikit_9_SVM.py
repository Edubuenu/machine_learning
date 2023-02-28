
# importa os dataset que vem com o sklearn
from sklearn import datasets
#Carrega o digits dataset na variável digits
digits = datasets.load_digits()
#Mostra que há 1797 imagens (8 por 8 imagens para uma dimensionalidade de 64)
print("Forma de dados da imagem" , digits.data.shape)
#Mostra que há 1797 amostras (inteiros de 0 a 9)
print("Forma de dados do rótulo", digits.target.shape)
#Mostra os dados, as features de cada dígito manuscrito
print(digits.data)
print()
# Ou então
print(digits['data'])
print()
#Mostra as features
print(digits['target'])
print('-'*30)
print(digits.images[0])
print('-'*30)
import numpy as np 
import matplotlib.pyplot as plt
plt.figure(figsize=(20,4))
for index, (image, label) in enumerate(zip(digits.data[0:5], digits.target[0:5])):
    plt.subplot(1, 5, index + 1)
    plt.imshow(np.reshape(image, (8,8)), cmap=plt.cm.gray)
    plt.title('Target: {}\n'.format(label, fontsize = 20))
print(plt.show())
print()

#Importa o svm(support vector machine) do sklearn
from sklearn import svm
#Instancia um objeto svm em clf
clf = svm.SVC(gamma=0.001, C=100.)

print(clf.fit(digits.data[:-1], digits.target[:-1]))
#Mostra o array correspondente
print(clf.predict(digits.data[-1:]))

