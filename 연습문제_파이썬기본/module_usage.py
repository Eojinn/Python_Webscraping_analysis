import datetime
import random

# 1. datetime 활용: 날짜와 시간
# 현재 시각 가져오기 (출력 예시와 일치시키기 위해 임의 설정 가능)
now = datetime.datetime.now()
print(f"현재 날짜와 시간: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# 날짜 포맷팅: %A는 요일을 나타냅니다.
# (참고: 한국어 요일을 출력하려면 별도의 설정이나 리스트 매핑이 필요할 수 있음)
formatted_date = now.strftime("%Y년 %m월 %d일")
# 요일 한글 매핑 예시
days = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
weekday_kr = days[now.weekday()]
print(f"포맷된 날짜: {formatted_date} {weekday_kr}")

# 2. random 활용: 무작위 생성
# 지정된 범위 내의 임의의 정수 (1~10)
rand_int = random.randint(1, 10)
print(f"임의의 숫자: {rand_int}")

# 임의의 실수 (0.0 ~ 1.0 사이의 값을 스케일링)
rand_float = round(random.uniform(1.0, 5.0), 2)
print(f"임의의 실수: {rand_float}")

# 리스트에서 임의의 요소 하나 선택
fruits = ['사과', '바나나', '오렌지', '포도', '딸기']
print(f"임의의 리스트 요소: {random.choice(fruits)}")

# 리스트 요소 섞기 (원본 리스트를 직접 변경함)
random.shuffle(fruits)
print(f"섞인 리스트: {fruits}")