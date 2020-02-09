'''Hi, here's your problem today. This problem was recently asked by Twitter:

Implement a class for a stack that supports all the regular functions (push, pop) and an additional function of max() which returns the maximum element in the stack (return None if the stack is empty). Each method should run in constant time.

class MaxStack:
  def __init__(self):
    # Fill this in.

  def push(self, val):
    # Fill this in.

  def pop(self):
    # Fill this in.

  def max(self):
    # Fill this in.

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print s.max()
# 3
s.pop()
s.pop()
print s.max()
# 2
'''

class MinMaxStack:
    def __init__(self):
        self._stack = []

    def push(self, val):
        self._stack.append(val)

    def pop(self):
        self._stack.pop()

    def max(self):
        return max(self._stack)
        
    def min(self):
     return min(self._stack)

s = MinMaxStack()
s.push(1)
s.push(-2)
s.push(3)
s.push(2)
s.push(-3)
print(s.max())
print(s.min())

s.pop()
s.pop()
print(s.max())
print(s.min())
