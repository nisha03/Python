"""CSVReading"""
import csv
def csv_reader(file_obj):
    """Read a CSV file using csv.DictReader"""
    reader = csv.DictReader(file_obj, delimiter=',')
    with open("convert.csv", "wb") as out_file:
        fieldnames = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
        writer = csv.DictWriter(out_file, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            print row["Date"],
            print row["Open"],
            print row["High"],
            print row["Low"],
            print row["Close"],
            print row["Adj Close"],
            print row["Volume"]
            csv_writer(writer, row)

def csv_writer(writer, data):
    """
    Writes a CSV file using DictWriter
    """
    writer.writerow(data)
    return

if __name__ == "__main__":
    with open("AAPL.csv", "rb") as file_obj:
        csv_reader(file_obj)
