def print_dict(dictionary, ident = '', braces=1):    
    """ Recursively prints nested dictionaries."""

    # for key, value in dictionary.iteritems():
    #     if isinstance(value, dict):
    #         print '%s%s%s%s' %(ident,braces*'[',key,braces*']') 
    #         # print '%s%s%s%s' %(ident,braces*'[',key,braces*']')             
    #         print_dict(value, ident, braces+1)
    #     else:
    #         print ident+'%s = %s' %(key, value)


if __name__ == '__main__':

    a = {
        "key1": 1,
        "key2": {
                "key3": 1,
                "key4": {
                        "key5": 4
                }
        }
    }

    print_dict(a)