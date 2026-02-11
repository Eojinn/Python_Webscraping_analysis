# 1. 과일 목록 리스트 생성
fruits = ['사과', '바나나', '오렌지', '포도', '딸기']

# 2. enumerate를 사용하여 인덱스와 값을 함께 출력
# enumerate()는 (인덱스, 값) 형태의 튜플을 반환
print("과일 목록:")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")