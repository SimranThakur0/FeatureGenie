
import unittest
import pandas as pd
from featuregenie.feature_engineer import FeatureEngineer

class TestFeatureEngineer(unittest.TestCase):

    def setUp(self):
        """Setup sample DataFrame for testing."""
        self.data = {'A': [1, 2, 3], 'B': [10, 20, 30], 'date': ['2024-01-01', '2024-02-15', '2024-03-20'], 'text': ['hello world', 'test data', 'sample sentence']}
        self.df = pd.DataFrame(self.data)
        self.fe = FeatureEngineer(self.df)

    def test_polynomial_features(self):
        """Test polynomial features are generated correctly."""
        df = self.fe.generate_polynomial_features(['A', 'B'], degree=2)
        self.assertIn('A^2', df.columns)
        self.assertIn('A B', df.columns)

    def test_date_features(self):
        """Test date features are extracted correctly."""
        df = self.fe.extract_date_features('date')
        self.assertIn('date_year', df.columns)
        self.assertIn('date_month', df.columns)
        self.assertIn('date_dayofweek', df.columns)

    def test_text_features(self):
        """Test text features are extracted correctly."""
        df = self.fe.extract_text_features('text')
        self.assertIn('text_word_count', df.columns)
        self.assertIn('text_char_count', df.columns)
        self.assertIn('text_sentence_count', df.columns)

if __name__ == '__main__':
    unittest.main()
