# 1. 원본 리스트 정의
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 2. map을 사용하여 모든 수의 제곱 구하기
# map(함수, 반복가능객체)
squared_numbers = list(map(lambda x: x**2, numbers))

# 3. filter를 사용하여 5보다 큰 수들만 골라내기
# filter(함수, 반복가능객체)
filtered_numbers = list(filter(lambda x: x > 5, numbers))

# 4. filter와 map을 조합하여 5보다 큰 수들의 제곱 구하기
# 5보다 큰 수를 먼저 거르고(filter), 그 결과에 제곱을 적용(map)
combined_result = list(map(lambda x: x**2, filter(lambda x: x > 5, numbers)))

# 5. 결과 출력
print(f"원본 숫자: {numbers}")
print(f"모든 수의 제곱: {squared_numbers}")
print(f"5보다 큰 수들: {filtered_numbers}")
print(f"5보다 큰 수들의 제곱: {combined_result}")