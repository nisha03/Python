"""CSVReadingWriting"""
from data_file import read_data, convert_data, write_data

def dollars_to_pounds(num):
    """dollars_to_pounds"""
    exchange_rate = 0.76
    return num * exchange_rate

def main():
    """main"""
    data = read_data("AAPL.csv")
    new_data = convert_data(data, dollars_to_pounds)
    write_data("convert.csv", new_data)
    print "Convertion completed.."

if __name__ == "__main__":
    main()
