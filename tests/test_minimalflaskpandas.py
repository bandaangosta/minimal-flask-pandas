import unittest

import minimalflaskpandas


class MinimalflaskpandasTestCase(unittest.TestCase):

    def setUp(self):
        self.app = minimalflaskpandas.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertIn('Welcome to Minimal Flask Pandas', rv.data.decode())


if __name__ == '__main__':
    unittest.main()
