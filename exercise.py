import unittest
import library

"""
For all functions in library.py, build one ore more unit test methods
to check the required functionalities of the library.
References:
    1 - https://docs.python.org/3/library/unittest.html
    2 - https://numpy.org/doc/stable/reference/routines.testing.html

For Part 2. in each method you need to modify the code in library.py 
without breaking it.
"""

class TestLibrary(unittest.TestCase):

    def test_is_perfect_square(self):
        # 1. Check if it works
        self.assertTrue(library.is_perfect_square(36))
        self.assertFalse(library.is_perfect_square(6))

        # 2. Raise TypeError when using floats or string
        with self.assertRaises(TypeError):
            library.is_perfect_square('6')
            
        with self.assertRaises(TypeError):
            library.is_perfect_square(6.6)

    def test_gcd(self):
        # 1. Check if it works
        self.assertEqual(library.gcd(24,36), 12)
        self.assertNotEqual(library.gcd(36,42),2)
        # 2. Raise TypeError floats and string argument
        with self.assertRaises(TypeError):
            library.gcd(24,'36')
        
        with self.assertRaises(TypeError):
            library.gcd(24.3, 10.0)

    def test_are_arrays_equal(self):
        # 1. Check if it works using numpy testing methods
        # 2. Define a new error to be raised when catching numpy data type errors. 
        pass


if __name__ == "__main__":
    unittest.main()

