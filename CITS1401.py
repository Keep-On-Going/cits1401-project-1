#Vincent Jeff Liu, UWA Student ID: 23777635

# python project for CITS1401

# we need to find a way to manage the csv file data so we can edit it and access it easier and in its orders 
# so we using a dictionary 

Data_on_organisations = open("Organisations.csv","r") # this creates a file object, the object is set to read which only allows us to read the data about organisations
print(Data_on_organisations.readline())

#"C:\Users\Vince\OneDrive\Documents\GitHub\cits1401\Organisations.csv"