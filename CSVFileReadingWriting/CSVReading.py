"""CSVReading"""
import csv
def csv_reader(file_obj):
    """csv_reader"""
    reader = csv.reader(file_obj)
    for row in reader:
        print " ".join(row)

if __name__ == "__main__":
    file_path = "AAPL.csv"
    with open(file_path, "rb") as file_obj:
        csv_reader(file_obj)
