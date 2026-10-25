word = "Programming"

# reversed using slicing
print(word[::-1])

#  first 3 and last 3 on one line
print(word[:3], word[-3:])

# count "m" in word
print(word.count("m"))

# is_palindrome function check word same after reverse
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("level"), is_palindrome("python"))