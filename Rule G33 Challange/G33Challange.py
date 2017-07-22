"""rule_g33_challange"""
import ruleg33function
from ruleg33function import calc_accuredinterest, calc_dollarprice, calc_yield
print "Rule G33 Challange"
def init():
    """init"""
    while True:
        choice = raw_input("Accrued Interest (A), Dollar Price (D), Yield (Y) or Exit (E):")
        if choice == "E\r":
            break
        elif choice == "A\r":
            num = float(raw_input('Enter a number:'))
            calc_accuredinterest(num)
        elif choice == "D\r":
            num = float(raw_input('Enter a number:'))
            calc_dollarprice(num)
        elif choice == "Y\r":
            num = float(raw_input('Enter a number:'))
            calc_yield(num)
        print choice
    print "Good bye!"

if __name__ == '__main__':
    init()
