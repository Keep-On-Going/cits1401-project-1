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
    #print(companies_max_and_min_employee_list)

    #q2 country SD
    Country_SD = standard_deviation_calculator(csv_data,companies_in_target_country,pos_median_salary_in_header_list)
    print("Country_SD:" ,str(Country_SD))
    #q2 total org SD 
    Total_org_SD = standard_deviation_calculator(csv_data,all_org_median_salary_pos,pos_median_salary_in_header_list)
    print("Total_org_SD:", str(Total_org_SD))
    # standard dev [country, total]
    Calculated_SD = [Country_SD,Total_org_SD]

    #q4, work on this before q3

    return None

main("Organisations.csv","Australia")
#main("Organisations.csv","Korea")