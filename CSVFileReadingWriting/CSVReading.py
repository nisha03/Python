"""CSVReading"""
import csv
def read_data(file_obj):
    """Read data"""
    data = csv.DictReader(file_obj, delimiter=',')
    convert_data(data)

def convert_data(data):
    """Convert data"""
    exchange_rate = 0.76
    with open("convert.csv", "wb") as out_file:
        fieldnames = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
        writer = csv.DictWriter(out_file, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            row['Open'] = float(row['Open']) * exchange_rate
            row['High'] = float(row['High']) * exchange_rate
            row['Low'] = float(row['Low']) * exchange_rate
            row['Close'] = float(row['Close']) * exchange_rate
            row['Adj Close'] = float(row['Adj Close']) * exchange_rate
            write_data(writer, row)

def write_data(writer, data):
    """Write data"""
    writer.writerow(data)

if __name__ == "__main__":
    with open("AAPL.csv", "rb") as file_obj:
        read_data(file_obj)
    print "Convertion completed.."
