from pathlib import Path #import the Path library
import csv #Import the csv library

filepath = ("Pybank/Resources/budget_data.csv") #Define the filepath

with open (filepath, 'r') as csvfile: # Read the csv file
    
    csvreader = csv.reader(csvfile, delimiter = ',') #Separate the data by comma
    
    

    #skip the header
    header = next(csvreader)
    
    #Declare the variables:
    header_test = []
    count = -1
    amount = 0
    total = 0
    maximum = 0
    difference = 0
    minimum = float('inf')
    greatest_profit = {}
    greatest_loss = {}
    one_shot = False
    previous = 0
    future = 0
    net_increase = 0
    
    #convert the csv file into a list
    rows = list(csvreader)
    
    
    #Loop through each row in the list
    for row in rows:
        
        count += 1 #Counter that helps me calculate the difference between profits/losses by ignoring the first value
        amount += 1 #Total number of transactions
        total += int(row[1]) #Total amount of profits and losses
        
        if count > 0:
            
            previous = int(rows[count-1][1]) #Set my first value

            future = int(row[1]) #set my next value
            difference = future - previous #calculate the difference between the first value and the next value

            net_increase = net_increase + difference #total value of changes
                    
        if difference > maximum: #find the maximum value of differences
            maximum = difference
            positive_month = row [0]
            
        if difference < minimum: #calculate the minimum value of differences
            minimum = difference
            negative_month = row[0]
            
greatest_profit [positive_month] = f'${maximum:,}'
greatest_loss [negative_month] = f'${minimum:,}'
average = net_increase/count

# for key, value in greatest_profit:
    
print ("Financial Analyses")
print ("--------------------------------")
print (f'Total Months: {amount}')
print (f'Total : ${total:,}')
print (f'Average Change: ${average:,.2f}')
print (f'Greatest Increase in profits: {list(greatest_profit.keys())[0]} ({list(greatest_profit.values())[0]})')
print (f'Greatest Decrease in profits: {list(greatest_loss.keys())[0]} ({list(greatest_loss.values())[0]})')


