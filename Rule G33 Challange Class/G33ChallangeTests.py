"""G33ChallangeTests"""
import unittest
from unittest import TestCase
import ruleg33function
from ruleg33function import calc_accuredinterest, calc_dollarprice, calc_yield

class G33ChallangeTests(TestCase):
    """G33ChallangeTests"""
    def test_accured_interest(self):
        """test_accured_interest"""
        self.assertEqual(calc_accuredinterest(2.34567), 2.35)

    def test_calc_dollarprice(self):
        """test_accured_interest"""
        self.assertEqual(calc_dollarprice(2.34567), 2.345)

    def test_calc_yield(self):
        """test_accured_interest"""
        self.assertEqual(calc_yield(2.34567), 2.346)

if __name__ == '__main__':
    unittest.main()
