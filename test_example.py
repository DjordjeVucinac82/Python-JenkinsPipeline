import unittest

def add(x, y):
    """Function to add two numbers."""
    return x + y

class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

if __name__ == '__main__':
    unittest.main()