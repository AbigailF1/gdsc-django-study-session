print("Enter a word: ")
word = input()
r_word ="".join(reversed(list(word)))
if r_word == word:
    print(word + " is a palindrome")
else:
    print(word + " is not a palindrome")
