# we need to functionalise some of q3 as it can be reused in q4

# calc this for x and y
def mean_calc(csv_dict,pos_list,pos_header): # pos header is the numerical list position of the header in the header list
    object_amount = len(pos_list)
    #calc mean of the area
    sum_total = 0
    for i in pos_list:
        sum_total += int(csv_dict[0][csv_dict[1][pos_header]][i])
    mean = sum_total/object_amount


# up to here for q4 in main i think, confirm outputs and inputs 


# this is the numerator 
def diff_sum_xy(csv_dict,pos_list,mean,pos_header,mean2,pos_header2):
    diff_sum = 0
    for i in pos_list:
        diff_sum += (int(csv_dict[0][csv_dict[1][pos_header]][i])-mean)(int(csv_dict[0][csv_dict[1][pos_header2]][i])-mean2)
    print(diff_sum)

#this needs to be calced for x and y and then multiplied together for demominator 
def diff_sum_squared(csv_dict,pos_list,pos_header,mean):
    diff_sum = 0
    for i in pos_list:
        diff_sum += (int(csv_dict[0][csv_dict[1][pos_header]][i])-mean)**2
    print(diff_sum)


def correlation_calc(numerator,denominator):
    correlation = numerator/(denominator)**0.5                                                                   