import unittest
def fun(x,y):
        
    return x*y
class Mytest(unittest.TestCase):

    def test(self):
        self.assertEqual(fun(4,2),8)
if __name__ == '__main_':
    unittest.main()
