#! usr/bin/env python
already_emailed_list = ["x", "z"]

# import open(newlist.txt,'r') as needs_to_be_checked:
needs_to_be_checked = ["x", "y","z", "L"]
for item in needs_to_be_checked:
    if item in already_emailed_list:
        pass
    else:
        print '"'+item+'",'

