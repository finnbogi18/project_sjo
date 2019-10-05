''' This program takes a .csv file that the user inputs, then the program reads 
    the file and finds the average price for each month
    and prints out the average price and the month of that price, 
    finally it prints out the year-month-day of the highest price '''

DATE = 0
ADJ_CLOSE = 5
VOLUME = 6


def open_file(filename):
    try:
        file_object = open(filename, "r")
        return file_object

    except FileNotFoundError:
        print("Filename {} not found!".format(filename))


def get_data_list(file_object):
    data_list = []
    for line_str in file_object:
        data_list.append(line_str.strip().split(","))
    return data_list


def date_list(data_list):
    date_list = []
    for i in range(1, len(data_list)):
        temp_var = data_list[i][DATE]
        temp_var = temp_var[:7]
        if temp_var not in date_list:
            date_list.append(temp_var)

    return date_list


filename = input("Enter filename: ")
file_object = open_file(filename)
data_list = get_data_list(file_object)
date_list = date_list(data_list)
print(date_list)