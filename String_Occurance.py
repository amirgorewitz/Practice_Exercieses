sentence = input("Please write a sentence or two. ")

find_word = input("Which word do you want to check its occurance? ")
find_word_lower = find_word.lower()

words = sentence.split()
words = sentence.lower()



occurance = words.count(find_word_lower)
print ("The word - " + find_word + " - occurs " + str(occurance) + " times in the sentence.")
