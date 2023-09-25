# The following example shows how to use a default parameter value.
# If we call the function without argument, it uses the default value.

def my_function(country = "Kenya"):
    print("I am from " + country)

my_function("Ethiopia")
my_function("Eritrea")
my_function()
my_function("Uganda") 