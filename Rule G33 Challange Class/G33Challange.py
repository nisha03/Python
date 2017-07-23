"""G33Challange"""
import sys
import ruleg33function
from ruleg33function import calc_accuredinterest, calc_dollarprice, calc_yield
print "Rule G33 Challange"
class G33Challange(object):
    """G33Challange"""
    def __init__(self):
        self.choice = raw_input("Accrued Interest (A), Dollar Price (D), Yield (Y) or Quit (Q):")
        if self.choice == "Q\r":
            print "Good Bye..."
            sys.exit()
        self.num = float(raw_input('Enter a number:'))

    def g33calculate(self):
        """g33calculate"""
        if self.choice == "A\r":
            calc_accuredinterest(self.num)
        elif self.choice == "D\r":
            calc_dollarprice(self.num)
        elif self.choice == "Y\r":
            calc_yield(self.num)
