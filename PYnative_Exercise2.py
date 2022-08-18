num1 = int(input("Input a number: "))

previous_num = 0
second_num = 0

print("Current number " + str(previous_num) + ". Next number " + str(second_num))

for x in range(num1):

    second_num = previous_num + 1
    previous_num = previous_num + 1

    print("Current number " + str(previous_num) + ". Next number " + str(second_num) + ". The sum of the numbers: " + str(second_num + previous_num))
