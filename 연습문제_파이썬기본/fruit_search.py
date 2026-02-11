# 1. 과일 이름들이 담긴 리스트 생성
fruits = ['사과', '바나나', '오렌지', '포도', '딸기']

# 2. 과일 목록 출력
print(f"과일 목록: {fruits}")

# 3. 사용자로부터 찾을 과일 이름 입력 받기
search_fruit = input("찾을 과일을 입력하세요: ")

# 4. 리스트 내에 해당 과일이 있는지 검색 (in 연산자 활용)
if search_fruit in fruits:
    print(f"'{search_fruit}'가 목록에 있습니다!")
else:
    print(f"'{search_fruit}'가 목록에 없습니다.")