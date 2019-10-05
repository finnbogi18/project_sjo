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


def get_monthly_average(data_list, date_list):
    month_counter = 0
    month_tuple = ()
    average_list = []
    acv_sum = 0
    vol_sum = 0
    for i in data_list[1:]:
        temp_var = i[DATE]
        temp_var = temp_var[:7]
        if temp_var == date_list[month_counter]:
            acv_sum += float(i[ADJ_CLOSE]) * float(i[VOLUME])
            vol_sum += float(i[VOLUME])
        else:
            month_avg = acv_sum / vol_sum
            month_tuple = (date_list[month_counter], month_avg)
            average_list.append(month_tuple)
            acv_sum = 0
            vol_sum = 0
            month_counter += 1

    return average_list


def find_highest(data_list):
    highest_price = 0.00
    high_date = ""
    for i in data_list[1:]:
        temp_var = float(i[ADJ_CLOSE])
        if temp_var > highest_price:
            highest_price = temp_var
            high_date = i[DATE]

    high_tuple = (highest_price, high_date)
    return high_tuple


def print_info(average_list, highest_tuple):
    print("{:<10}{:>7}".format("Month", "Price"))
    for i in average_list:
        print("{:<10}{:>7.2f}".format(i[0], i[1]))


filename = input("Enter filename: ")
file_object = open_file(filename)
data_list = get_data_list(file_object)
date_list = date_list(data_list)
print(date_list)
average_list = get_monthly_average(data_list, date_list)
print(average_list)
highest_tuple = find_highest(data_list)
print_info(average_list, highest_tuple)
