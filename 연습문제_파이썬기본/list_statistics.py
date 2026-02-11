# 1. 5개의 숫자를 리스트에 저장
# 직접 입력받는 대신 문제의 예시 데이터를 리스트로 만듦
numbers = [10, 20, 30, 40, 50]

# 2. 합계 계산
# sum() 함수는 리스트 안의 모든 숫자를 더해줍니다.
total = sum(numbers)

# 3. 평균 계산
# 평균 = 합계 / 데이터 개수 (len() 함수 사용)
average = total / len(numbers)

# 4. 결과 출력
print(f"숫자들: {numbers}")
print(f"합계: {total}")
print(f"평균: {average:.1f}")