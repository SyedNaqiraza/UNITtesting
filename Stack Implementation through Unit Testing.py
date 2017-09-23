################## Code ###############
class stack:
    def push(self,Input,size):
        sizelist=size
        inp=Input
        if (len(list)<=size):
         list.append(inp)
         print "Done"
         return True
        else:
            print("Size overflow")
            return False
    def pop(self):
        check = len(list)
        if (check==0):
            print ("No element presend in the list ")
            return False
        else:

            check=check-1
            temp=list[check]
            print "Popped Element", temp
            list.pop()
            return True

list=[]



##################### Unit Testing #######################
from stackheader import stack
import unittest
class mytests(unittest.TestCase):
  def test_equalanswer(self):
   FF=stack()
   for i  in range(0,5):
     self.assertEqual(FF.push(8,5),True )
  def test_pop(self):
      FF=stack()
      for i in range(0,5):
          self.assertEqual(FF.pop(),True)

if __name__ == '__main__':
    unittest.main()
