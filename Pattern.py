x = int(input("Input a number: "))
for num in range(x + 1):
    for i in range(num):
        print (num, end=" ") #print number
    # new line after each row to display pattern correctly
    print("\n")
