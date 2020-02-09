'''
This problem was recently asked by Uber:

Given a string s and a character c, find the distance for all characters in the string to the character c in the string s.
You can assume that the character c will appear at least once in the string.

Here's an example and some starter code:

def shortest_dist(s, c):
  # Fill this in.

print(shortest_dist('helloworld', 'l'))
# [2, 1, 0, 0, 1, 2, 2, 1, 0, 1]
'''
import time

def shortest_dist(string, character):
    char_index = [i for i, x in enumerate(string) if x == character]
    return [min([abs(i - m) for m in char_index]) for i, x in enumerate(string)]    

start = time.time()
print(shortest_dist('helloworld', 'l'))
print(time.time() - start)