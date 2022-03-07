

import csv

def main():
    I_NUMBER_INDEX = 0
    NAME_INDEX = 1
    students_dict = read_dict('students.csv', I_NUMBER_INDEX)
    i_number = input('What is an I-number: ')
    i_number = i_number.replace('-' '')
    
    if i_number not in students_dict:
        print('Input no in database')
    else:
        value = students_dict[i_number]
        name = value[NAME_INDEX]
        print(name)


def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    comp_dictionary = {}
    with open(filename, 'rt') as csv_file:
        reader = csv.reader(csv_file)

    next(reader) 
    
    for row in reader:
        key = row[key_column_index]
        comp_dictionary[key] = row
    return comp_dictionary

main()