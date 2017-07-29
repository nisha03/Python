"""CSVReading"""
import csv
def csv_reader(file_obj):
    """Read a CSV file using csv.DictReader"""
    reader = csv.DictReader(file_obj, delimiter=',')
    for row in reader:
        print row["Date"],
        print row["Open"],
        print row["High"],
        print row["Low"],
        print row["Close"],
        print row["Adj Close"]

if __name__ == "__main__":
    with open("AAPL.csv", "rb") as file_obj:
        csv_reader(file_obj)
