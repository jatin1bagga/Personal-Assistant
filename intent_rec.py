from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pickle

data = pd.read_csv("C:\\Users\\Jatin bagga\\Desktop\\ML\\JARVIS\\jarvis_commands_full.csv")
data['text'] = data['text'].str.lower() 

x = data['text']
y = data['label']


vectorizer = CountVectorizer()
xvec =vectorizer.fit_transform(x)

xtrain,xtest,ytrain,ytest = train_test_split(xvec , y , test_size= 0.2, random_state=42)
model = LogisticRegression()
model.fit(xtrain, ytrain)

pickle.dump(model, open('jarvis_model.pkl', 'wb'))
pickle.dump(vectorizer, open('jarvis_vectorizer.pkl', 'wb'))

print("Model trained and saved!")