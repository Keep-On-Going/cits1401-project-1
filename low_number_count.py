def high_and_low_count(csv_dict,poslist,pos_header): #poslist is the list of positions
    start_number = int(csv_dict[0][csv_dict[1][pos_header]][poslist[0]])
    largest_number = start_number
    smallest_number = start_number
    max_company_list_pos = poslist[0]
    min_company_list_pos = poslist[0] 
    for i in poslist:
        #print(csv_dict[0][csv_dict[1][pos_header]][i])
        if int(csv_dict[0][csv_dict[1][pos_header]][i]) > largest_number:
            largest_number =  int(csv_dict[0][csv_dict[1][pos_header]][i])
            max_company_list_pos = i 
        if  int(csv_dict[0][csv_dict[1][pos_header]][i]) < smallest_number : #min not correct right now 
            smallest_number = int(csv_dict[0][csv_dict[1][pos_header]][i])
            min_company_list_pos = i
    return [max_company_list_pos,min_company_list_pos]      

