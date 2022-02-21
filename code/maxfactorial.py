import sys
def findMaxValue():
 
    res = 2;
    fact = 2;
    while (True):
         
        # when fact crosses its size
        # it gives negative value
        if (fact < 0 or fact > sys.maxsize):
            break;
        res += 1;
        fact = fact * res;
    return res - 1;

     
