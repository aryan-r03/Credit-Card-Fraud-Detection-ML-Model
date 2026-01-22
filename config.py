"""
Configuration settings for the Fraud Detection application
"""
import os

class Config:
    # Flask settings
    DEBUG = True
    PORT = 5000
    HOST = '127.0.0.1'
    
    # Model settings
    MODEL_PATH = 'fraud_model.pkl'
    DATASET_PATH = 'creditcard.csv'
    
    # Random Forest settings
    N_ESTIMATORS = 100
    RANDOM_STATE = 42
    CLASS_WEIGHT = 'balanced'
    
    # Train-test split
    TEST_SIZE = 0.2
    
    # Feature names
    FEATURE_NAMES = ['Time', 'Amount'] + [f'V{i}' for i in range(1, 29)]
    
    # Risk thresholds (in percentage)
    LOW_RISK_THRESHOLD = 20
    MEDIUM_RISK_THRESHOLD = 50
    HIGH_RISK_THRESHOLD = 80
    
    @staticmethod
    def get_base_dir():
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
