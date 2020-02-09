'''
Given an integer, reverse the digits. Do not convert the integer into a string and reverse it.

Here's some examples and some starter code.

def reverse_integer(num):
  # Fill this in.
  
print(reverse_integer(135))
# 531

print(reverse_integer(-321))
# -123
'''

def reverse_integer(num):
    negative = False
    if num < 0:
        negative = True
        num *= -1
    
    reverse = 0
    while num > 0:
        reverse = reverse * 10 + num % 10
        num //= 10

    return reverse * -1 if negative else reverse    
  
print(reverse_integer(135))
# 531

print(reverse_integer(-321))
# -123