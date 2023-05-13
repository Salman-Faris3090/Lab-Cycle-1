import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
f=pd.read_csv('Iris.csv')

#to plot bar graph using matplotlib
f.Species.value_counts().plot(kind='bar',color=['y','orange','r'])
plt.xlabel('Species',fontsize=18)
plt.ylabel('Frequency of Species',fontsize=15)
plt.title("Frequency Bar Graph",fontsize=15)

#applying PCA 
import pandas as pd
f=pd.read_csv('Iris.csv')
#names=['SepalLength','SepalWidth', 'PetalLength', 'PetalWidth','Species']
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
#features = ['SepalLength','SepalWidth', 'PetalLength', 'PetalWidth']
X=f.iloc[:,1:5].values
#X=f.loc[:,features].values
#['Nameofspecies']
#X=f.loc[:,[['SepalLength'],['SepalWidth'],['PetalLength'], ['PetalWidth']]].values
#Y=f.iloc[:,5].values
X_axis=StandardScaler().fit_transform(X)
pca=PCA(n_components=2)
pc=pca.fit_transform(X_axis)
pf=pd.DataFrame(data=pc,columns=['Principal component 1','Principal component 2'])
final=pd.concat([pf,f['Species']],axis=1)
fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 component PCA', fontsize = 20)
targets = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
colors = ['b', 'r', 'g']
for target, color in zip(targets,colors):
    indicesToKeep = final['Species'] == target
    ax.scatter(final.loc[indicesToKeep, 'Principal component 1']
               , final.loc[indicesToKeep, 'Principal component 2']
               , c = color
               , s = 50)
ax.legend(targets)
ax.grid()

#Sepal length histogram
plt.figure(figsize=(10,10))
x=f.SepalLengthCm
plt.hist(x,bins=25,color='r')
plt.title("Sepal length in cm")
plt.xlabel("Sepal length")
plt.ylabel("Measure")

#Sepal width histogram
plt.figure(figsize=(10,10))
x=f.SepalWidthCm
plt.hist(x,bins=25,color='grey')
plt.title("Sepal Width in cm")
plt.xlabel("Sepal Width")
plt.ylabel("Measure")

#Petal Length histogram
plt.figure(figsize=(10,10))
x=f.PetalLengthCm
plt.hist(x,bins=25,color='green')
plt.title("Petal length in cm")
plt.xlabel("Petal Width")
plt.ylabel("Measure")

#Petal width histogram
plt.figure(figsize=(10,10))
x=f.PetalWidthCm
plt.hist(x,bins=25,color='orange')
plt.title("Petal Width in cm")
plt.xlabel("Petal Width")
plt.ylabel("Measure")
