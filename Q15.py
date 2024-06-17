# Q15. Write a program that reads data from a CSV file and prints it to the console

import csv

with open('data.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')       # Creating a reader object

    for row in csvreader:                                # Printing each row of the file
        print(', '.join(row))
