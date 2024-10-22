import unittest

from triangle import is_valid_triangle, type_of_triangle

class TestTriangleFunctions(unittest.TestCase):
    
    def test_valid_triangle(self):
        "Test case for valid triangles"
        self.assertTrue(is_valid_triangle(3, 4, 5))
        self.assertTrue(is_valid_triangle(5, 5, 5))
        self.assertTrue(is_valid_triangle(2, 2, 3))

    def test_invalid_triangle(self):
        "Test case for invalid triangles"
        self.assertFalse(is_valid_triangle(1, 1, 3))
        self.assertFalse(is_valid_triangle(0, 1, 1))
        self.assertFalse(is_valid_triangle(-1, 2, 2))

    def test_equilateral_triangle(self):
        "Test case for equilateral triangle"
        self.assertEqual(type_of_triangle(5, 5, 5), "Equilateral")

    def test_isosceles_triangle(self):
        "Test cases for isosceles triangles"
        self.assertEqual(type_of_triangle(5, 5, 7), "Isosceles")
        self.assertEqual(type_of_triangle(7, 5, 5), "Isosceles")
        self.assertEqual(type_of_triangle(5, 7, 5), "Isosceles")

    def test_scalene_triangle(self):
        "Test case for scalene triangle"
        self.assertEqual(type_of_triangle(3, 4, 5), "Scalene")
        self.assertEqual(type_of_triangle(4, 2, 3), "Scalene")

    def test_invalid_triangle_raises_error(self):
        "Test that an invalid triangle raises a ValueError"

        self.assertRaises(ValueError, type_of_triangle, 1, 1, 3)

        with self.assertRaises(ValueError):
            type_of_triangle(0, 1, 1)
        with self.assertRaises(ValueError):
            type_of_triangle(-1, 2, 2)

if __name__ == '__main__':
    unittest.main()
