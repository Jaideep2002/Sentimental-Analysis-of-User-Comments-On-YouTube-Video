# data processing packages
import warnings
import time
import os
import sys
import csv
import io
import pandas as pd
import numpy as np
from nltk.corpus import subjectivity
from nltk.corpus import stopwords
import math
import matplotlib.pyplot as plt
# NLP packages
from nltk.translate import metrics
from textblob import TextBlob as tb
from textblob import Word
from mlxtend.plotting import plot_confusion_matrix

pd.set_option('display.max_colwidth', 200)


print("\n")

gen = ' ********************* TEXTBLOB COMMENT ANALYZER *********************'
for i in gen:
    print (i, end='')
    sys.stdout.flush()
    time.sleep(0.05)
print("\n")

gen= '****************************************************************************************************************************************'
for i in gen:
    print(i, end='')
    sys.stdout.flush()
    time.sleep(0.05)
print()
# from wordcloud import WordCloud

# to avoid the warnings in the program
warnings.filterwarnings("ignore")

# Importing Youtube comments data
db = pd.read_csv('raw.csv',encoding='cp1252',error_bad_lines=False) # opening the file comments

print(db.shape)

# calculate the sentiment polarity


polarity_Score = []

for i in range(0,db.shape[0]):
    score = tb(db.iloc[i][0].lower())     # going to the review column and then next location of the dataframe
    score1 = score.sentiment[0]  # for each review we are finding the score
    polarity_Score.append(score1)   # we are appending the polarity score to the list


db = pd.concat([db, pd.Series(polarity_Score)], axis=1)
# adding the polarity score column to the dataframe
print(db.head(10))

neutral, negative, positive = 0, 0, 0

for i in polarity_Score:
    if i == 0:
        neutral = neutral + 1

    elif i > 0:
        positive = positive + 1

    elif i < 0:
        negative = negative + 1


print()
total = positive + negative + neutral
positive1 = (positive/total)*100
negative1 = (negative/total)*100
neutral1 = (neutral/total)*100

print(" "*30,positive1, " % comments are positive")
print()
print(" "*30,negative1," % comments are negative")
print()
print(" "*30,neutral1," % comments are neutral")
print()
gen= ' ********************************************************************'
for i in gen:
    print(i, end='')
    sys.stdout.flush()
    time.sleep(0.05)
print()
if positive1 >= (neutral1 + negative1 + 10) :
    print(" ==> GREAT JOB!! You got positive feeback.")

elif negative1>= (neutral1 + positive1 + 10):
    print(" ==> SORRY!! You got negative feedback.")

else :
    print(" ==> NICE TRY!! You got neutral feedback.")

print("*"*50)

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
nb_samples = 1000
x, y = make_classification(n_samples=nb_samples, n_features=2, n_informative=2, n_redundant=0, n_clusters_per_class=1)
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(xtrain, ytrain)
print(accuracy_score(ytest, model.predict(xtest)), "is the accuracy after calculating the testing and training data")
x = ["positive", "negative", "neutral"]
y= [positive, negative, neutral]
w = [0.2, 0.5, 0.7]
c = ["Green", "Red","Gold"]
plt.bar(x,y,width=0.5,color = c)
plt.xlabel("Sentiment")
plt.ylabel("No of sentiments for each")
plt.show()
gen= '****************************************************************************************************************************************'
for i in gen:
    print(i, end='')
    sys.stdout.flush()
    time.sleep(0.05)