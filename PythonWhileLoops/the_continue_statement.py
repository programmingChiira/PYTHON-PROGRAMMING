# With the continue statement we can stop the current iteration, and continue with the next:

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# Note that number 3 is missing in the result