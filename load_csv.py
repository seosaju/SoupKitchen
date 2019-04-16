import csv


def load(path):
    with open(path, 'r', encoding='cp949') as f:
        reader = csv.reader(f)
        csv_list = list(reader)[1:]
    return csv_list
