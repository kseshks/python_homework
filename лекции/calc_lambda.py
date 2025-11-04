str = "11 + 38 * 8"

# Обратная польская нотация 
ops = ['+', '-', '*', '/']
result = [] 
stack = []   
num = ''     

for char in str:
    if char.isdigit():
        num += char
    elif char in ops:
        if num:
            result.append(int(num))
            num = ''
        while stack and ops.index(stack[-1]) >= ops.index(char):
            result.append(stack.pop())
        stack.append(char)

if num:
    result.append(int(num))

while stack:
    result.append(stack.pop())

print(result)

#2
calc_stack = []

for token in result:
    if isinstance(token, int):
        calc_stack.append(token)
    else:
        b = calc_stack.pop()
        a = calc_stack.pop()
        if token == '+':
            calc_stack.append(a + b)
        elif token == '-':
            calc_stack.append(a - b)
        elif token == '*':
            calc_stack.append(a * b)
        elif token == '/':
            calc_stack.append(a / b)

print(calc_stack[-1])