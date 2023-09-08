
# Print the pattern
for x in range(4,-5,-1):
    if x >= 0:
        x = abs(x - 5)
    else:
        x = abs(x + 5)
    y = ""
    while x > 0:
        y = "*" + y
        x = x-1

    y = " ".join(y)
    print(y)
