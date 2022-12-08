#namedtuple is a lightweight object type
from collections import namedtuple, deque
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt.x, pt.y)

#double ended queue to add or rmemove elements from both ends efficiently
d=deque()

d.append(1)
d.append(2)

d.appendleft(3)
print(d)

d.extend([4,5,6]) #add the elements on the right
print(d)

d.extendleft([4,5,6]) #add the elements on the left
print(d)

d.rotate(1) #rotates elements one step to the right
print(d)

d.rotate(2) #rotates elements two steps to the right
print(d)

d.rotate(-1) #rotates elements one step to the left
print(d)

d.pop()
print(d)

d.popleft()
print(d)

d.clear()
print(d)


