"""CSVReading"""
import csv
def csv_reader(file_obj):
    """Read a CSV file using csv.DictReader"""
    reader = csv.DictReader(file_obj, delimiter=',')
    with open("convert.csv", "wb") as out_file:
        fieldnames = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
        writer = csv.DictWriter(out_file, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        exchange_rate = 0.757221
        for row in reader:
            csv_writer(writer, row, exchange_rate)
    print "Convertion completed.."

def csv_writer(writer, data, exchange_rate):
    """
    Writes a CSV file using DictWriter
    """
    data['Open'] = float(data['Open']) *  exchange_rate
    data['High'] = float(data['High']) *  exchange_rate
    data['Low'] = float(data['Low']) *  exchange_rate
    data['Close'] = float(data['Close']) *  exchange_rate
    data['Adj Close'] = float(data['Adj Close']) *  exchange_rate
    writer.writerow(data)

if __name__ == "__main__":
    with open("AAPL.csv", "rb") as file_obj:
        csv_reader(file_obj)
