def min_max_company_name(csv_dict,poslist,pos_header): # poslist is the list from the high_and_low_count function, returns the max and min company names
    list_pos = 0
    nameslist = []
    for i in poslist:
        nameslist[list_pos] = csv_dict[0][csv_dict[1][pos_header]][i]
        list_pos += 1
    return nameslist