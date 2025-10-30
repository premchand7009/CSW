stack = []

def push(x):
    stack.append(x)

def pop():
    if isempty():
        print("Stack is empty! Cannot pop.")
        return None
    return stack.pop()

def isempty():
    return len(stack) == 0

def display():
    if isempty():
        print("Stack is empty.")
    else:
        print("Stack elements (top to bottom):")
        for item in reversed(stack):
            print(item)

def evaluate_rpn(expression):
    stack.clear()
    tokens = expression.split()  # split by space for multi-digit numbers
    for token in tokens:
        if token.isdigit():
            push(int(token))
        elif token in "+-*/":
            op2 = pop()
            op1 = pop()
            if op1 is None or op2 is None:
                print("Invalid expression.")
                return
            match token:
                case '+':
                    push(op1 + op2)
                case '-':
                    push(op1 - op2)
                case '*':
                    push(op1 * op2)
                case '/':
                    push(op1 // op2)
        else:
            print(f"Invalid token: {token}")
            return
    if len(stack) == 1:
        print("Result:", pop())
    else:
        print("Invalid RPN expression.")

while True:
    print("\nStack Operations:")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Evaluate RPN")
    print("5. Exit")

    choice = input("Enter choice: ")

    match choice:
        case '1':
            value = input("Enter element to push: ")
            push(int(value))
        case '2':
            popped = pop()
            if popped is not None:
                print(f"Popped element: {popped}")
        case '3':
            display()
        case '4':
            expr = input("Enter RPN Expression (use spaces, e.g., 9 8 7 5 + *): ")
            evaluate_rpn(expr)
        case '5':
            print("Exiting program...")
            break
        case _:
            print("Invalid choice! Please try again.")
