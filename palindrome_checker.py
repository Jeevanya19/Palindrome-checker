
# Palindrome Checker

text = input("Enter a word or sentence: ")

# Convert to lowercase and remove spaces
cleaned_text = text.lower().replace(" ", "")

# Reverse the text
reversed_text = cleaned_text[::-1]

# Check whether it is a palindrome
if cleaned_text == reversed_text:
    print("It is a palindrome!")
else:
    print("It is not a palindrome.")
