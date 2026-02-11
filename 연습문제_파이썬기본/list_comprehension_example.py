# 1. 원본 리스트 생성
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 2. 리스트 컴프리헨션으로 짝수만 추출
# [표현식 for 항목 in 반복가능객체 if 조건]
even_numbers = [num for num in numbers if num % 2 == 0]

# 3. 리스트 컴프리헨션으로 짝수의 제곱 계산
squared_evens = [num ** 2 for num in numbers if num % 2 == 0]

# 4. 결과 출력
print(f"원본 리스트: {numbers}")
print(f"짝수들: {even_numbers}")
print(f"짝수의 제곱: {squared_evens}")