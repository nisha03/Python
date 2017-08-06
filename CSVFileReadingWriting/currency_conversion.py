"""CSVReadingWriting"""
import sys
import getopt
from data_file import read_data, convert_data, write_data

def dollars_to_pounds(num):
    """dollars_to_pounds"""
    exchange_rate = 0.76
    return num * exchange_rate

def dollars_to_euro(num):
    """dollars_to_euro"""
    exchange_rate = 0.85
    return num * exchange_rate

def main():
    """main"""
    data = read_data("AAPL.csv")
    for arg in sys.argv[1:]:
        print arg
        if arg == '-h':
            print 'currency_conversion.py -dtp <to convert from dollars to pounds> OR'
            print 'currency_conversion.py -dte <to convert from dollars to euro>'
            sys.exit()
        elif arg == '-dtp':
            new_data = convert_data(data, dollars_to_pounds)
            write_data("convert_to_pounds.csv", new_data)
        elif arg == '-dte':
            new_data = convert_data(data, dollars_to_euro)
            write_data("convert_to_euro.csv", new_data)
    print "Convertion completed.."

if __name__ == "__main__":
    main()
