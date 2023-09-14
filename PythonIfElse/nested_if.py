# You can have if statements inside if statements, this is called nested if statements.

x = 20

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    elif x == 20:
        print("and equal to 20!")
    else:
        print("but not above 20.") 