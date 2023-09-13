# Code by Zac Doruk Maslen, UWA Student ID: 23630652
# Python Project 1 for CITS1401 @ UWA

csvfile = 'Organisations.csv'
country = 'Belgium'

# File reader
def read_csv_file(file_path):
    # Initialize empty list
    data = []
    # Try statement to check whether CSV file returns an error
    try:
        # With statement used to automatically close the file after completing the operation
        # Parameters file_path for file location and 'r' for read
        with open(file_path, 'r') as file:
            # Initiate lines var as CSV split into strings separated by lines
            lines = file.readlines()
        # For loop, running through list stripping empty spaces before and after
        for line in lines:
            # Then splitting each dataset by a comma
            values = line.strip().split(',')
            values = [value.lower() for value in values]
            # Append data var list with each dataset
            data.append(values)
    except FileNotFoundError:
        return None
    return data

# Function to find min and max
def find_min_max(data, country):
    min_max = []
    filtered_data = [line for line in data[1:] if 1981 <= int(line[4]) <= 2000]
    matching_sublists = [sublist for sublist in filtered_data if any(country in item for item in sublist)]
    max_company = ""
    min_company = ""
    max_value = 0
    min_value = float('inf')

    if len(matching_sublists) > 1:
        for line in matching_sublists:
            if int(line[6]) < min_value:
                min_value = int(line[6])
                min_company = line[1]
            if int(line[6]) > max_value:
                max_value = int(line[6])
                max_company = line[1]

        min_max = [max_company, min_company]
        return min_max
    else:
        return None

# Function to calculate standard deviation
def calculate_std_dev(data, country):
    filtered_data = [line for line in data[1:]]
    matching_sublists = [sublist for sublist in data[1:] if any(country in item for item in sublist)]
    c_med_salary = [int(line[7]) for line in matching_sublists]
    w_med_salary = [int(line[7]) for line in filtered_data]

    # By Country
    if len(c_med_salary) > 1:
        c_mean = sum(c_med_salary) / len(c_med_salary)  # Calculate the mean (average)
        c_squared_diff = [(x - c_mean) ** 2 for x in c_med_salary]  # Calculate squared differences
        c_variance = sum(c_squared_diff) / (len(c_med_salary) - 1)  # Calculate variance with n-1 degrees of freedom
        c_std_dev = c_variance ** 0.5  # Calculate standard deviation
        c_std_dev = round(c_std_dev, 4)
    else:
        return None

    # Whole Data Set
    w_mean = sum(w_med_salary) / len(w_med_salary)
    w_squared_diff = [(x - w_mean) ** 2 for x in w_med_salary]
    w_variance = sum(w_squared_diff) / (len(w_med_salary) - 1)
    w_std_dev = w_variance ** 0.5
    w_std_dev = round(w_std_dev, 4)

    # Combining the two
    std_dev = [c_std_dev, w_std_dev]

    return std_dev

# Function to calculate ratio
def calculate_ratio(data, country):
    filtered_data = [line for line in data[1:]]
    matching_sublists = [sublist for sublist in filtered_data if any(country in item for item in sublist)]
    profit_increases = 0
    profit_decreases = 0

    for line in matching_sublists:
        profit_calc = int(line[9]) - int(line[8])
        if profit_calc > 0:
            profit_increases += profit_calc
        if profit_calc < 0:
            profit_decreases += profit_calc
    if profit_decreases != 0:
        ratio = profit_increases / abs(profit_decreases)
    else:
        return None

    ratio = round(ratio, 4)
    return ratio

# Function to calculate correlation
def calculate_correlation(data, country):
    filtered_data = [line for line in data[1:]]
    matching_sublists = [sublist for sublist in filtered_data if any(country in item for item in sublist)]

    # Extract two variables you want to find the correlation for (e.g., column 8 and column 9)
    variable1 = [int(line[7]) for line in matching_sublists]
    variable2 = [int(line[9]) for line in matching_sublists]

    print(variable1)
    print(variable2)

    # Check if there are enough data points for correlation calculation
    if len(variable1) < 2:
        return None

    # Calculate the mean (average) for both variables
    mean1 = sum(variable1) / len(variable1)
    mean2 = sum(variable2) / len(variable2)

    print(len(variable1))
    print(len(variable2))
    print(mean1)
    print(mean2)

    # Calculate the numerator and denominators for correlation calculation
    numerator = sum((x - mean1) * (y - mean2) for x, y in zip(variable1, variable2))
    print(numerator)
    denominator1 = sum((x - mean1) ** 2 for x in variable1)
    denominator2 = sum((y - mean2) ** 2 for y in variable2) 


    # Calculate the correlation coefficient (Pearson correlation)
    if denominator1 == 0 or denominator2 == 0:
        return None
    else:
        correlation_coefficient = numerator / ((denominator1 ** 0.5) * (denominator2 ** 0.5))
        correlation_coefficient = round(correlation_coefficient, 4)
        return correlation_coefficient

# Main code for statistical analysis
def main(csvfile, country):
    # Parse CSV contents
    data = read_csv_file(csvfile)

    # if there is nothing in CSV return empty
    if data == None:
        return [], [], 0, 0 # Returns empty result of data set

    country = country.lower() # cap insensitive

    return find_min_max(data, country), calculate_std_dev(data, country), calculate_ratio(data, country), calculate_correlation(data, country)

result = main(csvfile, country)
print(result)