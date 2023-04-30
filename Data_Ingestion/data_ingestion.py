import pandas as pd
import os
import sys
from App_Logging.logger import get_logs
from Exception_Handling.exception import CustomException
from dataclasses import dataclass

@dataclass
class DataLoader:

    '''class name: DataLoader
    
    description: This class will load input data file
    
    Written by: Siddharth Pal'''

    def __init__(self):
        #self.data_loader = DataLoader()
        self.logger = get_logs( open("Logs//Training_dataIngestion_validation_logs.txt" , "a") )
        self.logger.write_logs("Entered data_loader directory")

        

    

    def get_train_data(self):

        self.logger.write_logs("Entered get train data method.")

        try:
            train_data = pd.read_csv('C:\BigMartSales\Data\Train.csv')
            self.logger.write_logs("Task of Reading Train Data completed") 
            return train_data
        
        except Exception as e:
            raise CustomException(e,sys)


        
    def get_test_data(self):
        self.logger.write_logs("Entered get test data method.")



        try:

            test_data = pd.read_csv('C:\BigMartSales\Data\Test.csv')
            self.logger.write_logs("Task of Reading Test Data Completed")
            return test_data

        
        except Exception as e:
            raise CustomException(e,sys)

if __name__=="__main__":
    obj = DataLoader()
    obj.get_train_data()
    obj.get_test_data()
