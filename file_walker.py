import os
for root, dirs, files in os.walk("/Users/"):
    for file in files:
        if file.endswith(".html"):        
            print(os.path.join(root, file))
            text_file = open(os.path.join(root, file), "r")
            print text_file.read()
            text_file.close()
