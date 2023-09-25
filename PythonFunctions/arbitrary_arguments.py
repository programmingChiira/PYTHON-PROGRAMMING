# If the number of arguments is unknown, add a * before the parameter name:
def my_function(*siblings):
    print("The youngest sibling is " + siblings[-1])

my_function("Joseph", "Dennis", "Magdalene") 