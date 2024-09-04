def line_count():
    f = open("file.txt", "r")
    count = 0
    lines = f.readlines()
    
    for line in lines:
        line.strip()
        count += 1 

    f.close()
    return count
