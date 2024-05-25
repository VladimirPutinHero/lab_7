import unittest
from lab_7_3 import count_routes


class TestCountRoutes(unittest.TestCase):
    def test_small_grid(self):
        result = count_routes(2, 2)
        self.assertEqual(result, 2)

    def test_large_grid(self):
        result = count_routes(3, 3)
        self.assertEqual(result, 6)

    def test_square_grid(self):
        result = count_routes(4, 4)
        self.assertEqual(result, 20)


if __name__ == "__main__":
    unittest.main()
