def csv_to_dict(file_name):
    Data_on_organisations = open(file_name,"r") # this creates a file object, the object is set to read which only allows us to read the data about organisations
        # note the file is meant to take an output from the 

    first_line_of_file = Data_on_organisations.readline() # this reads the topline of the file and returns it as a single string, readline adds a \n we need to get rid of this
    first_line_of_file.rstrip("\n")
    #tester#print(first_line_of_file.replace("\n",""))
    first_line_of_file = first_line_of_file.replace("\n","") # this gets rid of the \n from the first line, the .replace will output a copy of the string so needs to be set to a variable to be used 
    list_of_headings = first_line_of_file.split(",") # this turns the string from the topline of the file into a list with each item being the respective headers, .split() outputs a copy of the list 
    #tester#print(list_of_headings)
    return list_of_headings

print(csv_to_dict("Organisations.csv"))