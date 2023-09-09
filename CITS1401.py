#Code by Vincent Jeff Liu, UWA Student ID: 23777635
# python project 1 for CITS1401

# we need to find a way to manage the csv file data so we can edit it and access it easier and in its orders 
# so we using a dictionary 

# The below file object is created with the understanding that the csv file is in the same repository as the code, if its not it needs to be changed 
#Data_on_organisations = open("Organisations.csv","r") # this creates a file object, the object is set to read which only allows us to read the data about organisations
# note the file is meant to take an output from the 

upper_year_limit = 2000
lower_year_limit = 1981

def csv_file_appender(csvfile): # makes sure the file has the .csv ending to allow for correct file call 
    if ".csv" not in csvfile:
        #print("csv not present")
        #print(csvfile)
        csvfile = csvfile +".csv"
        #print(csvfile)
    return csvfile

def lowercase_initial_country(target_country_name): # lowecases the inputed country
    return target_country_name.lower()

def csv_to_dict(file_name):# file_name can be the path with the file name 
    Data_on_organisations = open(file_name,"r") # this creates a file object, the object is set to read which only allows us to read the data about organisations
    # note the file is meant to take an output from the 

    first_line_of_file = Data_on_organisations.readline() # this reads the topline of the file and returns it as a single string, readline adds a \n we need to get rid of this
    first_line_of_file.rstrip("\n")
    #tester#print(first_line_of_file.replace("\n",""))
    first_line_of_file = first_line_of_file.replace("\n","") # this gets rid of the \n from the first line, the .replace will output a copy of the string so needs to be set to a variable to be used 
    list_of_headings = first_line_of_file.split(",") # this turns the string from the topline of the file into a list with each item being the respective headers, .split() outputs a copy of the list 
    #tester#print(list_of_headings)

    dict_of_org_data ={} # empty dictionary where all the org data will be sorted into 
    i = 0 # defining var i for for loop
    for i in list_of_headings: # this for loop adds dictionary items with the key being the header words and the value of the key is an empty list to add the header specific data to
        dict_of_org_data[i] = []

    list_of_org_dict_keys = list(dict_of_org_data)
    #tester#print(list_of_org_dict_keys[0])

    for line in Data_on_organisations:# this for loop loops through the remaining lines in csv file and sorts the data into the dictionary 
        line = line.replace("\n","") # gets rid of the "\n", the replace function needs to be set to an variable as it outputs a copy of the list
        #tester#print(line)
        current_line_list = line.split(",") # this turns the current line's string into a list, with each item corresponding to a key in the dictionary 
        a = 0     # iterator 
        for item in current_line_list: # this moves the data from each list object to the corresponding dictionary list to group data together in its categories 
            dict_of_org_data[list_of_org_dict_keys[a]].append(item) # list_of_org_dict_keys[a] gives the corresponding key, var a makes sure the key changes to the right one to allow for list appending, 
            #print(dict_of_org_data[list_of_org_dict_keys[a]])
            a += 1 #adds to a so its the correct list 
    return [dict_of_org_data, list_of_org_dict_keys] # the function returns a list which contains the dictionary with all the sorted data and also the list of dictionary keys 

def rangecheck(lowrange,highrange,pos_list,pos_header,csv_dict): # checks poslit item's (list of location of items of valid countries) years is within int lowrange and int highrange inclusive, outputs positions that match
    valid_pos = [] # empty list to store 
    for i in pos_list:
        if csv_dict[1][csv_dict[0][pos_header][i]] >= lowrange and csv_dict[1][csv_dict[0][pos_header][i]] <= highrange: # checks if within range inclusive 
            valid_pos.append(i)
    return valid_pos # returns the list positions of the items within year range

def positions_of_items(csv_dict,pos_header,term_find): # a function to find positions of objects that correspond to the term_find, csv_dict is the list containing all the data
    positions_in_list = [] # a blank list to append item positions to
    pos = 0
    for i in csv_dict[1][csv_dict[0][pos_header]]:
        if i == term_find:
            positions_in_list.append(pos)
    return positions_in_list

def pos_of_keys(dictionary_of_csv,headerlookingfor):# this function finds the position in the header list that returns the header we want
    position = 0
    #print(dictionary_of_csv[1]) # this prints out the header list
    for i in dictionary_of_csv[1]: # this checks which list it is
        #if i == headerlookingfor:
            #print(i)
            #print(position)
        #    return position
        if i.lower() == headerlookingfor.lower():
            #print(position)
            return position
        position += 1
    else: return None

def positions_of_items(csv_dict,pos_header,term_find): # a function to find positions of objects that correspond to the term_find, csv_dict is the list containing all the data, returns a list of the valid objects, note since its a list and the header line is not in the dictionary lists the values outputted are 2 less than the excel's position value
    positions_in_list = [] # a blank list to append item positions to
    pos = 0
    for i in csv_dict[0][csv_dict[1][pos_header]]:
        if i.lower() == term_find.lower():
            positions_in_list.append(pos)
        pos += 1    
    return positions_in_list

def rangecheck(csv_dict,lowrange,highrange,pos_list,pos_header): # checks poslit item's (list of location of items of valid countries) years is within int lowrange and int highrange inclusive, outputs positions that match
    valid_pos = [] # empty list to store 
    for i in pos_list:
        if int(csv_dict[0][csv_dict[1][pos_header]][i]) >= lowrange and int(csv_dict[0][csv_dict[1][pos_header]][i]) <= highrange: # checks if within range inclusive, int() added so that the strings are converted to integers so mathmatical operations can occur 
            valid_pos.append(i)
    return valid_pos # returns the list positions of the items within year range

# returns list with max and min company positions
def high_and_low_count(csv_dict,poslist,pos_header): #poslist is the list of positions of data in the dictionary lists
    # Defining variables for the function calculation 
    start_number = int(csv_dict[0][csv_dict[1][pos_header]][poslist[0]])
    largest_number = start_number
    smallest_number = start_number
    max_company_list_pos = poslist[0]
    min_company_list_pos = poslist[0] 
    for i in poslist:
        #print(csv_dict[0][csv_dict[1][pos_header]][i])
        if int(csv_dict[0][csv_dict[1][pos_header]][i]) > largest_number:
            largest_number =  int(csv_dict[0][csv_dict[1][pos_header]][i])
            max_company_list_pos = i 
        if  int(csv_dict[0][csv_dict[1][pos_header]][i]) < smallest_number : #min not correct right now 
            smallest_number = int(csv_dict[0][csv_dict[1][pos_header]][i])
            min_company_list_pos = i
    return [max_company_list_pos,min_company_list_pos]      

def min_max_company_name(csv_dict,poslist,pos_header): # poslist is the list from the high_and_low_count function, returns the max and min company names
    nameslist = []
    for i in poslist:
        nameslist.append(csv_dict[0][csv_dict[1][pos_header]][i])
    return nameslist

def pos_of_numbers(csv_dict,str_key_header):
    positions_in_list = [] # a blank list to append item positions to
    pos = 0
    for i in csv_dict[0][csv_dict[1][str_key_header]]:
        positions_in_list.append(pos)
        pos += 1    
    return positions_in_list

def standard_deviation_calculator(csv_dict,pos_list,pos_header): # pos_list is the list of valid object positions, pos_header is the dictionary key we want
    object_amount = len(pos_list)
    #print(object_amount)

    #calc mean of the area
    sum_total = 0
    for i in pos_list:
        sum_total += int(csv_dict[0][csv_dict[1][pos_header]][i])
    #print(sum_total)

    mean = sum_total/object_amount

    #sum of the difference between object and mean
    diff_sum = 0
    for i in pos_list:
        diff_sum += (int(csv_dict[0][csv_dict[1][pos_header]][i])-mean)**2

    #division by (number of objects - 1) and then square root
    Stand_Dev = (diff_sum/(object_amount-1))**(0.5)
    return Stand_Dev



# something here screwerd 
# returns the amount of money that did net profit and then those that did net loss between 2021 and 2020
def net_diff(csv_dict,pos_list,pos_header_21,pos_header_20): # pos_list is the list of valid object positions, pos_header is the location of dictionary key we want in the header list
    # defining empty lists for the calculation 
    pos_dif = []
    neg_dif = []
    pos_dif_pos = []
    neg_dif_pos = []
    for i in pos_list:
        difference = int(csv_dict[0][csv_dict[1][pos_header_21]][i])- int(csv_dict[0][csv_dict[1][pos_header_20]][i])
        #print(difference)
        if difference >= 0:
            pos_dif.append(difference)
            pos_dif_pos.append(i)
        elif difference < 0:
            neg_dif.append(difference)
            neg_dif_pos.append(i)
    #print([pos_dif,neg_dif,pos_dif_pos,neg_dif_pos])
    return [pos_dif,neg_dif,pos_dif_pos,neg_dif_pos]


#calculates the ratio of net pos/net neg 
def ratio_calc(list_of_pos_neg):
    abs_pos_vals = abs(sum(list_of_pos_neg[0]))
    abs_neg_vals = abs(sum(list_of_pos_neg[1]))
    #print(abs_pos_vals)
    #print(abs_neg_vals)
    ratio = abs_pos_vals/abs_neg_vals
    # check how many 
    return ratio

#q4 functions 
def mean_calc(csv_dict,pos_list,pos_header): # pos header is the numerical list position of the header in the header list
    object_amount = len(pos_list)
    #calc mean of the area
    sum_total = 0
    for i in pos_list:
        sum_total += int(csv_dict[0][csv_dict[1][pos_header]][i])
    mean = sum_total/object_amount
    return mean

# this is the numerator 
def diff_sum_xy(csv_dict,pos_list,mean,pos_header,mean2,pos_header2):
    diff_sum = 0
    for i in pos_list:
        diff_sum += (int(csv_dict[0][csv_dict[1][pos_header]][i])-mean)*(int(csv_dict[0][csv_dict[1][pos_header2]][i])-mean2)
    #print(diff_sum)
    return diff_sum

#this needs to be calced for x and y and then multiplied together for demominator 
def diff_sum_squared(csv_dict,pos_list,pos_header,mean):
    diff_sum = 0
    for i in pos_list:
        diff_sum += (int(csv_dict[0][csv_dict[1][pos_header]][i])-mean)**2
    #print(diff_sum)
    return diff_sum


def correlation_calc(numerator,denominator):
    correlation = numerator/(denominator)**0.5  
    return correlation

def main(csvfile,country):
    csvfile = csv_file_appender(csvfile)   # adds csv to the file
    csv_data = csv_to_dict(csvfile) # this creates a list that contains the headers and a dictionary that contains lists of all the data under each header   
    country = lowercase_initial_country(country) # this lowercase the inputed country

    # header positions in header lists 
    pos_Country_in_header_list = pos_of_keys(csv_data,"country") # this will return the position in the list of headers that the country header is stored so that the header key can be called to call the list storing country name of each organisation    
    pos_Founded_year_in_header_list = pos_of_keys(csv_data,"founded") # this will return the position in the list of headers that the founded year header is stored so that the header key can be called to call the list storing year of founding of each organisation    
    pos_Number_of_employees_in_header_list = pos_of_keys(csv_data,"Number of employees")
    pos_company_names_in_header_list = pos_of_keys(csv_data,"Name")
    pos_median_salary_in_header_list = pos_of_keys(csv_data,"Median Salary")
    pos_21_profit_in_header_list = pos_of_keys(csv_data,"Profits in 2021(Million)")
    pos_20_profit_in_header_list = pos_of_keys(csv_data,"Profits in 2020(Million)")

    #country check
    companies_in_target_country = positions_of_items(csv_data, pos_Country_in_header_list,country)

    #list of all organisations median salary positions, for use in total org medium salary standard deviation
    all_org_median_salary_pos = pos_of_numbers(csv_data,pos_median_salary_in_header_list)
    #print(all_org_median_salary_pos )
    
    #q1
    Companies_in_target_years_and_country = rangecheck(csv_data,lower_year_limit,upper_year_limit,companies_in_target_country, pos_Founded_year_in_header_list)
    highest_lowest_employ = high_and_low_count(csv_data,Companies_in_target_years_and_country,pos_Number_of_employees_in_header_list)
    companies_max_and_min_employee_list = min_max_company_name(csv_data,highest_lowest_employ,pos_company_names_in_header_list) # q1 answer 
    #q1 answer ^, this contains the list of the solutions 
    print("max and min:")
    print(companies_max_and_min_employee_list)

    #q2 country SD
    Country_SD = standard_deviation_calculator(csv_data,companies_in_target_country,pos_median_salary_in_header_list)
    #print("Country_SD:" ,str(Country_SD))
    
    #q2 total org SD 
    Total_org_SD = standard_deviation_calculator(csv_data,all_org_median_salary_pos,pos_median_salary_in_header_list)
    #print("Total_org_SD:", str(Total_org_SD))
    # standard dev [country, total]
    Calculated_SD = [round(Country_SD,4),round(Total_org_SD,4)]
    print("SD:")
    print(Calculated_SD)

    #q3
    pos_neg_profit = net_diff(csv_data,companies_in_target_country,pos_21_profit_in_header_list,pos_20_profit_in_header_list)
    pos_neg_ratio = ratio_calc(pos_neg_profit)
    pos_neg_ratio = round(pos_neg_ratio,4)
    print("Ratio:")
    print(pos_neg_ratio)

    #q4
    #pos_neg_profit_numerical = net_diff(csv_data,companies_in_target_country,pos_21_profit_in_header_list,pos_20_profit_in_header_list)
    country_met_profit_country = pos_neg_profit[2] # gives the list positions for the companies that meet criteria
    #print("country_met_profit_country:")
    #print(country_met_profit_country)
    median_salary_mean = mean_calc(csv_data,country_met_profit_country,pos_median_salary_in_header_list) # mean value of median salary
    #print("median_salary_mean:")
    #print(median_salary_mean)
    
    profits_mean = mean_calc(csv_data,country_met_profit_country,pos_21_profit_in_header_list) # mean value of profits 
    #print("profits_mean")
    #print(profits_mean)

    numerator = diff_sum_xy(csv_data,country_met_profit_country,profits_mean,pos_21_profit_in_header_list,median_salary_mean,pos_median_salary_in_header_list)
    #print("numerator")
    #print(numerator)


    diff_sum_squared_median = diff_sum_squared(csv_data,country_met_profit_country,pos_median_salary_in_header_list,median_salary_mean)
    #print("diff_sum_squared_median")
    #print(diff_sum_squared_median)

    diff_sum_squared_profit = diff_sum_squared(csv_data,country_met_profit_country,pos_21_profit_in_header_list,profits_mean)
    #print("diff_sum_squared_profit")
    #print(diff_sum_squared_profit)


    correlation = correlation_calc(numerator,diff_sum_squared_median*diff_sum_squared_profit)
    correlation = round(correlation,4)
    print("Correlation:")
    print(correlation)
    return companies_max_and_min_employee_list,Calculated_SD, pos_neg_ratio, correlation
    #return none

print(main("Organisations.csv","Australia"))
#main("Organisations.csv","Korea")