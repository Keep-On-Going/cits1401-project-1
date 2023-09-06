def standard_deviation_calculator(csv_dict,pos_list,pos_header):
    object_amount = len(pos_list)
    #calc mean of the area
    sum_total = 0
    for i in pos_list:
        sum_total += int(csv_dict[0][csv_dict[1][pos_header]][i])
    mean = sum_total/object_amount
    print(object_amount)
    print(sum_total)
    print(mean)

    #sum of the difference between object and mean
    diff_sum = 0
    for i in pos_list:
        diff_sum += (int(csv_dict[0][csv_dict[1][pos_header]][i])-mean)**2
    print(diff_sum)

    #division by (number of objects - 1) and then square root
    Stand_Dev = (diff_sum/(object_amount-1))**(0.5)
    return Stand_Dev