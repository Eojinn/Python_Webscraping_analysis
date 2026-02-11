# 1. 사칙연산 함수 정의
def add(a, b):
    """두 수를 더한 결과를 반환합니다."""
    return a + b

def subtract(a, b):
    """두 수를 뺀 결과를 반환합니다."""
    return a - b

def multiply(a, b):
    """두 수를 곱한 결과를 반환합니다."""
    return a * b

def divide(a, b):
    """두 수를 나눈 결과를 반환합니다."""
    if b == 0:
        return "0으로 나눌 수 없습니다."
    return a / b

# 2. 메인 실행부
x, y = 10, 5

# 각 함수를 호출하여 결과 출력
print(f"{x} + {y} = {add(x, y)}")
print(f"{x} - {y} = {subtract(x, y)}")
print(f"{x} * {y} = {multiply(x, y)}")
print(f"{x} / {y} = {divide(x, y)}")