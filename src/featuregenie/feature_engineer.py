import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures

class FeatureEngineer:
    
    def __init__(self, df):
        """Initialize with a Pandas DataFrame."""
        self.df = df.copy()
    
    def generate_polynomial_features(self, features, degree=2):
        """Generates polynomial features for specified columns."""
        poly = PolynomialFeatures(degree=degree, include_bias=False)
        poly_features = poly.fit_transform(self.df[features])
        poly_df = pd.DataFrame(poly_features, columns=poly.get_feature_names_out(features))
        self.df = pd.concat([self.df, poly_df], axis=1)
        return self.df
    
    def extract_date_features(self, date_column):
        """Extracts date-based features from a datetime column."""
        self.df[date_column] = pd.to_datetime(self.df[date_column])
        self.df[f'{date_column}_year'] = self.df[date_column].dt.year
        self.df[f'{date_column}_month'] = self.df[date_column].dt.month
        self.df[f'{date_column}_day'] = self.df[date_column].dt.day
        self.df[f'{date_column}_dayofweek'] = self.df[date_column].dt.dayofweek
        self.df[f'{date_column}_is_weekend'] = self.df[date_column].dt.dayofweek.isin([5, 6]).astype(int)
        return self.df
    
    def extract_text_features(self, text_column):
        """Extracts basic text features like word count, character count, and sentence count."""
        self.df[f'{text_column}_word_count'] = self.df[text_column].apply(lambda x: len(str(x).split()))
        self.df[f'{text_column}_char_count'] = self.df[text_column].apply(lambda x: len(str(x)))
        self.df[f'{text_column}_sentence_count'] = self.df[text_column].apply(lambda x: len(str(x).split('.')))
        return self.df
    
    def get_dataframe(self):
        """Returns the processed DataFrame."""
        return self.df

# Example Usage
if __name__ == "__main__":
    data = {
        'A': [1, 2, 3, 4],
        'B': [10, 20, 30, 40],
        'date': ['2024-01-01', '2024-02-15', '2024-03-20', '2024-04-10'],
        'text': ['This is a sentence.', 'Another example!', 'How are you?', 'I am fine.']
    }
    
    df = pd.DataFrame(data)
    fe = FeatureEngineer(df)
    df = fe.generate_polynomial_features(['A', 'B'], degree=2)
    df = fe.extract_date_features('date')
    df = fe.extract_text_features('text')
    print(df.head())
