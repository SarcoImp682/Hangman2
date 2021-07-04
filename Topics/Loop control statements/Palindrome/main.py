word = input()
is_it = ''.join(reversed(word))
if word != is_it:
    print("Not palindrome")
else:
    print("Palindrome")
