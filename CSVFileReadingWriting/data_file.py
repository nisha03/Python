"""dataFile"""
import csv

def read_data(csv_file):
    """Read data"""
    input_csv = []
    with open(csv_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            input_csv.append(row)
    return input_csv

def convert_data(data, f):
    """convert data"""
    new_data = []
    for row in data:        
        row['Open'] = f(float(row['Open']))
        row['High'] = f(float(row['High']))
        row['Low'] = f(float(row['Low']))
        row['Close'] = f(float(row['Close']))
        row['Adj Close'] = f(float(row['Adj Close']))
        new_data.append(row)
    return new_data

def write_data(csv_file, convert_csv):
    """write data"""
    with open(csv_file, "wb") as csvfile:
        fieldnames = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
        writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        for row in convert_csv:
            writer.writerow(row)
            