import argparse

from namamamonom.columns import read
from namamamonom.name import is_name

parser = argparse.ArgumentParser()
parser.add_argument('filename', nargs = '+')

def main():
    args = parser.parse_args()

    import sys, csv
    writer = csv.writer(sys.stdout)
    writer.writerow(('filename', 'name', 'is_name'))

    for filename in args.filename:
        columns = read(filename)
        for name, values in columns.items():
            result = 'name' in name.lower() and is_name(values)
            writer.writerow((filename, name, result))
