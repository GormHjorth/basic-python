import sys

# This program should take two arguments, a command--either "encode" or "decode"--
# and then a string.

if len(sys.argv) != 3:
    print("Incorrect number of arguments.", file=sys.stderr)
    print(f"Usage: {sys.argv[0]} command string\n", file=sys.stderr)
    sys.exit(1)

command, x = sys.argv[1:3]

match command:
    case "encode":
        # Implement the encoding here
        encoding = ""
        for i in x:
            i = "".join(i)
            i = hex(ord(i))
            encoding = encoding + i
        print(encoding)

    case "decode":
        # Implement the decoding here
        decoding = ""
        x = x.split("0x")
        for i in x[1:]: 
            print(i)
            i = int(i, base = 16)
            i = chr(i)
            decoding = decoding + i
        print(decoding)

