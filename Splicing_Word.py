# accept input string from a user
word = input('Enter word ')

n = int(input("How many letters to remove from the word? "))

word_len = len(word)

spliced_word = word[n:]

if n > word_len:
    print("You asked to remove more letters than there are in the word")
else:
    print(spliced_word)
