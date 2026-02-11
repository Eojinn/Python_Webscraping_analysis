# 1. 숫자 목록 리스트 생성
numbers = [15, 3, 27, 8, 19, 12, 31]

# 2. 숫자 목록 출력
print(f"숫자 목록: {numbers}")

# 3. 최댓값과 최솟값 찾기 (내장 함수 활용)
max_val = max(numbers)
min_val = min(numbers)

# 4. 두 번째로 큰 값 찾기
# 리스트를 복사한 뒤 정렬하여 뒤에서 두 번째 값을 선택
# 원본 리스트를 유지하기 위해 sorted()를 사용하거나 copy를 활용
sorted_numbers = sorted(numbers, reverse=True) # 내림차순 정렬
second_max = sorted_numbers[1] # 인덱스 0이 최댓값, 1이 두 번째 큰 값

# 5. 결과 출력
print(f"최댓값: {max_val}")
print(f"최솟값: {min_val}")
print(f"두 번째로 큰 값: {second_max}")