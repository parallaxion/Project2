import csv
import json
from pprint import pprint

with open('countries.geo.json') as f:
    data = json.load(f)

#pprint(data)
with open('countries.csv') as f:
    data = csv.reader(f, delimiter=' ')