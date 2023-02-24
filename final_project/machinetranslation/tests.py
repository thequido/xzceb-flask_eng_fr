import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnFr(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench('Hello'), 'Bonjour') #Test Hello translates to Bonjour
        self.assertNotEqual(square(''), '')  #Test for null input
        

class TestFrEn(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello') #Test Bonjour translates to Hello
        self.assertNotEqual(square(''), '')  #Test for null input
        
unittest.main()
