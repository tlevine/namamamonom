import csv
from collections import defaultdict

def read(fn):
    columns = defaultdict(lambda: [])
    with open(fn) as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            for key, value in row.items():
                columns[key].append(value)
    return columns
