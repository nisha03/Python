"""CSVReadingWriting"""
import csv
input_csv = []
convert_csv = []
def read_data(csv_file):
    """Read data"""
    with open(csv_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            input_csv.append(row)

def convert_data(data):
    """Read data"""
    exchange_rate = 0.76
    data['Open'] = float(data['Open']) * exchange_rate
    data['High'] = float(data['High']) * exchange_rate
    data['Low'] = float(data['Low']) * exchange_rate
    data['Close'] = float(data['Close']) * exchange_rate
    data['Adj Close'] = float(data['Adj Close']) * exchange_rate
    return data

def write_data(csv_file):
    """Read data"""
    with open(csv_file, "wb") as csvfile:
        fieldnames = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
        writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        for row in convert_csv:
            writer.writerow(row)

if __name__ == "__main__":
    read_data("AAPL.csv")
    for row in input_csv:
        convert_csv.append(convert_data(row))
        write_data("convert.csv")
    print "Convertion completed.."
