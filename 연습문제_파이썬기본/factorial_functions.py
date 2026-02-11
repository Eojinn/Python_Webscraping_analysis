# 1. 재귀 함수(Recursive Function)를 이용한 방식
def factorial_recursive(n):
    # 기저 조건(Base Case): 1 이하일 때 1을 반환하여 멈춤
    if n <= 1:
        return 1
    # 재귀 단계: n * (n-1)!
    return n * factorial_recursive(n - 1)

# 2. 반복문(Loop)을 이용한 방식
def factorial_iterative(n):
    result = 1
    # 1부터 n까지 차례대로 곱함
    for i in range(1, n + 1):
        result *= i
    return result

# 3. 결과 출력
numbers = [5, 7]

for num in numbers:
    print(f"{num}! (재귀) = {factorial_recursive(num)}")
    print(f"{num}! (반복) = {factorial_iterative(num)}")