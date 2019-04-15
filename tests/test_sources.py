import unittest
from app.models import Sources

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_sources = Sources('KTN', 'KTN-NEWS', 'Home of News', 'https://ktn.co.ke', 'general', 'en', 'ke')

    def test_instance(self):
        '''
        Test to check if new_sources instance exists
        '''

        self.assertTrue(isinstance(self.new_sources,Sources.class_or_type_or_tuplepython 3.6))