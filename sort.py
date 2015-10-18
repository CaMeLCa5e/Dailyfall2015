with open('cleanEmailData13.txt', "w") as outfile:
    with open('cleanEmailData.txt', "r") as infile:
        for line in sorted(infile, key=len, reverse=True):
            line_length = len(line)
            if 9 < line_length < 30 and '@' in line:
                if not any(ss in line for ss in undesired_substrings):                
                    if line not in lines_seen: 
                        if not any(l.endswith(line) for l in lines_seen):
                            outfile.write(line) 
                            lines_seen.add(line)
