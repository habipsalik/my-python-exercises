def reverse(a_string):
    new_string = a_string[::-1]
    command = "{0} to {1}".format(a_string, new_string)
    print(command)
    return new_string
