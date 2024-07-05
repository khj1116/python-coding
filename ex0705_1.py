def add(a,b):
    return a+b

def safe_add(a,b):
    if type(a) != type(b):
        print('더할 수 없습니다')
        return
    else:
        result=a+b
    return result


