# is_palindrome
# Write a function called is_palindrome. A Palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward. This function should take in one parameter and returns True or False depending on whether it is a palindrome. As a bonus, allow your function to ignore whitespace and capitalization so that is_palindrome('a man a plan a canal Panama') returns True.

def is_palindrome(string):
    modified_string = string.replace(' ', '').lower()
    return modified_string == modified_string[::-1]
   
    

print(is_palindrome('panos BezAS'))