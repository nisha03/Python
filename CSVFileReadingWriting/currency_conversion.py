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

def dollars_to_roman(num):
    """dollars_to_roman"""
    roman_numerals = []
    to_str = str(num)
    split_str1, split_str2 = to_str.split(".")
    rocks = int(split_str1)
    pebbles = int(split_str2[0:0+1])
    roman_table = [("M", 1000), ("CM", 900), ("D", 500), ("CD", 400), ("C", 100),
                   ("XC", 90), ("L", 50), ("XL", 40), ("X", 10), ("IX", 9), ("V", 5),
                   ("IV", 4), ("I", 1)]
    if rocks > 0:
        for numeral, value in roman_table:
            while value <= rocks:
                rocks -= value
                roman_numerals.append(numeral)
        roman_numerals.append(' Rocks ')
    elif rocks <= 0:
        roman_numerals.append(' NO Rocks ')
    if pebbles > 0:
        for numeral, value in roman_table:
            while value <= pebbles:
                pebbles -= value
                roman_numerals.append(numeral)
        roman_numerals.append(' pebbles')
    return ''.join(roman_numerals)

def main():
    """main"""
    data = read_data("AAPL.csv")
    for arg in sys.argv[1:]:
        print arg
        if arg == '-h':
            print 'currency_conversion.py -dtp <to convert from dollars to pounds> OR'
            print 'currency_conversion.py -dte <to convert from dollars to euro> OR'
            print 'currency_conversion.py -dtr <to convert from dollars to roman>'
            sys.exit()
        elif arg == '-dtp':
            new_data = convert_data(data, dollars_to_pounds)
            write_data("convert_to_pounds.csv", new_data)
        elif arg == '-dte':
            new_data = convert_data(data, dollars_to_euro)
            write_data("convert_to_euro.csv", new_data)
        elif arg == '-dtr':
            new_data = convert_data(data, dollars_to_roman)
            write_data("convert_to_roman.csv", new_data)
    print "Convertion completed.."

if __name__ == "__main__":
    main()
