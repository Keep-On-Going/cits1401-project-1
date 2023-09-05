def positions_of_items(csv_dict,pos_header_list,term_find): # a function to find positions of objects that correspond to the term_find, csv_dict is the list containing all the data
    positions_in_list = [] # a blank list to append item positions to
    pos = 0
    for i in csv_dict[1][csv_dict[0][pos_header_list]]:
        if i == term_find:
            positions_in_list.append(pos)
    return positions_in_list
