
# returns the list of companies that did net profit and then those that did net loss between 2021 and 2020
def net_diff(csv_dict,pos_list,pos_header_21,pos_header_20): # pos_list is the list of valid object positions, pos_header is the location of dictionary key we want in the header list
    pos_dif = []
    neg_dif = []
    for i in pos_list:
        difference = int(csv_dict[0][csv_dict[1][pos_header_21]][i])- int(csv_dict[0][csv_dict[1][pos_header_20]][i])
        if difference >= 0:
            pos_dif.append(difference)
        elif difference < 0:
            neg_dif.append(difference)
    return [pos_dif,neg_dif]


#calculates the ratio of net pos/net neg 
def ratio_calc(list_of_pos_neg):
    abs_pos_vals = abs(sum(list_of_pos_neg[0]))
    abs_neg_vals = abs(sum(list_of_pos_neg[1]))
    ratio = abs_pos_vals/abs_neg_vals
    return ratio