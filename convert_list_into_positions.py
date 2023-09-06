# this converts whole lists to show the list position
def pos_of_numbers(csv_dict,str_key_header):
    positions_in_list = [] # a blank list to append item positions to
    pos = 0
    for i in csv_dict[0][csv_dict[1][str_key_header]]:
        positions_in_list.append(pos)
        pos += 1    
    return positions_in_list