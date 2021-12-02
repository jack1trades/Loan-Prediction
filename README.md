### Overview
* Created a tool for detection of spam mail from non-spam mails
* Dataset was downloaded from kaggle
* Optimized Base and Ensemble Learner Algorithms to build a model
* Built a client facing API using fastapi and colabcode

### Code and Resources used
* Python version : Python 3.7
* Packages : pandas, numpy, matplotlib, seaborn, sklearn, pickle, fastapi, colabcode

### Project Walk-through
* Dataset : Dataset was downloaded from kaggle, and read using pandas.
* Data Cleaning : Data was checked for null values and resolved.
* Label Encoding : As the target variable is categorical-nominal, it was encoded as categorical-numerical variable.
* The Split : The dataset was divided - predictor(X) and target variable(y). Also, train_test_split is implemented too.
* Base Models : Base Regression Classifiers, Support Vector Machines and KNearestClassifier were implemented.
* Ensemble Models : Random Forest, and Boosting Algorithms - AdaBoostClassifier, GradientBoostingClassifier, XGBClassifier - were also used, to train the model.
* Inference : RandomForestClassifier give maximum accuracy for correct prediction of text with utmost ability to categorize the mails as - apam and ham.
* Deployment : The model was deployed using fastapi and colabcode, with the aid of pickle and pydantic.
