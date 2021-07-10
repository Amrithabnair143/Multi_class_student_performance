# Importing essential libraries
import numpy as np
import pandas as pd
import pickle

# Loading the dataset
df = pd.read_csv(r'C:\Users\sanje\Documents\python projects 2020\fisat\performance\student.csv')


# Model Building
from sklearn.model_selection import train_test_split
X = df.drop(columns='G3')
y = df['G3']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

# Creating Random Forest Model
from sklearn.ensemble import RandomForestClassifier, forest
classifier = RandomForestClassifier(n_estimators=20)
forest=classifier.fit(X_train, y_train)
print("Random Forest Train data Score" , ":" , forest.score(X_train, y_train) 
          , "," ,"Validation data Score" ,":" , forest.score(X_test, y_test))
# Creating a pickle file for the classifier
filename = r'C:\Users\sanje\Documents\python projects 2020\fisat\performance\RFmodel.pkl'
pickle.dump(classifier, open(filename, 'wb'))


from sklearn.tree import DecisionTreeClassifier
tree = DecisionTreeClassifier(min_samples_leaf=9,random_state=0)
tf=tree.fit(X_train, y_train)
print("Decisioin Tree Train data Score" , ":" , tf.score(X_train, y_train) 
          , "," , "Validation data Score" ,":" , tf.score(X_test, y_test))
# Creating a pickle file for the classifier
filename = r'C:\Users\sanje\Documents\python projects 2020\fisat\performance\DTmodel.pkl'
pickle.dump(tree, open(filename, 'wb'))



from sklearn.ensemble import AdaBoostClassifier
ada = AdaBoostClassifier(n_estimators=2)
af = ada.fit(X_train, y_train)
print("Ada Boost Train data Score" , ":" , af.score(X_train, y_train) 
        , "," ,"Validation data Score" ,":" , af.score(X_test, y_test))
filename = r'C:\Users\sanje\Documents\python projects 2020\fisat\performance\GBmodel.pkl'
pickle.dump(ada, open(filename, 'wb'))


from xgboost import XGBClassifier
model = XGBClassifier()
model = XGBClassifier(learning_rate=0.1,n_estimators=80)
mf = model.fit(X_train,y_train)
print("XGBoost Train data Score" , ":" , mf.score(X_train, y_train) 
        , "," ,"Validation data Score" ,":" , mf.score(X_test, y_test))
filename = r'C:\Users\sanje\Documents\python projects 2020\fisat\performance\XGBmodel.pkl'
pickle.dump(model, open(filename, 'wb'))
'''from sklearn.svm import SVC
svc = SVC()
svc.fit(X_train, y_train)
# Creating a pickle file for the classifier
filename = r'C:\Users\sanje\Documents\python projects 2020\fisat\dropout\SVMmodel.pkl'
pickle.dump(svc, open(filename, 'wb'))


from sklearn.linear_model import LogisticRegression
lr =  LogisticRegression()
lr.fit(X_train,y_train)
filename = r'C:\Users\sanje\Documents\python projects 2020\fisat\dropout\LRmodel.pkl'
pickle.dump(lr, open(filename, 'wb'))'''