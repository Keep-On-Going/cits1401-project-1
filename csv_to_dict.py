# this snippet of code will turn the csv file into a dictionary 

Data_on_organisations = open("Organisations.csv","r") # this creates a file object, the object is set to read which only allows us to read the data about organisations
# note the file is meant to take an output from the 

first_line_of_file = Data_on_organisations.readline() # this reads the topline of the file and returns it as a single string, readline adds a \n we need to get rid of this
first_line_of_file.rstrip("\n")
#print(first_line_of_file.replace("\n",""))
first_line_of_file = first_line_of_file.replace("\n","") # this gets rid of the \n from the first line
list_of_headings = first_line_of_file.split(",") # this turns the string from the topline of the file into a list with each item being the respective headers, .split() outputs a copy of the list 
#print(list_of_headings)

dict_of_org_data ={} # empty dictionary where all the org data will be sorted into 
i = 0
for i in list_of_headings: # this for loop adds dictionary items with the key being the header words and the value of the key is an empty list to add the header specific data to
    dict_of_org_data[i] = []


list_of_org_dict_keys = list(dict_of_org_data)
print(list_of_org_dict_keys[0])

for line in Data_on_organisations:# this for loop loops through the remaining lines in csv file and sorts the data into the dictionary 
    line.rstrip("\n")
    current_line_list = line.split(",")
    a = 0     # iterator 
    for item in current_line_list:
        dict_of_org_data[list_of_org_dict_keys[a]].append(item)
    a += 1

print(dict_of_org_data[list_of_org_dict_keys[0]])    

