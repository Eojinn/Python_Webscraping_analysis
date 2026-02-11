# 1. 기본 삼항 연산자 활용
# [참일 때의 값] if [조건문] else [거짓일 때의 값]
score = 85
result = "합격" if score >= 80 else "불합격"
print(f"점수: {score}, 결과: {result}")

# 2. 나이에 따른 상태 판별
age = 17
status = "성인" if age >= 19 else "미성년자"
print(f"나이: {age}, 상태: {status}")

# 3. 두 숫자 중 최대값 찾기 (내장 함수 max()와 동일한 논리)
a, b = 15, 42
max_value = a if a > b else b
print(f"숫자들의 최대값: {max_value}")

# 4. 리스트 컴프리헨션과 결합 (필터링)
# 양수만 골라내는 예시
numbers = [5, -3, 12, 0, 8, -1, 23]
positives = [n for n in numbers if n > 0]
print(f"양수들: {positives}")