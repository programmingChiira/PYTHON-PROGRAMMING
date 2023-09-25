# If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_function(**sibling):
    print("The last name is " + sibling["last_name"])

my_function(first_name = "Joseph", last_name = "Dennis") 