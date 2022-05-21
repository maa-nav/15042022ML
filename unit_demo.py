import unittest
import calc
from calc import Car

class TestCar(unittest.TestCase):
##   Test never run in order..
    
##    def test_add(self):
##        self.assertEqual(calc.add(2,5),7)
##        self.assertEqual(calc.add(2,-5),-3)
##        self.assertEqual(calc.add(-2,-5),-7)
##
##    def test_subtract(self):
##        self.assertEqual(calc.subtract(2,5),-3)
##        self.assertEqual(calc.subtract(2,-5),7)
##        self.assertEqual(calc.subtract(-2,-5),3)
##        
##    def test_multiply(self):
##        self.assertEqual(calc.multiply(2,5),10)
##        self.assertEqual(calc.multiply(2,-5),-10)
##        self.assertEqual(calc.multiply(-2,-5),10)
##        
##    def test_division(self):
##        self.assertEqual(calc.division(10,5),2)
##        self.assertEqual(calc.division(-10,-5),2)
##        self.assertEqual(calc.division(-10,5),-2)
##
##    # To test an exception (2 ways)
##    #1. self.assertRaises(ValueError,calc.division,10,0)
##        with self.assertRaises(ValueError):
##            calc.division(10,0)
        @classmethod
        def setUpClass(cls):
            print('1st thing to run before testing starts')
        @classmethod
        def tearDownClass(cls):
            print('Last thing to run after all testing done')


        def setUp(self):
            self.car1 = Car('tata',2500,500)
            print('Before each unit testing')
        def tearDown(self):
            print('After each unit testing complete')

        
    
        def test_drive(self):
##            car1 = Car('tata',2500,500)
            print('testing...')
            self.assertEqual(self.car1.drive(),'The tata has started')
        def test_eng(self):
            print('testing...')
##            car1 = Car('tata',2500,500)
            self.assertEqual(self.car1.eng(),'The tata has a engine of 2500 cc')
        def test_discount(self):
##            car1 = Car('tata',2500,500)
            print('testing...')
            self.car1.discount()
            self.assertEqual(self.car1.price,400)
    
        

if __name__ == '__main__':
    unittest.main()
