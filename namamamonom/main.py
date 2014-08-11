from namamamonom.columns import read
from namamamonom.name import is_name

def main():
    import sys, csv
    writer = csv.writer(sys.stdout)
    writer.writerow(('name', 'is_name'))

    columns = read('/home/tlevine/csv-files/https/data.cityofnewyork.us/resource/feu5-w2e2.csv')
    for name, values in columns.items():
        result = 'name' in name.lower() and is_name(values)
        writer.writerow((name, result))
