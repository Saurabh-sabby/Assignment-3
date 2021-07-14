def print_words(function):
    def wrapper(t,no):
        for i in range(0,no):
            print(t, end="\n")
        return function(t,no)
    return wrapper

@print_words
def take_input(t,no):
    pass
t=input("what you want to print o screen? \n")
no=int(input("how many times you want to print this on screen ? \n"))
take_input(t,no)




