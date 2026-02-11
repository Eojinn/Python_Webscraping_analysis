# math_operations.py 파일에서 정의된 함수들을 불러옴
import math_operations as mo

# 1. 원의 넓이 (반지름 5)
area_c = mo.circle_area(5)
print(f"원의 넓이: {area_c:.2f}")

# 2. 직사각형 넓이 (가로 10, 세로 5)
area_r = mo.rectangle_area(10, 5)
print(f"직사각형 넓이: {area_r}")

# 3. 팩토리얼 5!
fact_5 = mo.factorial(5)
print(f"팩토리얼 5! = {fact_5}")

# 4. 최대공약수 (48, 18)
common_div = mo.gcd(48, 18)
print(f"최대공약수(48, 18) = {common_div}")