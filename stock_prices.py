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

def get_monthly_averages(data_list):
    rows = len(data_list)
    for i in rows:
        

def date_splitter(data_list, i):
    row = i
    date_list = data_list[row][DATE].split("-")
    
    return date_list


filename = input("Enter filename: ")
file_object = open_file(filename)
data_list = get_data_list(file_object)