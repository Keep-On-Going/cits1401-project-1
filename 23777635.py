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
        csvfile = csvfile +".csv"
        #print(csvfile)
    return csvfile

def lowercase_initial_country(target_country_name): # lowecases the inputed country
    return target_country_name.lower()

def csv_to_dict(file_name):# file_name can be the path with the file name 
    Data_on_organisations = open(file_name,"r",encoding='utf-8-sig') # this creates a file object, the object is set to read which only allows us to read the data about organisations
    # note the file is meant to take an output from the 

    first_line_of_file = Data_on_organisations.readline() # this reads the topline of the file and returns it as a single string, readline adds a \n we need to get rid of this
    first_line_of_file.rstrip("\n")
    first_line_of_file = first_line_of_file.replace("\n","") # this gets rid of the \n from the first line, the .replace will output a copy of the string so needs to be set to a variable to be used 
    list_of_headings = first_line_of_file.split(",") # this turns the string from the topline of the file into a list with each item being the respective headers, .split() outputs a copy of the list

    dict_of_org_data ={} # empty dictionary where all the org data will be sorted into 
    i = 0 # defining var i for for loop
    for i in list_of_headings: # this for loop adds dictionary items with the key being the header words and the value of the key is an empty list to add the header specific data to
        dict_of_org_data[i] = []

    list_of_org_dict_keys = list(dict_of_org_data)
    #tester#print(list_of_org_dict_keys[0])

    for line in Data_on_organisations:# this for loop loops through the remaining lines in csv file and sorts the data into the dictionary 
        line = line.replace("\n","") # gets rid of the "\n", the replace function needs to be set to an variable as it outputs a copy of the list
        current_line_list = line.split(",") # this turns the current line's string into a list, with each item corresponding to a key in the dictionary 
        a = 0     # iterator 
        for item in current_line_list: # this moves the data from each list object to the corresponding dictionary list to group data together in its categories 
            dict_of_org_data[list_of_org_dict_keys[a]].append(item) # list_of_org_dict_keys[a] gives the corresponding key, var a makes sure the key changes to the right one to allow for list appending, 
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
    for i in dictionary_of_csv[1]: # this checks which list it is
        if i.lower() == headerlookingfor.lower():
            return position
        position += 1
    

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
    ###print(int(csv_dict[0][csv_dict[1][pos_header]][poslist[0]]))
    start_number = int(csv_dict[0][csv_dict[1][pos_header]][poslist[0]])
    largest_number = start_number
    smallest_number = start_number
    max_company_list_pos = poslist[0]
    min_company_list_pos = poslist[0] 
    for i in poslist: # finds the largest and smallest employee count 
        print(i)
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

    #calc mean of the area
    sum_total = 0
    for i in pos_list:
        sum_total += int(csv_dict[0][csv_dict[1][pos_header]][i])

    mean = sum_total/object_amount

    #sum of the difference between object and mean
    diff_sum = 0
    for i in pos_list:
        diff_sum += (int(csv_dict[0][csv_dict[1][pos_header]][i])-mean)**2

    #division by (number of objects - 1) and then square root
    Stand_Dev = (diff_sum/(object_amount-1))**(0.5)
    return Stand_Dev

def net_diff(csv_dict,pos_list,pos_header_21,pos_header_20): # pos_list is the list of valid object positions, pos_header is the location of dictionary key we want in the header list
    # defining empty lists for the calculation 
    pos_dif = []
    neg_dif = []
    pos_dif_pos = []
    neg_dif_pos = []
    for i in pos_list:
        difference = int(csv_dict[0][csv_dict[1][pos_header_21]][i])- int(csv_dict[0][csv_dict[1][pos_header_20]][i])
        if difference >= 0:
            pos_dif.append(difference)
            pos_dif_pos.append(i)
        elif difference < 0:
            neg_dif.append(difference)
            neg_dif_pos.append(i)
    return [pos_dif,neg_dif,pos_dif_pos,neg_dif_pos]


#calculates the ratio of net pos/net neg 
def ratio_calc(list_of_pos_neg):
    abs_pos_vals = abs(sum(list_of_pos_neg[0]))
    abs_neg_vals = abs(sum(list_of_pos_neg[1]))
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

    return diff_sum

#this needs to be calced for x and y and then multiplied together for demominator 
def diff_sum_squared(csv_dict,pos_list,pos_header,mean):
    diff_sum = 0
    for i in pos_list:
        diff_sum += (int(csv_dict[0][csv_dict[1][pos_header]][i])-mean)**2

    return diff_sum

def correlation_calc(numerator,denominator):
    correlation = numerator/(denominator)**0.5  
    return correlation

def main(csvfile,country):
    try:
        csvfile = csv_file_appender(csvfile)   # adds csv to the file
    except:
        print("Error with inputed file argument")
        return [],[],0,0 
    
    try:
        csv_data = csv_to_dict(csvfile) # this creates a list that contains the a list of the headers and a dictionary (that contains lists of all the data under each header) each in a seperate list space      
    except:
        print("Error with csv conversion to a dictionary")
        return [],[],0,0 

    try:
        country = lowercase_initial_country(country) # this lowercase the inputed country
    except:
        print("Error with main function country argument")
        return [],[],0,0     

    #functions that find the position of headers and their respective data 
    try:
        pos_Country_in_header_list = pos_of_keys(csv_data,"country") # this will return the position in the list of headers that the country header is stored so that the header key can be called to call the list storing country name of each organisation    
    except:
        print("Unable to find list position of header for: country")
        return [],[],0,0

    try:
        pos_Founded_year_in_header_list = pos_of_keys(csv_data,"founded") # this will return the position in the list of headers that the founded year header is stored so that the header key can be called to call the list storing year of founding of each organisation    
    except:
        print("Unable to find list position of header for: year founded")
        return [],[],0,0

    try:
        pos_Number_of_employees_in_header_list = pos_of_keys(csv_data,"Number of employees")
    except:
        print("Unable to find list position of header for: number of employees")
        return [],[],0,0
    
    try:
        pos_company_names_in_header_list = pos_of_keys(csv_data,"Name")
    except:
        print("Unable to find list position of header for: company name")
        return [],[],0,0
    
    try:
        pos_median_salary_in_header_list = pos_of_keys(csv_data,"Median Salary")
    except:
        print("Unable to find list position of header for: median")
        return [],[],0,0

    try:
        pos_21_profit_in_header_list = pos_of_keys(csv_data,"Profits in 2021(Million)")
    except:
        print("Unable to find list position of header for: profits in 2021")
        return [],[],0,0
    
    try:
        pos_20_profit_in_header_list = pos_of_keys(csv_data,"Profits in 2020(Million)")
    except:
        print("Unable to find list position of header for: profits in 2020")
        return [],[],0,0

    #country check
    try:
        companies_in_target_country = positions_of_items(csv_data, pos_Country_in_header_list,country)
    except:
        print("Unable to find companies in target countries")
        return [],[],0,0

    #list of all organisations median salary positions, for use in total org medium salary standard deviation
    try:
        all_org_median_salary_pos = pos_of_numbers(csv_data,pos_median_salary_in_header_list)
    except:
        print("Unable to find median salary data")
        return [],[],0,0

    #q1
    #checking 
    
    Companies_in_target_years_and_country = rangecheck(csv_data,lower_year_limit,upper_year_limit,companies_in_target_country, pos_Founded_year_in_header_list)
    if len(Companies_in_target_years_and_country) == 0:
         companies_max_and_min_employee_list = []
    else:
        highest_lowest_employ = high_and_low_count(csv_data,Companies_in_target_years_and_country,pos_Number_of_employees_in_header_list)
        companies_max_and_min_employee_list = min_max_company_name(csv_data,highest_lowest_employ,pos_company_names_in_header_list) # q1 answer 
        #q1 answer ^, this contains the list of the solutions 

    #q2 country SD
    if len(companies_in_target_country) > 1:
        Country_SD = standard_deviation_calculator(csv_data,companies_in_target_country,pos_median_salary_in_header_list)
    elif len(companies_in_target_country) <= 1:
        Country_SD = 0

    #q2 total org SD 
    if len(all_org_median_salary_pos) > 1:
        Total_org_SD = standard_deviation_calculator(csv_data,all_org_median_salary_pos,pos_median_salary_in_header_list)
    elif len(companies_in_target_country) <= 1:
        Total_org_SD = 0
    Calculated_SD = [round(Country_SD,4),round(Total_org_SD,4)]

    #q3, ratio calc
    pos_neg_profit = net_diff(csv_data,companies_in_target_country,pos_21_profit_in_header_list,pos_20_profit_in_header_list)
    if abs(sum(pos_neg_profit[1])) <= 0:
        pos_neg_ratio = 0
    else:
        pos_neg_ratio = ratio_calc(pos_neg_profit)
        pos_neg_ratio = round(pos_neg_ratio,4)

    #q4, correlation calc
    country_met_profit_country = pos_neg_profit[2] # gives the list positions for the companies that meet criteria
    median_salary_mean = mean_calc(csv_data,country_met_profit_country,pos_median_salary_in_header_list) # mean value of median salary
    profits_mean = mean_calc(csv_data,country_met_profit_country,pos_21_profit_in_header_list) # mean value of profits 
    numerator = diff_sum_xy(csv_data,country_met_profit_country,profits_mean,pos_21_profit_in_header_list,median_salary_mean,pos_median_salary_in_header_list)
    diff_sum_squared_median = diff_sum_squared(csv_data,country_met_profit_country,pos_median_salary_in_header_list,median_salary_mean)
    diff_sum_squared_profit = diff_sum_squared(csv_data,country_met_profit_country,pos_21_profit_in_header_list,profits_mean)
    if (diff_sum_squared_median*diff_sum_squared_profit) == 0:
        correlation = 0
    else:
        correlation = correlation_calc(numerator,diff_sum_squared_median*diff_sum_squared_profit)
        correlation = round(correlation,4)

    return companies_max_and_min_employee_list,Calculated_SD, pos_neg_ratio, correlation


#print(main("Organisations","Australia"))
#main("Organisations.csv","Korea")
print(main("Organisations.csv","El Salvador"))
