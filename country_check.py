def pos_of_keys(dictionary_of_csv,headerlookingfor):
    position = 0
    for i in dictionary_of_csv[1]: # this checks which list it is
        position = 0
        if i == headerlookingfor:
            #print(i)
            #print(position)
            return [position]
        position += 1

def country_check(dictionary_of_csv, country): # the input here is the output of the csv_to_dict function
    key_location_in_list = pos_of_keys(dictionary_of_csv,country)
    list_of_country = dictionary_of_csv[key_location_in_list]
        

    
country_check([[0],["a","b","Country"]])