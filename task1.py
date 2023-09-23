# PALINDROME CHACKER

#function for string checker
def is_pd (input_str):
    input_str = input_str.replace('','').lower()  # for making case-insensitive and ignor spaces
    return input_str == input_str[::-1]   # for compare input_str with its reverse

# get input from the user
user_word = input('ENTER WORD TO CHECK IF WORD IS PALINDROME = ')

# Conditions for checking palindrome
if is_pd(user_word):
    print(f"{user_word} it is a palindrome")
else:
    print(f"{user_word} it is not a palindrome")
