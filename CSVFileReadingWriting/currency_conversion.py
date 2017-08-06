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
    for arg in sys.argv[1:]:
        print arg
    data = read_data("AAPL.csv")
    new_data = convert_data(data, dollars_to_pounds)
    write_data("convert.csv", new_data)
    print "Convertion completed.."

if __name__ == "__main__":
    main()
