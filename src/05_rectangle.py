print("Enter the smaller side of the rectangle ")
sm = int(input(">>> "))
print("Enter the bigger side of the rectangle ")
bg = int(input(">>> "))
for i in range(1, sm + 1):
    print("*" * bg)

print("------------")


print("*" * bg)
for i in range(1, sm - 1):
    print("*" + " " * (bg - 2) + "*")
print("*" * bg)
