"""
Utility for generating sample fraud detection data
"""
import numpy as np
import pandas as pd


class DataGenerator:
    """Generate sample credit card transaction data for testing"""
    
    @staticmethod
    def create_sample_data(n_samples=5000, random_state=42):
        """
        Create a synthetic dataset for fraud detection
        
        Args:
            n_samples: Number of samples to generate
            random_state: Random seed for reproducibility
            
        Returns:
            DataFrame with synthetic transaction data
        """
        print("Creating sample dataset...")
        np.random.seed(random_state)
        
        data = {
            'Time': np.random.randint(0, 172792, n_samples),
            'Amount': np.random.exponential(88, n_samples)
        }
        
        # Generate V1-V28 features
        for i in range(1, 29):
            data[f'V{i}'] = np.random.randn(n_samples)
        
        df = pd.DataFrame(data)
        
        # Create fraud labels based on heuristics
        score = (
            (df['Amount'] > 300) * 3 + 
            (df['V1'].abs() > 2) * 2 + 
            (df['V4'].abs() > 2) * 1.5
        )
        
        df['Class'] = 0
        df.loc[score.nlargest(50).index, 'Class'] = 1
        
        return df
