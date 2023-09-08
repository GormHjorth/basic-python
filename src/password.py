import sys

if len(sys.argv) != 2:
    print(f"{sys.argv[0]} expected exactly one argument.")
    sys.exit(1)

password = sys.argv[1]
is_valid = False

# Do all the requirement checks here.

lower = False
upper = False
numeric = False
other = False
if 6<=len(password)<=16:
    length = True
else:
    length = False
    

for x in password:
    if x.islower:
        lower = True
    if x.isupper:
        upper = True
    if x.isnumeric:
        numeric = True
    if x in "$#@":
        other = True

if lower and upper and numeric and other and length == True:
    is_valid = True

print(is_valid)
