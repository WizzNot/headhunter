import unittest
import math
import main
from parameterized import parameterized

class TestCircle(unittest.TestCase):
    def test_create_circle_and_get_area(self):
        circle = main.Circle(2)
        self.assertEqual(circle.get_area(), math.pi * 2 * 2)
    
    def test_create_circle_with_zero_radius(self):
        try:
            circle = main.Circle(0)
        except ValueError:
            pass


class TestTriangle(unittest.TestCase):
    def test_create_triangle_and_get_area(self):
        triangle = main.Triangle(1, 1, 1)
        self.assertEqual(triangle.get_area(), math.sqrt(3) * (1 ** 2) / 4)
    
    def test_create_triangle_with_zero_radius(self):
        try:
            triangle = main.Triangle(-1, 1, 0)
        except ValueError:
            pass
    
    def test_create_triangle_where_sum_two_sides_less_than_third(self):
        try:
            triangle = main.Triangle(3, 10, 4)
        except ValueError:
            pass
    
    @parameterized.expand([
        [3, 4, 5, True],
        [3, 4, 6, False],
        [5, 12, 13, True]
    ])
    def test_is_rectangular(self, a, b, c, is_rect):
        triangle = main.Triangle(a, b, c)
        self.assertEqual(triangle.is_rectangular(), is_rect)


if __name__ == "__main__":
    unittest.main()