def counter(name):

    if name == None:
        raise Exception("Please input correct value")

    name = name.replace(' ', '')
    if len(name) == 0:
        raise Exception("Please input your name")

    if name.isalpha():
        return len(name)
    else:
        raise Exception('The value which should be input is alphabet')

