import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegressions
from sklearn.datasets import load_iris

iris =  load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

df['target'] = iris.target

df.loc[df['target'] == 0, 'target'] = 'setosa'
df.loc[df['target'] == 1, 'target'] = 'versicolor'
df.loc[df['target'] == 2, 'target'] = 'virginica'

x = iris.data[:,[0, 2]]
y = iris.target

clf = LogisticRegression()
clf.fit(x, y)

st.sidebar.header('Input features')

sepalValue = st.sidebar.slider('sepal length(cm)', min_value=0.0 , max_value=10.0 , step = 0.1)
petalValue = st.sidebar.slider('petal length(cm)', min_value=0.0 , max_value=10.0 , step = 0.1)

st.title('Iris Classifier')
st.write('## Input value')

value_df = pd.DataFrame({'data':'data', 'sepal length (cm)':sepalValue, 'petal length (cm)':petalValue}, index=[0])
value_df.set_index('data', inplace=True)

st.write(value_df)

pred_probs = clf.predict_proba(value_df)
pred_df = pd.DataFrame(pred_probs,columns=['setosa','versicolor','virginica'],index=['probability'])

st.write('## Prediction')
st.write(pred_df)

# 予測結果の出力
name = pred_df.idxmax(axis=1).tolist()
st.write('## Result')
st.write('このアイリスはきっと',str(name[0]),'です!')

