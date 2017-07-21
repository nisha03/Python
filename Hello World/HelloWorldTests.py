"""HelloWroldTests"""
import unittest
from HelloWorld import HelloWorld

class HelloWorldTests(unittest.TestCase):
    """HelloWorldTests"""
    def test_default_greeting_set(self):
        """HelloWorldTests"""
        helloworld = HelloWorld()
        self.assertEqual(helloworld.message, 'Hello world')

if __name__ == '__main__':
    unittest.main()
