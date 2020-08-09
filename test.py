import unittest
import main


class TestCalculator(unittest.TestCase):

    def setUp(self):
        main.app.testing = True
        self.app = main.app.test_client()

    def test_empty_page(self):
        """Test the empty page"""
        solution = self.app.get("/")
        self.assertEqual(
            b"Usage;\n<Operation>?X=<Value1, Value2, ..., ValueN>\n", solution.data)

    def testMax1(self):
        solution = self.app.get("/max?X=1,2,5,0,100")
        self.assertEqual(b'100 \n', solution.data)

    def testMax2(self):
        solution = self.app.get("/max?X=1,2.33,4.5,3.6")
        self.assertEqual(b'4.5 \n', solution.data)

    def testMax3(self):
        solution = self.app.get("/max?X=1,2,5,0,100,-100,-5,-2")
        self.assertEqual(b'100 \n', solution.data)

    def testMin1(self):
        solution = self.app.get("/min?X=1,2,5,0,100")
        self.assertEqual(b'0 \n', solution.data)

    def testMin2(self):
        solution = self.app.get("/min?X=1,2.33,4.5,3.6")
        self.assertEqual(b'1 \n', solution.data)

    def testMin3(self):
        solution = self.app.get("/min?X=1,2,5,0,100,-100,-5,-2")
        self.assertEqual(b'-100 \n', solution.data)

    def testAverage(self):
        solution = self.app.get("/average?X=1,2,5,0,100")
        self.assertEqual(b'21.6 \n', solution.data)

    def testAvg(self):
        solution = self.app.get("/avg?X=1,2.33,4.5,3.6")
        self.assertEqual(b'2.857 \n', solution.data)

    def testMean(self):
        solution = self.app.get("/mean?X=1,2,5,0,100,-100,-5,-2")
        self.assertEqual(b'0.125 \n', solution.data)

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
