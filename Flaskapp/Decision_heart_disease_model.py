
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split


# In[2]:


import os
os.listdir()


# In[3]:


def importData():
    data = pd.read_csv("heart.csv")
    #print("Data length:",len(data))
    #print("Data Shape:",data.shape)
    # print("Data:",data.head())
    return data


# In[4]:


data = pd.read_csv("heart.csv")
data.columns


# In[5]:


data.head()


# In[6]:


data.isnull().sum()


# In[71]:


def SplitData(data):
    #     Features = ['Age', 'Sex', 'ChestPainType', 'RestingBP', 'SerumCholestoral',
    #        'FastingBloodSugar', 'RestingECG', 'MaxHeartRate',
    #        'ExerciseInducedAngina', 'OldPeak', 'StSegSlope', 'NumOfMajorVessels',
    #        'Thal']
    X = data.drop(['target'], axis=1)
    Y = data['target']
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=100)
    return X, Y, X_train, X_test, y_train, y_test


# In[72]:


def train_model_gini(X_train, X_test, y_train):
    global clf_gini
    clf_gini = DecisionTreeClassifier(criterion="gini", max_depth=6, random_state=42)
    clf_gini.fit(X_train, y_train)
    return clf_gini


# In[73]:


def train_model_entropy(X_train, X_test, y_train):
    global clf_entropy
    clf_entropy = DecisionTreeClassifier(criterion="entropy", max_depth=6, random_state=42)
    clf_entropy.fit(X_train, y_train)
    return clf_entropy


# In[74]:


def Prediction(X_test, clf_gini, clf_entropy):
    y_predicted = clf_gini.predict(X_test)
    print("Predicted Values:")
    # print(y_predicted)
    return y_predicted


# In[75]:


def Accuracy(y_test, y_predicted):
    print("Confusion Metrix: ", confusion_matrix(y_test, y_predicted))
    print(" Classification Report:", classification_report(y_test, y_predicted))
    accuracy = accuracy_score(y_test, y_predicted)
    print(accuracy * 100)


# In[76]:


def main():
    data = importData()
    print(data.head())
    X, Y, X_train, X_test, y_train, y_test = SplitData(data)
    clf_gini = train_model_gini(X_train, X_test, y_train)
    clf_entropy = train_model_entropy(X_train, X_test, y_train)
    print("Gini Index Results:")
    y_gini_prediction = Prediction(X_test, clf_gini, clf_entropy)
    Accuracy(y_test, y_gini_prediction)
    print("Entropy Results:")
    y_entropy_prediction = Prediction(X_test, clf_entropy, clf_entropy)

    Accuracy(y_test, y_entropy_prediction)


main()


# In[77]:


from sklearn.externals.six import StringIO
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus
data = pd.read_csv("heart.csv")
X = data.drop(['target'], axis=1)
Y = data['target']
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)
Dtree = DecisionTreeClassifier(criterion="gini", max_depth=6, random_state=100)
Dtree.fit(X_train, y_train)
dot_data = StringIO()
export_graphviz(Dtree, out_file=dot_data, filled=True, rounded=True, special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
Image(graph.create_png())


# In[22]:


import pickle
model = pickle.dump(clf_gini, open('model.pkl', 'wb'))
#model1 = pickle.dump(clf_entropy,open('model1.pkl','wb'))


# In[15]:


model = pickle.load(open('model.pkl', 'rb'))
print(model.predict([[60, 1, 4, 130, 180, 0, 1, 109, 0, 0.4, 2, 2, 2]]))
