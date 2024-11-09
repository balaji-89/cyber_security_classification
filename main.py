import dill
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler


def predict_using_xgb(preprocessing_pipeline, xgb_model, x_item):
    x_item = preprocessing_pipeline.transform([x_item.values()])
    prediction = xgb_model.predict(x_item)
    if prediction == 0:
        return 'BenignPositive'
    
    elif prediction ==1 :
        return 'TruePositive'
    
    else:
        return 'FalsePositive'
    


with open(r'/home/laptop-kl-11/personal_project/cyber_security_classification/pickle_files/preprocess_pipeline.pkl','rb') as file:
    preprocessing_pipeline = dill.load(file)

with open(r'/home/laptop-kl-11/personal_project/cyber_security_classification/pickle_files/xgb_weights.pkl','rb') as file:
    xgb_model = dill.load(file)


for idx, item in pd.read_csv('/home/laptop-kl-11/personal_project/cyber_security_classification/dataset/train_subset.csv')[:20].iterrows():
    predict_using_xgb(preprocessing_pipeline,xgb_model,item)

