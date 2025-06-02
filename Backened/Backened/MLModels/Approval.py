from joblib import dump
import pandas as pd 
import numpy as np
import os
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
data=pd.read_csv(r"C:/Users/HP/Downloads/Intake.csv")
label_encoder_program=LabelEncoder()
label_encoder_level=LabelEncoder()
label_encoder_App=LabelEncoder()
data["Approval"]=label_encoder_App.fit_transform(data["Approval"])
data["Level"]=label_encoder_level.fit_transform(data["Level"])
data["Program"]=data["Program"].str.split(" ").str.get(0)
data["Program"]=label_encoder_program.fit_transform(data["Program"])
model=LogisticRegression(max_iter=1000  )
x=data.drop(columns="Approval")
y=data["Approval"]
print(data.info())
model.fit(x,y)

model_directory = 'MLModels'
if not os.path.exists(model_directory):
    os.makedirs(model_directory)

# Save the model to a joblib file
model_path = os.path.join(model_directory, 'model.joblib')
dump(model, model_path)
dump(label_encoder_program, os.path.join(model_directory, 'label_encoder_program.joblib'))
dump(label_encoder_level, os.path.join(model_directory, 'label_encoder_level.joblib'))

# print(f"Model saved at {model_path}")
# print(os.path.abspath('MLModels/model.joblib'))
# print(f"Label encoder saved at {encoder_path}")
# print(os.path.abspath('MLModels\label_encoder.joblib'))
