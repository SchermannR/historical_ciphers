from historical_ciphers import *
import unittest

class MyTest(unittest.TestCase):
    def test_caesar(self):
        self.assertEqual(caesar("CAESAR","e",3),"FDHVDU")
        self.assertEqual(caesar("abcdef","d",7),"TUVWXY")
        self.assertEqual(vigenere("THEYDRINKTHETEA","e","duh"),"WBLBXYLHRWBLWYH")
        self.assertEqual(vigenere("LLGPHKARMKLXLIC","d","secret"),"THEYDRINKTHETEA")
        self.assertEqual(caesar("CAE1SAR","e",3),"0")
        self.assertEqual(caesar("CAESAR2", "d", 3), "0")
        self.assertEqual(caesar("abcdef", "d", "a"), "0")
        self.assertEqual(vigenere("LLGPHKARMK1LXLIC", "d", "secret"), "0")
        self.assertEqual(vigenere("LLGPHKARMKLXLIC", "d", "sec2ret"), "0")
        
if __name__ =="__main__":
    unittest.main()
