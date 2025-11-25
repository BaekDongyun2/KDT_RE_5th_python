def add(a, b):
    return print(a + b)

def subtract(a, b):
    return print(a - b)

def multiply(a, b):
    return print(a * b)

def divide(a, b):
    if b == 0:
        print("0으로 나눌 수 없습니다.")
        return None
    else:
        return print(a / b)