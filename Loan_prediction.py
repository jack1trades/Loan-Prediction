# -*- coding: utf-8 -*-
"""Loan prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kjUrq94J3SnJ__yeXYuQAS1l57e4RiQ5

**BANK LOAN PREDICTION**

**There are a number of challenges solved by ML/DS Algorithms, in our daily life**

**One such challenge for banking firms is- Dealing with unfit candidates for loan**

**Following are a couple of scientific approaches to identify such cases, and to prevent mammoth loss of bank revenue**
"""



"""##### **Dataset**"""

import pandas as pd

"""**1. Train Dataset**

**The Training dataset for building the model upon**
"""

lp = pd.read_csv("Loan-prediction1.csv")

lp.head()

lp.shape

lp.isnull().sum().sum()

lp.info()

from collections import Counter
Counter(lp["Loan_Status"])

"""**2. Test Dataset**

**The Valuation dataset for checking the quality of the model built**
"""

pl = pd.read_csv("Loan-prediction2.csv")

pl.head()

pl.shape



"""##### **Data Cleaning**

1. **Imputation (Missing Values)**
2. **LabelEncoder**
"""



lp.dtypes

lp.isna().sum().sum()

def df_tn(df):

  # Imputation-1

  categorical_columns = ["Gender", "Married", "Dependents", "Education", "Self_Employed", "Property_Area", "Loan_Status"]
  for cat_col in categorical_columns:
    df[cat_col].fillna(df[cat_col].mode()[0], inplace=True)

  # Imputation-2

  numerical_columns = ["ApplicantIncome", "CoapplicantIncome", "LoanAmount", "Loan_Amount_Term", "Credit_History"]
  for nume_cols in numerical_columns:
    df[nume_cols].fillna(df[nume_cols].mean(), inplace=True)

  # LabelEncoder
  
  from sklearn.preprocessing import LabelEncoder
  le = LabelEncoder()
  
  df["Gender"] = le.fit_transform(df["Gender"])
  df["Married"] = le.fit_transform(df.Married)
  df["Dependents"] = le.fit_transform(df.Dependents)
  df["Education"] = le.fit_transform(df.Education)
  df["Self_Employed"] = le.fit_transform(df.Self_Employed)
  df["Property_Area"] = le.fit_transform(df.Property_Area)
  df["Loan_Status"] = le.fit_transform(df.Loan_Status)

  # Alphanumeric deletions ( # replacings )

  del df["Loan_ID"]
  # df["Loan_ID"] = list(range(1, (len(df.Gender)+1)))
  # df.set_index(["Loan_ID"], inplace=True)
  # df.reset_index(inplace=True)

df_tn(lp)

lp.isna().sum().sum()

lp.head()

"""**"lp" is the training set**

**"pl" --> is the testing set**
"""

def df_tt(df):

  # Imputation-1

  categorical_columns = ["Gender", "Married", "Dependents", "Education", "Self_Employed", "Property_Area"]
  for cat_col in categorical_columns:
    df[cat_col].fillna(df[cat_col].mode()[0], inplace=True)

  # Imputation-2

  numerical_columns = ["ApplicantIncome", "CoapplicantIncome", "LoanAmount", "Loan_Amount_Term", "Credit_History"]
  for nume_cols in numerical_columns:
    df[nume_cols].fillna(df[nume_cols].mean(), inplace=True)

  # LabelEncoder
  
  from sklearn.preprocessing import LabelEncoder
  le = LabelEncoder()
  
  df["Gender"] = le.fit_transform(df["Gender"])
  df["Married"] = le.fit_transform(df.Married)
  df["Dependents"] = le.fit_transform(df.Dependents)
  df["Education"] = le.fit_transform(df.Education)
  df["Self_Employed"] = le.fit_transform(df.Self_Employed)
  df["Property_Area"] = le.fit_transform(df.Property_Area)

  # Alphanumeric deletions ( # replacings )

  del df["Loan_ID"]
  # df["Loan_ID"] = list(range(1, (len(df.Gender)+1)))
  # df.set_index(["Loan_ID"], inplace=True)
  # df.reset_index(inplace=True)

df_tt(pl)

pl.isna().sum().sum()

pl.head()

"""##### **The Split**"""

X = lp.drop(columns = ["Loan_Status"], axis=1)
y = lp["Loan_Status"]

X_train = lp.drop(columns=["Loan_Status"], axis=1)
y_train = lp["Loan_Status"]

# X_test is the dataframe "pl"

"""##### **Linear Regression**"""

from sklearn.linear_model import LinearRegression

lr = LinearRegression()

lr.fit(X_train, y_train)

lr.score(X_train, y_train)

# Prediction

y_pred = lr.predict(X_train)

y_pred

from sklearn.metrics import accuracy_score

accuracy_score(y_train, y_pred.round())

lr.score(X_train, y_train)

from sklearn.metrics import mean_squared_error, mean_absolute_error

mean_absolute_error(y_train, y_pred)



"""##### **LogisticRegression**"""

from sklearn.linear_model import LogisticRegression







"""##### **SupportVectorMachines**"""

from sklearn.svm import SVC

svm = SVC()

svm.fit(X_train, y_train)

# Model Score

svm.score(X_train, y_train)

# Prediction

y_pred = svm.predict(pl)

# Valuation Score

svm.score(pl, y_pred)



"""##### Lesson Learnt

Lesson Learnt - 

    model.score(X,y)
            -->> predicts the target value for X_df under hood, and compares that under_hood_predicted_value with the "y"

##### **kNearestNeighbors**
"""

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()

knn.fit(X_train, y_train)

# Model Score

knn.score(X_train, y_train)

# Prediction

y_pred = knn.predict(pl)

# Valuation Score

knn.score(pl, y_pred)



"""##### **DecisionTreeClassifier**"""

from sklearn.tree import DecisionTreeClassifier

tree = DecisionTreeClassifier()

tree.fit(X_train, y_train)

# Model Score

tree.score(X_train, y_train)

# Prediction

y_pred = tree.predict(pl)

# Valuation Score

tree.score(pl, y_pred)



"""##### **RandomForestClassifier**"""

from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier()

rfc.fit(X_train, y_train)

# Model Score

rfc.score(X_train, y_train)

# Prediction

y_pred = rfc.predict(pl)

# Valuation Score

rfc.score(pl, y_pred)



"""##### **AdaBoostClassifier**"""

from sklearn.ensemble import AdaBoostClassifier

ada = AdaBoostClassifier()

ada.fit(X_train, y_train)

# Model Score

ada.score(X_train, y_train)

# Prediction

y_pred = ada.predict(pl)

# Valuation Score

ada.score(pl, y_pred)



"""##### **GradientBoostingClassifier**"""

from sklearn.ensemble import GradientBoostingClassifier

grad = GradientBoostingClassifier()

grad.fit(X_train, y_train)

# Model Score

grad.score(X_train, y_train)

# Prediction

y_pred = grad.predict(pl)

# Valuation Score

grad.score(pl, grad.predict(pl))



"""##### **XGBClassifier**"""

import xgboost
from xgboost import XGBClassifier

xgb = XGBClassifier()

xgb.fit(X_train, y_train)

# Model Score

xgb.score(X_train, y_train)

# Prediction

y_pred = xgb.predict(pl)

# Valuation Score

xgb.score(pl, y_pred)



"""##### **Gobbledygook**"""



"""##### **Model Selected**

**The selected model based on model score (model.score) is RandomForestClassifier, whose training score was 1**
"""



"""##### **Deployment**"""

# Pckle dump

import pickle

pickle.dump(rfc, open("model_rfc.pkl", "wb"))

# Pydantic

!pip install pydantic
from pydantic import BaseModel

class Customer_details(BaseModel):
  Gender             : str
  Married            : str
  Dependents         : int
  Education          : str
  Self_Employed      : str
  ApplicantIncome    : float
  CoapplicantIncome  : float
  LoanAmount         : float
  Loan_Amount_Term   : float
  Credit_History     : float
  Property_Area      : str

  class Config:
    schema_extra = {
        "example" : {
            "Gender"            : "Male",
            "Married"           : "No",
            "Dependents"        : 0,
            "Education"         : "Graduate",
            "Self_Employed"     : "Yes",
            "ApplicantIncome"   : 3564.00,
            "CoapplicantIncome" : 5482.00,
            "LoanAmount"        : 265.00,
            "Loan_Amount_Term"  : 258.00,
            "Credit_History"    : 1,
            "Proprty_Area"      : "Urban"
        }
    }

# FastAPI

!pip install fastapi
from fastapi import FastAPI

app = FastAPI()

@app.on_event("startup")
def load_model():                                   # path.operation.functiuno
  global model
  model = pickle.load(open("model_rfc.pkl", "rb"))

@app.get("/")
def index():
  return {"message" : "Homepage of API"}

@app.post("predict")
def get_customer_details(data: Customer_details):
  received = data.dict()
  Gender  =  received["Gender"]
  Married  =  received["Married"]
  Dependents  =  received["Dependents"]
  Education  =  received["Education"]
  Self_Employed  =  received["Self_Employed"]
  ApplicantIncome  =  received["ApplicantIncome"]
  CoapplicantIncome  =  received["CoapplicantIncome"]
  LoanAmount  =  received["LoanAmount"]
  Loan_Amount_Term  =  received["Loan_Amount_Term"]
  Credit_History  =  received["Credit_History"]
  Property_Area  =  received["Property_Area"]

  pred_name = model.predict([[Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area]]).tolist()[0]
  return {"prediction" : pred_name}

# ColabCode

!pip install colabcode

from colabcode import ColabCode

server = ColabCode(port = 15000, code=False)

server.run_app(app = app)

"""##### **END OF THE LINE**"""