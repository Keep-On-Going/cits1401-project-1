#Code by Vincent Jeff Liu, UWA Student ID: 23777635

# python project for CITS1401

# we need to find a way to manage the csv file data so we can edit it and access it easier and in its orders 
# so we using a dictionary 


# The below file object is created with the understanding that the csv file is in the same repository as the code, if its not it needs to be changed 
#Data_on_organisations = open("Organisations.csv","r") # this creates a file object, the object is set to read which only allows us to read the data about organisations
# note the file is meant to take an output from the 

def main(csvfile,country):
    if ".csv" not in csvfile: # this if statement is there to make sure the correct file is opened later. 
        print("csv not present")
        print(csvfile
              )
        csvfile = csvfile +".csv"
        print(csvfile)
    
    
    return None