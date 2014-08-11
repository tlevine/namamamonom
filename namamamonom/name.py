import re
import csv

def is_name(column):
    '''
    column is an iterable of strings

    Is the column a name column?
    '''
    nones = 0
    names = 0
    others = 0
    for cell in column:
        if is_none(cell):
            nones += 1
        elif nword(cell) <= 3 and not hasdigits(cell) and contains_common_surname(cell) and len(cell) > 2:
            names += 1
        else:
            others += 1
    return others <3 * names

def _load_names(fn):
    'http://www.census.gov/genealogy/www/data/2000surnames/index.html'
    with open(fn) as fp:
        reader = csv.reader(fp)
        next(reader)
        for row in reader:
            yield row[0].lower()

NAMES = set(_load_names('/home/tlevine/git/namamamonom/data/app_c.csv'))

def is_none(text):
    return text.strip().lower() in {'', 'na', 'none'}

def contains_common_surname(text):
    for name in text.lower().strip().split():
        if name in NAMES:
            return True
    else:
        return False

def nword(text):
    'How many words are in a string?'
    return text.strip().count(' ') + 1

def hasdigits(text):
    '''
    Are there any digits in the string?
    If yes, this might be a street address
    rather than a name.
    '''
    return re.search(r'[0-9]', text) != None
