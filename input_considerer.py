def main(csvfile,country): # makes sure the correct header 
    if ".csv" not in csvfile:
        print("csv not present")
        print(csvfile
              )
        csvfile = csvfile +".csv"
        print(csvfile)
    return None

print(main("apple","Australia"))        
     