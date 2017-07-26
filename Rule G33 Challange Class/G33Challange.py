"""G33Challange"""
import sys
import ruleg33function
from ruleg33function import calc_accuredinterest, calc_dollarprice, calc_yield
print "Rule G33 Challange"
class G33Challange(object):
    """G33Challange"""
    def __init__(self):
        self.choice = ""
        self.num = 0
    def ask(self):
        """ask"""
        while True:
            choice = raw_input("Accrued Interest (A), Dollar Price (D), Yield (Y) or Quit (Q):")
            if choice == "Q\r":
                print "Good Bye..."
                sys.exit()
            num = float(raw_input('Enter a number:'))
            if choice == "A\r":
                print "Accured Interest: ", calc_accuredinterest(num)
            elif choice == "D\r":
                print "Dollar Price: ", calc_dollarprice(num)
            elif choice == "Y\r":
                print "Yield: ", calc_yield(num)
        self.choice = choice
        self.num = num

if __name__ == '__main__':
    prog = G33Challange()
    prog.ask()
    