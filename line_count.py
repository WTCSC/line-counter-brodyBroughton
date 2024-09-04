def line_count():
    
    # Opens file.txt in read mode
    f = open("file.txt", "r")
    
    # Count variable for the number of lines
    count = 0
    
    # Lines variable for the list of the file
    lines = f.readlines()
    
    # For loops that goes through each line, strips it, and adds 1 to the count
    for line in lines:
        
        line.strip()
        
        count += 1 

    # Closes file
    f.close()
    
    # Returns the number of lines :)
    return count
