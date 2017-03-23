# coding: UTF-8


import unittest
import program


class TestHI(unittest.TestCase):

    def setUp(self):
        self.hashc = program.HashIdentifier('f5d1278e8109edd94e1e4197e04873b9')


    def test_decrypt(self):
        self.decryption = self.hashc.decrypt()
        
        self.assertTrue(self.decryption)
        self.assertIsNotNone(self.decryption)
        self.assertEqual(self.decryption, 'tester')



if __name__ == '__main__':
    unittest.main()