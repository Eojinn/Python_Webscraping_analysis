# 1. 테스트할 숫자 리스트 정의
numbers1 = [2, 4, 6, 8, 10]
numbers2 = [1, 3, 5, 7, 12]

# 2. 리스트1 검사
print(f"숫자 리스트: {numbers1}")
# 모든 수가 짝수인지 검사 (all 사용)
print(f"모든 수가 짝수인가? {all(n % 2 == 0 for n in numbers1)}")
# 10보다 큰 수가 하나라도 있는지 검사 (any 사용)
print(f"하나라도 10보다 큰 수가 있는가? {any(n > 10 for n in numbers1)}")

print() # 줄바꿈

# 3. 리스트2 검사
print(f"숫자 리스트2: {numbers2}")
print(f"모든 수가 짝수인가? {all(n % 2 == 0 for n in numbers2)}")
print(f"하나라도 10보다 큰 수가 있는가? {any(n > 10 for n in numbers2)}")