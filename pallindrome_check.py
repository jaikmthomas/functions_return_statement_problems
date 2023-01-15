#Write a function that takes in a string and determines whether the string is a Palindrome or not (reads the same forwards and backward). The function should return a boolean value (True, False) depending on whether the string is a Palindrome.

#Examples of Palindromes: Racecar, Kayak
s = input("Enter a word to check:")
def Palindrome(s):
    return s == s[::-1]

if Palindrome(s):
    print(s+" is pallindrome")
else:
    print(s+" is not a pallindrome")