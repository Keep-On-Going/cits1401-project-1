#Code by Vincent Jeff Liu, UWA Student ID: 23777635
# python project 1 for CITS1401

# we need to find a way to manage the csv file data so we can edit it and access it easier and in its orders 
# so we using a dictionary 

# The below file object is created with the understanding that the csv file is in the same repository as the code, if its not it needs to be changed 
#Data_on_organisations = open("Organisations.csv","r") # this creates a file object, the object is set to read which only allows us to read the data about organisations
# note the file is meant to take an output from the 

def csv_file_appender(csvfile): # makes sure the file has the .csv ending to allow for correct file call 
    if ".csv" not in csvfile:
        #print("csv not present")
        #print(csvfile)
        csvfile = csvfile +".csv"
        #print(csvfile)
    return csvfile

def lowercase_initial_country(target_country_name):
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

def pos_of_keys(dictionary_of_csv,headerlookingfor):
    position = 0
    print(dictionary_of_csv[1])
    for i in dictionary_of_csv[1]: # this checks which list it is
        #if i == headerlookingfor:
            #print(i)
            #print(position)
        #    return position
        if i.lower() == headerlookingfor.lower():
            return position
        position += 1
    else: return None

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

def pos_of_keys(dictionary_of_csv,headerlookingfor):
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

def positions_of_items(csv_dict,pos_header,term_find): # a function to find positions of objects that correspond to the term_find, csv_dict is the list containing all the data
    positions_in_list = [] # a blank list to append item positions to
    pos = 0
    for i in csv_dict[0][csv_dict[1][pos_header]]:
        if i.lower() == term_find.lower():
            positions_in_list.append(pos)
        pos += 1    
    return positions_in_list


def main(csvfile,country):
    csvfile = csv_file_appender(csvfile)   # adds csv to the file
    csv_data = csv_to_dict(csvfile) # this creates a list that contains the headers and a dictionary that contains lists of all the data under each header   
    country = lowercase_initial_country(country) # this lowercase the inputed country
    Country_in_header_list = pos_of_keys(csv_data,"Country") # this will return the position in the list of headers that the country header is stored so that the header key can be called to call the list storing country name of each organisation    
    Companies_that_meet_target_country = positions_of_items(csv_data, Country_in_header_list,country)
    print(Companies_that_meet_target_country)
    return None

main("Organisations.csv","Australia")