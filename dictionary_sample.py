# practice for how a dictionary can hold data and how to call that data out 

dictionary = { "a" : 10, "b" : "Hello", "c": [1,2,3] }

print(dictionary["c"][1]) # here by calling the key we get the list object that is paired with c, the [] right after acts to get the specific data from the list following list syntax

dict_of_org_data ={}
dict_of_org_data["Name"] = [] # adding a item to the dictionary with keyword "Name" and value is a empty list 
dict_of_org_data["Name"].append("BOB") # these add to the empty list 
dict_of_org_data["Name"].append("DOD")
dict_of_org_data["Name"].append("CAC")
print(dict_of_org_data)    
print(dict_of_org_data["Name"][0])   # this calls the specific item 0 from the list in the value of the key "Name"