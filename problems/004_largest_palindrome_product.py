# https://projecteuler.net/problem=4

def is_palindrome(word):
    return str(word) == str(word)[::-1]

max_palindrome = 0

for a in range(1000):
    for b in range(1000):
        if is_palindrome(a*b):
            max_palindrome = max(a*b, max_palindrome)

print(max_palindrome)