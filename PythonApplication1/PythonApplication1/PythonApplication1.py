import unittest

from my_function import my_function


class MyFunctionTest(unittest.TestCase):

    def test_my_function(self):
        self.assertEqual(my_function(1), 2)
        self.assertEqual(my_function(2), 4)


if __name__ == "__main__":
    unittest.main()