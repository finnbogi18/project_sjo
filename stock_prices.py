''' This program takes a .csv file that the user inputs, then the program reads 
    the file and finds the average price for each month
    and prints out the average price and the month of that price, 
    finally it prints out the year-month-day of the highest price '''

import csv


def open_file(filename):
    try:
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            line_count = 0
            temp_list = []
            main_data = []
            for row in csv_reader:
                temp_list.append(row)
                main_data.append(temp_list)
                line_count += 1
            return main_data, line_count

    except FileNotFoundError:
        print("Filename {} not found!".format(filename))