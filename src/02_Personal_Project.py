print("Enter the text ")
text = input(">>> ")
print("Choose the operations (Lower or Upper)")
op = input(">>> ")
op = op.lower()


def low():
    print(text.lower())


def up():
    print(text.upper())


if op == "lower":
    low()
elif op == "upper":
    up()
else:
    print("Sorry, but on this version we don't have this operation. ")
