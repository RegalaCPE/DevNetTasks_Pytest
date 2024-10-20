import unittest
def fun(x):
        
    return x+1
class Mytest(unittest.TestCase):

    def test(self):
        self.assertEqual(fun(4),6)
if __name__ == '__main_':
    unittest.main()