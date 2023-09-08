
# Print the numbers described in the exercise
for x in range(1,11):
    y = ""
    while x > 0:
        y =  str(x) + " " + y 
        x = x-1
    print(y)
