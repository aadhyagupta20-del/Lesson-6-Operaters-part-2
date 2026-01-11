c = input("Enter a character: ")
if len(c) != 1:
    print("Please enter exactly one character.")
elif '0' <= c <= '9':
    print("It is a number.")
elif 'A' <= c <= 'Z' or 'a' <= c <= 'z':
    print("It is a letter.")
else:
    print("It is neither a number nor a letter.")