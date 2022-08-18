from random import seed
from random import randint

seed(1)

number = randint(0, 1000000)

def palindrome(number):
    print("original number", number)
    original_num = number

    # reverse the given number
    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10

    # check numbers
    if original_num == reverse_num:
        print("Given number palindrome")
    else:
        print("Given number is not palindrome")

palindrome(int(number))
