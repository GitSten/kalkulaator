import unittest
import calc

class testcalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10,5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(2, 2), 4)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10,5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(2, 2), 0)

    def  test_multiply(self):
        self.assertEqual(calc.multiply(2,2), 4)
        self.assertEqual(calc.multiply(10,10), 100)
        self.assertEqual(calc.multiply(10,5),50)

    def test_divide(self):
        self.assertEqual(calc.divide(10,5), 2)


    def test_square_root(self):
        self.assertEqual(calc.square_root(100),10)

    def test_root(self):
        self.assertEqual(calc.root(10),100)






if __name__ == "__main__":
    unittest.main()


