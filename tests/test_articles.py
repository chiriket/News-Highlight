import unittest
from app.models import Articles

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Articles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_articles = Articles('Chiri', 'Kenyan', 'The variety and rich culture that exists in Kenya', 'https://ktn.co.ke/image1','https://ktn.co.ke', 'KTN News')

    def test_instance(self):
        '''
        Test to check if new_Articles instance exists
        '''

        self.assertTrue(isinstance(self.new_articles,Articles))