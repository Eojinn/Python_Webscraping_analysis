import datetime

# 변수 정의
name = "김철수"
age = 25
pi = 3.14159
price = 1234
percentage = 0.855
today = datetime.date(2025, 7, 20)

# 1. 기본 변수 삽입
print(f"이름: {name}, 나이: {age}")

# 2. 소수점 자릿수 제어 (:.2f는 소수점 둘째 자리까지 표시)
print(f"원주율: {pi:.2f}")

# 3. 천 단위 구분 기호 (:,는 콤마 추가)
print(f"가격: {price:,}원")

# 4. 퍼센트 표시 (:.2%는 100을 곱하고 소수점 둘째 자리까지 % 표시)
print(f"퍼센트: {percentage:.2%}")

# 5. 날짜 포매팅 (: 뒤에 strftime 형식을 지정)
print(f"날짜: {today:%Y년 %m월 %d일}")