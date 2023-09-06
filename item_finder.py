# csv_dict = the list containing the information in a dict and the headers in a list 
# pos_header = a int, that is the location of the header we want in the header list 
# term find = a string, specific string word we want to find

def positions_of_items(csv_dict,pos_header,term_find): # a function to find positions of objects that correspond to the term_find, csv_dict is the list containing all the data
    positions_in_list = [] # a blank list to append item positions to
    pos = 0
    for i in csv_dict[1][csv_dict[0][pos_header]]:
        if i.lower() == term_find.lower():
            positions_in_list.append(pos)
        pos += 1    
    return positions_in_list

print(positions_of_items([[0,1,"Country"],{"Country": ["Australia","","australia"]}],2,"Australia"))