import unittest
import main


class TestCalculator(unittest.TestCase):

    def setUp(self):
        main.app.testing = True
        self.app = main.app.test_client()

    def testMed1(self):
        solution = self.app.get("/median?X=1,2,5,0,100")
        self.assertEqual(b'2 \n', solution.data)

    def testMed2(self):
        solution = self.app.get("/median?X=1,2,5,0,100,-100,-5,-2")
        self.assertEqual(b'0.5 \n', solution.data)

    def testMed3(self):
        solution = self.app.get("/median?X=1,0.3,0.33333,0.2934943943,02.050")
        self.assertEqual(b'0.333 \n', solution.data)


if __name__ == '__main__':
    unittest.main()
