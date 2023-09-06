def high_and_low_count(csv_dict,poslist,pos_header): #poslist is the list of positions
    largest_number = int(csv_dict[0][csv_dict[1][pos_header]][0])
    smallest_number = int(csv_dict[0][csv_dict[1][pos_header]][0])
    max_company_list_pos = 0
    min_company_list_pos = 0 
    for i in poslist:
        if int(csv_dict[0][csv_dict[1][pos_header]][i]) > largest_number:
            largest_number =  int(csv_dict[0][csv_dict[1][pos_header]][i])
            max_company_list_pos = i 
        if  int(csv_dict[0][csv_dict[1][pos_header]][i]) < smallest_number: # no company will have less than 0 employee so just start with numbers in the list
            smallest_number = int(csv_dict[0][csv_dict[1][pos_header]][i])
            min_company_list_pos = i

    return [max_company_list_pos,min_company_list_pos]      

