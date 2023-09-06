def rangecheck(lowrange,highrange,pos_list,pos_header,csv_dict): # checks poslit item's (list of location of items of valid countries) years is within int lowrange and int highrange inclusive, outputs positions that match
    valid_pos = [] # empty list to store 
    for i in pos_list:
        if int(csv_dict[1][csv_dict[0][pos_header]][i]) >= lowrange and int(csv_dict[1][csv_dict[0][pos_header]][i]) <= highrange: # checks if within range inclusive, int() added so that the strings are converted to integers so mathmatical operations can occur 
            valid_pos.append(i)
    return valid_pos # returns the list positions of the items within year range
