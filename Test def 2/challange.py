

def counter(name):
    if name == None:
        return Exception('Please try other combination')

    name = name.replace(' ', '')
    if len(name) == 0:
        return Exception('Please input correct value')


    if name.isalpha():
        return len(name)
    else:
        raise Exception('We need use only letters')




