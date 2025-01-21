import os
import sys
from dataclasses import dataclass

from sklearn.ensemble import (
    RandomForestClassifier,
)
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import r2_score, f1_score, accuracy_score, roc_auc_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from xgboost import XGBClassifier

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object,evaluate_models

@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()


    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Split training and test input data")
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            models = {
                # "LogisticRegression" : LogisticRegression(),
                # "Decision Tree": DecisionTreeClassifier(),
                "Random Forest": RandomForestClassifier(),
                # "XGBClassifier": XGBClassifier(),
            }
            params={
                # "LogisticRegression": {
                #     'penalty': ['l2'], 
                #     'C': [0.001, 0.01, 0.1, 1, 10 , 100, 1000], 
                #     'solver': ['liblinear'],
                #     'max_iter': [100,150,200,400,600,800,1000]  
                # },
                # "Decision Tree": {
                #     'criterion':['gini', 'entropy'],
                #     'max_features':['sqrt'],
                # },
                "Random Forest": {
                    'criterion': ['log_loss'], 
                    'max_features': ['sqrt'], 
                    'n_estimators': [100,150,300,1000], 
                    'max_depth': [10,20,30,50,100],
                },
                # "XGBClassifier": {
                #     'learning_rate': [0.05, 0.1, 0.15],
                #     'n_estimators': [100, 150, 200],
                #     'booster': ['gbtree', 'gblinear']
                # },
            }

            model_report:dict=evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,
                                             models=models,param=params)
            
            ## To get best model score from dict
            best_model_score = max(sorted(model_report.values()))

            ## To get best model name from dict

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]

            if best_model_score<0.7:
                raise CustomException("No best model found")
            logging.info(f"Best found model on both training and testing dataset")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            predicted=best_model.predict(X_test)

            score = f1_score(y_test, predicted)
            return score

        except Exception as e:
            raise CustomException(e,sys.exc_info())