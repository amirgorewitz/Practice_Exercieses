input_string = input('Enter elements of a list separated by space ')
print("\n")
user_list = input_string.split()
# print list
print('list: ', user_list)

for user in user_list:
    user = int(user)
    decimal = user % 5
    if decimal == 0:
        print (str(user) + " is a diviser of 5")
    else:
        print (str(user) + " is not a diviser of 5")
