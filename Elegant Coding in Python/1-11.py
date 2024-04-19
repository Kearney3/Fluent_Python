"""读取一个csv文件"""

import csv

# Wrong way
with open('example.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1

    print(f'Processed {line_count} lines.')

# Right way
def process_by_line(csv_reader):
    """Process each line of the csv file"""
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')

with open('example.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    process_by_line(csv_reader)