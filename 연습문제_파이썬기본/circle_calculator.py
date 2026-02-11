# 1. 사용자로부터 반지름 입력 받기
radius = float(input("원의 반지름을 입력하세요: "))

# 2. 상수 정의 (π)
PI = 3.14159

# 3. 원의 넓이와 둘레 계산
# 넓이 공식: π * r^2
area = PI * (radius ** 2)
# 둘레 공식: 2 * π * r
circumference = 2 * PI * radius

# 4. 결과 출력 (소수점 둘째 자리까지)
print(f"반지름이 {radius:.0f}인 원의 넓이: {area:.2f}")
print(f"반지름이 {radius:.0f}인 원의 둘레: {circumference:.2f}")