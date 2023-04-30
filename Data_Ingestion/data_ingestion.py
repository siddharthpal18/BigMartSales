import pandas as pd
import os
import sys
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass

@dataclass
class DataLoader:

    '''class name: DataLoader
    
    description: This class will load input data file
    
    Written by: Siddharth Pal'''

    def __init__(self):
        #self.data_loader = DataLoader()

        logging.info("Entered data loader directory.")

    

    def get_train_data(self):

        logging.info("Entered get train data method.")

        try:
            train_data = pd.read_csv('C:\BigMartSales\Data\Train.csv')
            logging.info("Task of Reading Train Data completed") 
            return train_data
        
        except Exception as e:
            raise CustomException(e,sys)


        
    def get_test_data(self):
        logging.info("Entered get test data method.")



        try:

            test_data = pd.read_csv('C:\BigMartSales\Data\Test.csv')
            logging.info("Task of Reading Test Data Completed")
            return test_data

        
        except Exception as e:
            raise CustomException(e,sys)

if __name__=="__main__":
    obj = DataLoader()
    obj.get_train_data()
    obj.get_test_data()
