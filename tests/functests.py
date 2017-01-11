import unittest

from tornado.testing import AsyncHTTPTestCase

from dexplorer import DataExplorer


class TestDataServer(AsyncHTTPTestCase):

    def get_app(self):
        dte = DataExplorer()
        return dte.make_app()

    def test_homepage(self):
        response = self.fetch('/')
        self.assertEqual(response.code, 200)
        self.assertIn("Data Explorer", str(response.body))


if __name__ == "__main__":
    unittest.main()
