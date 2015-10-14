lines_seen = set() # holds lines already seen
outfile = open('cleanEmailData13.txt', "w")
for line in open('cleanEmailData.txt', "r"):
    line = line.strip('*')
    line_length = len(line)
    if line_length < 30:
        if line_length > 13:            
            if '@' in line:
                # elif:
                    # except.find(''):                
                # if not line.endswith('.c' [-1]):
                # if '.com' or '.net' or '.us' or '.in' or '.biz' or 'org' in line:
                    # if not 'apache' or 'googlegroups' or 'unsubscribe' or '.jpg' or '.png' in line:         
                if line not in lines_seen: 
                    # if line.endswith(line) not in lines_seen:
                    # outfile.write(',')
                    outfile.write(line) 
                    lines_seen.add(line)
    else: 
        print line

outfile.close()