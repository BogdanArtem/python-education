"""Functions practice examples"""

# edit the functions prototype and implementation
def func1(arg1, arg2, arg3, *args):
    """Function to demonstrate args"""
    return len(args)

def func2(arg1, arg2, arg3, **kwargs):
    """Function to demonstrate kwargs"""
    if kwargs['magicnumber'] == 7:
        return True
    return False


# test code
if func1(1,2,3,4) == 1:
    print("Good.")
if func1(1,2,3,4,5) == 2:
    print("Better.")
if bar(1,2,3,magicnumber = 6) is False:
    print("Great.")
if bar(1,2,3,magicnumber = 7) is True:
    print("Awesome!")
