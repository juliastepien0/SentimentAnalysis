"""
Class for unit testing the outcome of the sentiment analysis.
"""
import unittest
from SentAnalysis.sent_analysis import sentiment_analyzer

class test_sentiment_analyzer(unittest.TestCase):
    """
    Unit tests for sentiment_analyzer.py
    """
    def test_sentiment_analyzer(self):
        # Test case for positive sentiment
        result1 = sentiment_analyzer('Kocham pracować z Pythonem')
        self.assertEqual(result1['label'], 'positive')

        # Test case for neutral sentiment
        result2 = sentiment_analyzer('Moje odczucia wobec Pythona są neutralne')
        self.assertEqual(result2['label'], 'neutral')

        # Test case for negative sentiment
        result3 = sentiment_analyzer('Nienawidzę pracować z Pythonem, nienawidzę!')
        self.assertEqual(result3['label'], 'negative')
