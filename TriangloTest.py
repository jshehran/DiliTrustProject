import unittest
from dilitrust import trianglo


class TriangloUnitTests(unittest.TestCase):
    def test_equilateral_triangle(self):
        self.assertEqual(trianglo(6, 6, 6), "Equilateral", "Should be Equilateral Triangle")

    def test_isosceles_triangle(self):
        self.assertEqual(trianglo(5, 4, 5), "Isosceles", "Should be Isosceles Triangle")

    def test_right_angle_triangle(self):
        self.assertEqual(trianglo(5,3,4),"Right Angled","Should be Right Angled Triangle")

    def test_nothing_special(self):
        self.assertEqual(trianglo(8,6,5),"nothing special", "Should be Nothing special")


if __name__ == '__main__':
    unittest.main()
