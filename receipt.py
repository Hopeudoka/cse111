# I exceeded the requirements. I added an invitation for an online
#survey. This is on line 92.

import csv
from datetime import datetime

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
    filename: the name of the CSV file to read.
      key_column_index: the index of the column
          to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    #create an empty dictionary that will store the data
    #from the csv file
    dictionary = {}
    #open the csv file for reading:
    with open(filename, "rt") as csv_file:
        #use the csv module to create a reader object to read
        #the file.
        reader = csv.reader(csv_file)
        #skip the first row because it contains the headings
        next(reader)
        #read the rows in the csv file one at a time.
        for row_list in reader:
            #if the current row is not blank, add the data from
            #from the current row to the dictionary.
            if len(row_list) != 0:
                #get the key from the current row.
                key = row_list[key_column_index]
                #store the data from the current row into the
                #dictionary.
                dictionary[key] = row_list
    #return the dictionary.
    return dictionary

def main():
    print("Hotty's Stores")
    #product number and quantity index
    PROD_NUM_INDEX = 0
    PROD_QUANTITY = 1
    #create total quantity and price variable and set each to 0
    total_quantity = 0
    total_price = 0
    #call the read_dictionary function and sore in a variable
    products_dict = read_dictionary("products.csv", PROD_NUM_INDEX)
    #print products_dict
    # print("ALL PRODUCTS:")
    # print(products_dict)
    #open request.csv file for reading
    with open("request.csv", "r") as request_file:
        #use the csv module reader to read the file
        reader = csv.reader(request_file)
        #skips the first line
        next(reader)
        #iterate over the rows in the file
        #print("REQUESTED ITEMS:")
        for row in reader:
            #access the product number in the current row
            prod_num = row[PROD_NUM_INDEX]
            quantity = int(row[PROD_QUANTITY])
            #access name and price
            product_details = products_dict[prod_num]
            product_name = product_details[1]
            product_price = float(product_details[2])
            #check if the product number is in the dictionary
            if prod_num in products_dict:
                print(f"{product_name}: {quantity} @ ${product_price}")
            #calculate the total quantity
            total_quantity += quantity
            #calculate the total price
            total_prod_price = product_price * quantity
            total_price += total_prod_price
            #calculate the sales taxs
            sales_tax = 0.06 * total_price
            #calculate total plus tax
            total = sales_tax + total_price
        
        print(f"Number of Items: {total_quantity}")
        print(f"Subtotal: ${total_price:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total:.2f}")
        #print Thank you message
        print(f"Thank you for shopping at Hotty's Store.")
        #print time and date
        date_and_time = datetime.now()
        formatted_date = date_and_time.strftime("%a %b %d %H:%M:%S %Y")
        print(formatted_date)
        print("We value your feedback. Please complete our online survey at www.hottystore.com/survey")

    try:
        product = products_dict[prod_num]
    except FileNotFoundError as not_found_err:
        print(f"{not_found_err}: please check that file location is correct and try again.")
    except PermissionError as perm_err:
        print(f"{perm_err}: You do not have permission to use this file. Try another file.")
    except KeyError as key_err:
        print(f"KeyError: {key_err}. Product with code '{prod_num}' not found.")


if __name__ == "__main__":
    main()