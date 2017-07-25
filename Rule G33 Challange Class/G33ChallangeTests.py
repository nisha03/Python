"""G33ChallangeTests"""
import unittest
from unittest import TestCase
import G33Challange

class G33ChallangeTests(unittest.TestCase):
    """G33ChallangeTests"""
    def setUp(self):
        self.g33 = G33Challange(self)
    def test_accured_interest(self):
        """test_accured_interest"""
        self.g33.choice = "A\r"
        self.g33.num = 2.34567
        self.assertEqual(g33.ask, 2.35)

if __name__ == '__main__':
    unittest.main()
