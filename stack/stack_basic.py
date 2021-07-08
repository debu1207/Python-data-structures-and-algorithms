"""
stack functions are:

empty(), size(), top(), push(g), pop()

it can implemented using list or collections.deque or queue.LifoQueue
"""

# Implementing stack using list

stack = []
stack.append(1)
stack.append(3)
stack.append(7)

print(f'Initial stack')
print(stack)

# pop() function to pop
print(f'Elements poped from stack: ')
print(stack.pop())
print(stack.pop())
print(f'Stack after Elements are poped: ')
print(stack)