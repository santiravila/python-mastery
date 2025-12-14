expression = input("Expression: ").strip()
first_operand, operation, second_operand = expression.split(' ')

match operation:
    case "+":
        print(f"{float(first_operand) + float(second_operand):.1f}")
    case "-":
        print(f"{float(first_operand) - float(second_operand):.1f}")
    case "*":
        print(f"{float(first_operand) * float(second_operand):.1f}")
    case "/":
        print(f"{float(first_operand) / float(second_operand):.1f}")