while True:
    cmd = input("Enter operation (add/sub/mul/div) or 'exit' to quit: ")

    if cmd == "exit":
        print("Program terminated")
        break

    parts = cmd.split()

    if len(parts) != 3:
        print("Invalid input format")
        continue

    op, a, b = parts
    a, b = int(a), int(b)

    if op == "add":
        print("Result:", a + b)
    elif op == "sub":
        print("Result:", a - b)
    elif op == "mul":
        print("Result:", a * b)
    elif op == "div":
        if b == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print("Result:", a / b)
    else:
        print("Invalid operation")
