d = {
	"key1": 1,
	"key2": {
			"key3": 1,
			"key4": {
					"key5": 4
			}
	}
}

def myprint(d):
	stack = d.items()
	while stack:
		k, v = stack.pop()
		if isinstance(v, dict):
			stack.extend(v.iteritems())
		else:
			print("%s: %s" % (k, v)) 
		pass

myprint(d)

# def myprint(d):
#   for k, v in d.iteritems():
#     if isinstance(v, dict):
#       myprint(v)
#     else:
#       print "{0} : {1}".format(k, v)

# def printDict(d):
#     for k, v in dict.iteritems():
#         if type(v) is dict:
#             printDict(v)
#         else:
#             print "{0} : {1}".format(k, v)