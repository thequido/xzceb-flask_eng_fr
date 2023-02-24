import unittest

from translator import english_to_french, french_to_english

class TestEnFr(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour') #Test Hello translates to Bonjour
        self.assertNotEqual(english_to_french(''), '')  #Test for null input
        

class TestFrEn(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello') #Test Bonjour translates to Hello
        self.assertNotEqual(french_to_english(''), '')  #Test for null input
        
unittest.main()
