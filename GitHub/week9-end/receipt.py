import csv
from datetime import datetime



def main():
    try:
        products = read_dict('products.csv', 0)
        print ('\n\n-----PYTHON FUNCTIONS STORE-----\n\n')

        requests = {}

        with open("request.csv", "rt") as infile:
            reader = csv.reader(infile)

            next(reader)

            subtotal = 0

            for row in reader:
                key = row[0]
                quantity = row[1]
                quantity = float(quantity)

                ordered_items = products[key]
                name = ordered_items[1]
                price = ordered_items[2]
                price = float(price)

                subtotal += price * quantity

                print(f'{name}:     |{quantity}|    ${price}')
            print(" ")
            print(f'Subtotal: ${subtotal:.2f}')

            sales_tax = subtotal * 0.06
            sales_tax = float(sales_tax)
            print(f'Sales-tax: ${sales_tax:.2f}')

            total_amount = subtotal + sales_tax
            total_amount = float(total_amount)
            print(f'Total Amount: ${total_amount:.2f}')

            print('\n\n\n -----THANK YOU -----\n\n')

            current_date_and_time = datetime.now()
            print('\n\n')
            print(f'{current_date_and_time:%A %I %M %P}')

    except(FileNotFoundError, PermissionError) as error:
        print(error)
        print('Please choose a different file.')

    except ValueError as val_err:
        print('We have found this error {val_err}. Quantity that you have selected must be numbers only. If you need assistance, please call 000-123-4567.')

    except KeyError as key_error:
        print(f'Error: line {reader.line_num} of {infile.name} is'
        'formatted incorrectly.')


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
    products = {}#empty dictionary

    with open(filename, "rt") as infile:

        reader = csv.reader(infile)#create reader object

        next(reader)#skips first line

        for row in reader:#each key in products.csv
            key = row[0]
            name = row[1]
            price = row[2]
            
            products[key] = [key,name,price]
    return products

def read_request():
    requests = {}
    
    with open("request.csv", "rt") as infile:

        reader = csv.reader(infile)

        next(reader)

        for row in reader: 
            key = row[0]
            quantity = row[1]

            requests[key] = [key, quantity]
            print(requests[key])
    return requests
    
if __name__ == "__main__":
    main()