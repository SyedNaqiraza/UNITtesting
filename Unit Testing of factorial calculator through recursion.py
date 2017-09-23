Unit Testing of Factorial Function through recursion 
# First of all i will write program for calculating factorial function in Python 
class factorial:   # This is the header file of class
    def fact(self,num):
        ans=num
        Fact=0
        Type =type(ans)
        if (Type==int):    # check case no 1 if it is int its okay
          if (ans<0):      # check case no 2 is it is less than zero
             print("Sorry not possible")
             return False
          if (ans>999):
            print ("Max depth of stack overflowed ")
            return False
          if (ans == 1 or ans==0):
            return 1
          else:
            temp=ans
            temp=temp-1
            return ans * self.fact(temp)
        else:
            print ("Sorry input is not int type")
            return False
            ################################################################# Header File ################################
            ################################UNIT TEST###########################
import unittest
from headerfact import factorial
class mytests(unittest.TestCase):
  def test_equalanswer(self):
   FF=factorial()
   self.assertEqual(FF.fact(8), 40320)
  def test_char(self):
      FF=factorial()
      self.assertEqual(FF.fact('a'),False)
  def test_negative(self):
      FF=factorial()
      self.assertEqual(FF.fact(-39),False)
  def test_overflow(self):
      FF=factorial()
      self.assertEqual(FF.fact(1000),False)

if __name__ == '__main__':
    unittest.main()

            
