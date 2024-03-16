import json
import csv


# this function save 2D array to json file:
def write_json(table, filename):
    with open(filename, 'w') as file:
        json.dump(table, file)


# this function save 2D array to csv file:
def write_csv(data_array, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['INFO', 'SALE', 'AREA', 'LOCATION', 'DATETIME', 'URL'])
        writer.writerows(data_array)

