'''
 This problem was recently asked by LinkedIn:

Given two rectangles, find the area of intersection.

Here's some starter code and a starter example:

class Rectangle():
  def __init__(self, min_x=0, min_y=0, max_x=0, max_y=0):
    self.min_x = min_x
    self.min_y = min_y
    self.max_x = max_x
    self.max_y = max_y

def intersection_area(rect1, rect2):
  # Fill this in.
  
rect1 = Rectangle(0, 0, 3, 2)
rect2 = Rectangle(1, 1, 3, 3)

print(intersection_area(rect1, rect2))
# 2
'''

class Rectangle(object):
    def __init__(self, min_x=0, min_y=0, max_x=0, max_y=0):
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y


def intersection_area(rect1, rect2):
    if (rect1.min_x > rect2.max_x or rect2.min_x > rect1.max_x) or \
        (rect1.min_y > rect2.max_y or rect2.min_y > rect1.max_y):
        return None

    bottom_left_x = max(rect1.min_x, rect2.min_x)
    bottom_left_y = max(rect1.min_y, rect2.min_y)

    top_right_x = min(rect1.max_x, rect2.max_x)
    top_right_y = min(rect1.max_y, rect2.max_y)

    return (top_right_x - bottom_left_x) * (top_right_y - bottom_left_y)

rect1 = Rectangle(0, 0, 3, 2)
rect2 = Rectangle(1, 1, 3, 3)
print(intersection_area(rect1, rect2))

rect1 = Rectangle(0, 0, 10, 8)
rect2 = Rectangle(2, 3, 7, 9)
print(intersection_area(rect1, rect2))

rect1 = Rectangle(0, 0, 10, 8)
rect2 = Rectangle(-2, 3, -7, 9)
print(intersection_area(rect1, rect2))

rect1 = Rectangle(0, 0, 10, 8)
rect2 = Rectangle(-2, -3, 0, 0)
print(intersection_area(rect1, rect2))
