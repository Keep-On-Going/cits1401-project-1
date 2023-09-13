def csv_to_dict(file_name):# file_name can be the path with the file name 
    Data_on_organisations = open(file_name,"r",encoding='utf-8-sig') # this creates a file object, the object is set to read which only allows us to read the data about organisations
    # note the file is meant to take an output from the 

    first_line_of_file = Data_on_organisations.readline() # this reads the topline of the file and returns it as a single string, readline adds a \n we need to get rid of this
    first_line_of_file = first_line_of_file.replace("\n","") # this gets rid of the \n from the first line, the .replace will output a copy of the string so needs to be set to a variable to be used 
    list_of_headings = first_line_of_file.split(",") # this turns the string from the topline of the file into a list with each item being the respective headers, .split() outputs a copy of the list

    dict_of_org_data ={} # empty dictionary where all the org data will be sorted into 
    i = 0 # defining var i for for loop
    for i in list_of_headings: # this for loop adds dictionary items with the key being the header words and the value of the key is an empty list to add the header specific data to
        dict_of_org_data[i] = []

    list_of_org_dict_keys = list(dict_of_org_data)

    for line in Data_on_organisations:# this for loop loops through the remaining lines in csv file and sorts the data into the dictionary 
        line = line.replace("\n","") # gets rid of the "\n", the replace function needs to be set to an variable as it outputs a copy of the list
        current_line_list = line.split(",") # this turns the current line's string into a list, with each item corresponding to a key in the dictionary 
        a = 0     # iterator 
        for item in current_line_list: # this moves the data from each list object to the corresponding dictionary list to group data together in its categories 
            dict_of_org_data[list_of_org_dict_keys[a]].append(item) # list_of_org_dict_keys[a] gives the corresponding key, var a makes sure the key changes to the right one to allow for list appending, 
            a += 1 #adds to a so its the correct list 
    return [dict_of_org_data, list_of_org_dict_keys]


a = open("/Users/jeff/Downloads/Organisations.csv","r",encoding='utf-8-sig')
print(a.readline())
