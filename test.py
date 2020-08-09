import unittest
import main

class CalculatorTest(unittest.TestCase):

    def setUp(self):

        """Setup the app for testing"""
        main.app.testing = True
        self.app = main.app.test_client()

    def test_empty_page(self):

        """Test the empty page"""
        solution = self.app.get("/")
        self.assertEqual(
            b"Usage;\n<Operation>?X=<Value1, Value2, ..., ValueN>\n", solution.data)

if __name__ == "__main__":
    unittest.main()
