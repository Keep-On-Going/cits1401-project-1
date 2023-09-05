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

#def country_check(dictionary_of_csv, country): # the input here is the output of the csv_to_dict function
#    key_location_in_list = pos_of_keys(dictionary_of_csv,country)
#    list_of_country = dictionary_of_csv[key_location_in_list]
        

print(pos_of_keys([[0],["a","b","country"]],"Country"))   
#country_check([[0],["a","b","country"]],"Country")