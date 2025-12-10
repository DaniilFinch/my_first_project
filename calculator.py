def calculator():
    print("Калькулятор")
    num1 = float(input("Первое число: "))
    operation = input("Операция (+, -): ")
    num2 = float(input("Второе число: "))
    
    if operation == "+":
        print(f"Результат: {num1 + num2}")
    elif operation == "-":
        print(f"Результат: {num1 - num2}")
    else:
        print("Неподдерживаемая операция")

if __name__ == "__main__":
    calculator()
