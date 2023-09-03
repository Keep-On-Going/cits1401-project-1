def pos_of_keys(dictionary_of_csv,headerlookingfor):
    position = 0
    for i in dictionary_of_csv[1]: # this checks which list it is
        position = 0
        if i == headerlookingfor:
            #print(i)
            #print(position)
            return [position]
        position += 1

pos_of_keys([[0],["a","b","Country"]],"Country")