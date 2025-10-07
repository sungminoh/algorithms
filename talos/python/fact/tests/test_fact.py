import unittest

from fact.fact import fact

class FactTestSuite(unittest.TestCase):
    """Fact test cases."""

    def test_fact(self):
        assert fact(0) == 1
        assert fact(1) == 1
        assert fact(2) == 2
        assert fact(3) == 6


if __name__ == '__main__':
    unittest.main()
