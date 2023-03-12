#Importing the csv module
import csv 

#Importing the json module
import json

      
# Open the CSV file
with open('acw_user_data.csv', mode='r', encoding = 'utf-8') as csv_file:
    # Create a CSV reader object
    csv_reader = csv.DictReader(csv_file)


    # Create an empty list
    dict_list = []

    # Loop through each row in the CSV file
    for row in csv_reader:
        details = {'Address' : {'Street' : row['Address Street'], 
                                'City' : row['Address City'], 
                                'PostCode' : row['Address Postcode']},
                   
                   'Age(Years)' : row['Age (Years)'], 
                   
                   'Distance to Work(miles)' : row['Distance Commuted to Work (miles)'], 
                   
                   'Employer Company' : row['Employer Company'],
                   
                   'Credit Card' : {'Start Date' : row['Credit Card Start Date'], 
                                    'Expiry Date' : row['Credit Card Expiry Date'],
                                    'Number' : row['Credit Card Number'], 
                                    'CVV' : row['Credit Card CVV']}, 
                   
                   'Dependants' : row['Dependants'],
                   
                   'First Name' : row['First Name'],
                   
                   'Last Name' : row['Last Name'],
                   
                   'Bank IBAN' : row['Bank IBAN'],
                   
                   'Marital Status' : row['Marital Status'],
                   
                   'Yearly Pension(GBP)' : row['Yearly Pension (GBP)'],
                   
                   'Retired' : row['Retired'],
                   
                   'Yearly Salary(GBP)' : row['Yearly Salary (GBP)'],
                   
                   'Sex' : row['Sex'],
                   
                   'Vehicle' : {'Make' : row['Vehicle Make'],
                                'Model' : row['Vehicle Model'],
                                'Year' : row['Vehicle Year'],
                                'Type' : row['Vehicle Type']}
            }
        
        
        
        #Appending or adding the details of each employee to the list.
        dict_list.append(details)
        

# Write the dictionary to a JSON file
with open('processed.json', mode='w', encoding = 'utf-8') as json_file:
    json.dump(dict_list, json_file, indent=4)
        
        



        

    
