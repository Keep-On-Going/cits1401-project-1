def rangecheck(lowrange,highrange,pos_list,pos_header,csv_dict): # checks poslit item's (list of location of items of valid countries) years is within int lowrange and int highrange inclusive, outputs positions that match
    valid_pos = [] # empty list to store 
    for i in pos_list:
        if csv_dict[1][csv_dict[0][pos_header]][i] >= lowrange and csv_dict[1][csv_dict[0][pos_header]][i] <= highrange: # checks if within range inclusive 
            valid_pos.append(i)
    return valid_pos # returns the list positions of the items within year range
