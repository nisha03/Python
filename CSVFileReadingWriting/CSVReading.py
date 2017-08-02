"""CSVReading"""
import csv
def read_data():
    """Read a CSV file using csv.DictReader"""
    with open("AAPL.csv", "rb") as file_obj:
        data = csv.DictReader(file_obj, delimiter=',')
        write_data(data)
        print "Convertion completed.."

def convert_data(data):
    """Convert data"""
    exchange_rate = 0.76
    data['Open'] = float(data['Open']) * exchange_rate
    data['High'] = float(data['High']) * exchange_rate
    data['Low'] = float(data['Low']) * exchange_rate
    data['Close'] = float(data['Close']) * exchange_rate
    data['Adj Close'] = float(data['Adj Close']) * exchange_rate
    return data

def write_data(data):
    """Writes a CSV file using DictWriter"""
    with open("convert.csv", "wb") as out_file:
        fieldnames = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
        writer = csv.DictWriter(out_file, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(convert_data(row))

if __name__ == "__main__":
    read_data()
