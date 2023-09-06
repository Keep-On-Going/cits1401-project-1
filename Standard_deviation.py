def standard_deviation(csv_dict,pos_list,pos_header):
    object_amount = len(pos_list)

    #calc mean of the area
    sum_total = 0
    for i in pos_list:
        sum_total += csv_dict[0][csv_dict[1][pos_header]][pos_list[i]]

    mean = sum_total/object_amount

    return None