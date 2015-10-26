import unittest
import algo

class unitTest(unittest.TestCase):

    def test_simple(self):
        algo.randomPassWord(8)
        self.assertEqual(22,2)
        

if __name__ == "__main__":
##  unittest.main();
    algo.randomPassWord(8)