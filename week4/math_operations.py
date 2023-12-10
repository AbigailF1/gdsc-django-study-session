def basic_operations(x,y):
    dic = {}
    # sum
    result = x + y
    dic[(x,"+", y)] = result
    # subtraction 
    result = x -y
    dic[(x,"-", y)] = result
    # multiplication 
    result = x * y
    dic[(x,"*", y)] = result
    #division 
    try: 
        result = x / y
    except:
        result = "invalid"
    dic[(x,"/", y)] = result
    return dic

def power_operation(base, exponent, **kwargs):
    try:
        result = base ** exponent
    except Exception as e:
        print(f"Error: {e}")
        result = -1

    if 'modulo' in kwargs:
        result %= kwargs['modulo']
    return result

def apply_operations(args):
    ans =[]
    try:
        for fn, nums in args:
            ans.append(fn(*nums))
        return ans
    except:
        print("ERROR")



