from namamamonom.columns import read

def main():
    columns = read('/home/tlevine/csv-files/https/data.cityofnewyork.us/resource/feu5-w2e2.csv')
    print(columns)
