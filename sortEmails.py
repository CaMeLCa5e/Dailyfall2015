lines_seen = set() # holds lines already seen
outfile = open('cleanData4.txt', "w")
for line in open('cleanData3.txt', "r"):
    line_length = len(line)
    if line_length < 30:
        if line not in lines_seen: # not a duplicate
            # outfile.write(',')
            outfile.write(line)
            lines_seen.add(line)
    else: 
        pass

outfile.close()