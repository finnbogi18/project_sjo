''' This program takes a .csv file that the user inputs, then the program reads 
    the file and finds the average price for each month
    and prints out the average price and the month of that price, 
    finally it prints out the year-month-day of the highest price '''

# Constants for the colums in the data list.
DATE = 0
ADJ_CLOSE = 5
VOLUME = 6


def open_file(filename):
    ''' This function opens the file and returns a file object,
        if the file doesn't exist it prints out an error '''
    try:
        file_object = open(filename, "r")
        return file_object

    except FileNotFoundError:
        print("Filename {} not found!".format(filename))


def get_data_list(file_object):
    ''' This function creates a list of lists
        for the dates and stock prices '''
    data_list = []
    
    for line_str in file_object:
        data_list.append(line_str.strip().split(","))  # Appends a list that splits at "," and then adds that to the main data list.

    return data_list


def get_date_list(data_list):
    ''' This function creates a list of the dates, with the days removed
        return the list with the following format: "YYYY-MM"
        allowing the user for easier navigation when calculating averages '''
    date_list = []
    
    for i in range(1, len(data_list)):
        temp_var = data_list[i][DATE]
        temp_var = temp_var[:7]

        if temp_var not in date_list:
            date_list.append(temp_var)

    return date_list


def get_monthly_average(data_list, date_list):
    ''' This functions reads the data list and calculates
        the average stock price for each month and returns
        the average price and the associated month as a list of tuples '''
    month_counter = 0
    month_tuple = ()
    average_list = []
    acv_sum = 0.0
    vol_sum = 0.0
    
    for i in data_list[1:]:
        temp_var = i[DATE]
        temp_var = temp_var[:7]

        if temp_var == date_list[
                month_counter]:  # Checks if the current month matches the month being calcuated
            acv_sum += float(i[ADJ_CLOSE]) * float(i[VOLUME])
            vol_sum += float(i[VOLUME])

        else:  # If the months changes it calculates the average and adds the month and average to a tuple.
            month_avg = acv_sum / vol_sum
            month_tuple = (date_list[month_counter], month_avg)
            average_list.append(month_tuple)  # Adds the tuple to the main average list.
            acv_sum = 0.0
            vol_sum = 0.0
            month_counter += 1
            #  Adds the first day of the new month as the starting sums.
            #  Because it's used to evaluate if a new month has begun causing it to be left out
            #  of the new month.
            acv_sum += float(i[ADJ_CLOSE]) * float(i[VOLUME])
            vol_sum += float(i[VOLUME])

    #  Adds the last month to the list.
    month_avg = acv_sum / vol_sum
    month_tuple = (date_list[month_counter], month_avg)
    average_list.append(month_tuple)

    return average_list


def find_highest(data_list):
    """ This function finds the highest stock price in the whole list
        and returns a tuple with the date and the price as a tuple."""
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
    """ This function prints out the average price for each month in the time period that is given with the .csv file. 
    And lastly it prints out the price and date of the highest stock."""
    print("{:<10}{:>7}".format("Month", "Price"))

    for i in average_list:
        print("{:<10}{:>7.2f}".format((i[0]),i[1]))

    print("Highest price {:.2f} on day {}".format(highest_tuple[0], highest_tuple[1]))


def main(file_object):
    """ The main function only runs most of the functions in the program. 
        If the file name entered by the user is wrong then this function wont run. """
    data_list = get_data_list(file_object)
    date_list = get_date_list(data_list)
    average_list = get_monthly_average(data_list, date_list)
    highest_tuple = find_highest(data_list)
    print_info(average_list, highest_tuple)


filename = input("Enter filename: ")
file_object = open_file(filename)

if file_object != None:
    main(file_object)
