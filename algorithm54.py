n = int(input())
left_stack = []
right_stack = []
for i in range(n):
    words = input()
    for word in words:
        if word == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif word == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        elif word == '-':
            if left_stack:
                left_stack.pop()
        else:
            left_stack.append(word)
    left_stack.extend(reversed(right_stack))
    print(''.join(left_stack))


        
