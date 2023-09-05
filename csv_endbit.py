def csv_file_appender(csvfile): # makes sure the file has the .csv ending to allow for correct file call 
    if ".csv" not in csvfile:
        #print("csv not present")
        #print(csvfile)
        csvfile = csvfile +".csv"
        #print(csvfile)
    return csvfile

print(csv_file_appender("k._csv"))        

