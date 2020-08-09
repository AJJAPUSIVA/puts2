import unittest
import main


class TestCalculator(unittest.TestCase):

    def setUp(self):
        main.app.testing = True
        self.app = main.app.test_client()

    def testMax1(self):
        solution = self.app.get("/max?X=1,2,5,0,100")
        self.assertEqual(b'100 \n', solution.data)

    def testMax2(self):
        solution = self.app.get("/max?X=1,2.33,4.5,3.6")
        self.assertEqual(b'4.5 \n', solution.data)

    def testMax3(self):
        solution = self.app.get("/max?X=1,2,5,0,100,-100,-5,-2")
        self.assertEqual(b'100 \n', solution.data)


if __name__ == '__main__':
    unittest.main()
