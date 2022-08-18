input_string = input('Enter elements of a list separated by space ')
print("\n")
user_list = input_string.split()
# print list
print('list: ', user_list)

num1 = user_list[0]
num_last = user_list[-1]

if num1 == num_last:
    print("The first and last numbers are the same")
else:
    print("The first and last numbers aren't the same")
