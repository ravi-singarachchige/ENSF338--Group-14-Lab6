class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def parse_expression(expression):
    tokens = list(expression.replace(' ', ''))
    stack = []
    operator_stack = []
    precedence = {'+':1, '-':1, '*':2, '/':2}

    i = 0
    while i < len(tokens):
        if tokens[i].isdigit():
            j = i
            while j < len(tokens) and tokens[j].isdigit():
                j += 1
            stack.append(Node(int(''.join(tokens[i:j]))))
            i = j
        elif tokens[i] in '+-*/':
            while operator_stack and operator_stack[-1] in '+-*/' and precedence[tokens[i]] <= precedence[operator_stack[-1]]:
                operator = operator_stack.pop()
                right = stack.pop()
                left = stack.pop()
                stack.append(Node(operator, left, right))
            operator_stack.append(tokens[i])
            i += 1
        elif tokens[i] == '(':
            operator_stack.append(tokens[i])
            i += 1
        elif tokens[i] == ')':
            while operator_stack[-1] != '(':
                operator = operator_stack.pop()
                right = stack.pop()
                left = stack.pop()
                stack.append(Node(operator, left, right))
            operator_stack.pop()  # pop the '('
            i += 1
    while operator_stack:
        operator = operator_stack.pop()
        right = stack.pop()
        left = stack.pop()
        stack.append(Node(operator, left, right))
    return stack[0]

def calculate(node):
    if isinstance(node.value, int):
        return node.value
    elif node.value == '+':
        return calculate(node.left) + calculate(node.right)
    elif node.value == '-':
        return calculate(node.left) - calculate(node.right)
    elif node.value == '*':
        return calculate(node.left) * calculate(node.right)
    elif node.value == '/':
        return calculate(node.left) / calculate(node.right)

expression = input('Enter an expression: ')
tree = parse_expression(expression)
result = calculate(tree)
print(result)