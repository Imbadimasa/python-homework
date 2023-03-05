# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# @TODO: Import libraries
import csv
from pathlib import Path
import json
import collections
from pprint import pprint

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('Resources/menu_data.csv')
sales_filepath = Path('Resources/sales_data.csv')


# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []
menuitem_quantity = []
menu_items = []
quantity_of_sales_items = []
quantity_dict = {}



# @TODO: Read in the menu data into the menu list

with open (menu_filepath, 'r') as csvfile_menu:
    
    menu_csv = csv.reader(csvfile_menu, delimiter = ',')
    
    header1 = next(menu_csv)
    
    for menu_item in menu_csv:
        menu.append(menu_item)
    


    
    
    
# @TODO: Read in the sales data into the sales list

with open (sales_filepath, 'r') as csvfile_sales:
    
    sales_scv = csv.reader(csvfile_sales, delimiter = ',')
    
    header = next(sales_scv)
    
    for row2 in sales_scv:
        # print (row2)
        sales.append(row2)


#Decided not to use the report value
# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {
    
    "01-count": 0,
    "02-revenue": 0,
    "03-cogs": 0,
    "04-profit": 0,
} 


# @TODO: Loop over every row in the sales list object

for sale_item in sales:
    
    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # @TODO: Initialize sales data variables
    
    menu_items.append(sale_item [4])

menu_items = list(dict.fromkeys(menu_items))    


    # Added quantities sold to a separate dictionary called quantity_dict. I am only including the items that were actually sold

for items in menu_items:
    quantity_dict [items] = 0


for sale_item in sales:
    for key, value in quantity_dict.items():
        if sale_item[4] == key:
            quantity_dict[key] += int(sale_item[3])


            
            
            
    # Created a new dictionary that will hold the full information about the items: Quantity, Price, Cost, Revenue, Cogs, Profit
sales_dict = collections.defaultdict(dict)

for key, value in quantity_dict.items():
    sales_dict [key]["quantity"] = value
    

for menu_item in menu:
    for key, value in sales_dict.items():
        if menu_item[0] == key:
            sales_dict [key]["price"] = menu_item[3]
            sales_dict [key]["cost"] = menu_item[4]
            sales_dict [key]["revenue"] = int(sales_dict [key]["price"]) * int(sales_dict [key]["quantity"]) 
            sales_dict [key]["cogs"] = int(sales_dict [key]["cost"]) * int(sales_dict [key]["quantity"]) 
            sales_dict [key]["profit"] = int(sales_dict [key]["revenue"]) - int(sales_dict [key]["cogs"]) 
            
            
        # Printed the values of the sales dictionary just to check
        
print (json.dumps(sales_dict, indent = 4, sort_keys=True))


        # Wrote the results to a text file
    
with open('results.txt', 'w') as file:
     file.write(json.dumps(sales_dict, indent = 4, sort_keys=True))
    
    
    
    ##################################################################
    
    # The rest of the steps were not used
    
    ##################################################################
    
    
    
    
    # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit








    # @TODO: For every row in our sales data, loop over the menu records to determine a match


        # Item,Category,Description,Price,Cost
        # @TODO: Initialize menu data variables




        # @TODO: Calculate profit of each item in the menu data


        # @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item


            # @TODO: Print out matching menu data






            # @TODO: Cumulatively add up the metrics for each item key


            
            



        # @TODO: Else, the sales item does not equal any fo the item in the menu data, therefore no match



    # @TODO: Increment the row counter by 1


# @TODO: Print total number of records in sales data




# @TODO: Write out report to a text file (won't appear on the command line output)
