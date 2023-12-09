# A.Jumping the Queue  

from collections import deque

lines = open('hw3_q1.txt').readlines()

queue = deque([])

for line in lines:
    operation, name = line.strip().split(' ')

    if operation == 'JOIN':
        queue.appendleft(name)
    elif operation == 'JUMP':
        queue.append(name)

print("Result:", ', '.join(list(queue)))    

# B.Time and Space Complexity: it is O (n) for both, because the loop runs (n) times, linearly depends on the number of operations processed from the input file 
# and it scales linearly with the input size.
