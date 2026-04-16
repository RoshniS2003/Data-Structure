def evaluate_postfix(expression):
    stack = []

    for char in expression:
        # If operand (number)
        if char.isdigit():
            stack.append(int(char))
        
        # If operator
        else:
            b = stack.pop()
            a = stack.pop()
            
            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            elif char == '/':
                stack.append(a / b)

    return stack.pop()


# Example
exp = "23*54*+9-"
result = evaluate_postfix(exp)

print("Postfix Expression:", exp)
print("Result:", result)