# 1. 사용자로부터 출력할 단 입력 받기
dan = int(input("몇 단을 출력할까요? "))

# 2. 구구단 제목 출력
print(f"{dan}단 구구단:")

# 3. 반복문을 사용하여 1부터 9까지 곱셈 결과 출력
# range(1, 10)은 1부터 9까지의 숫자를 생성합니다.
for i in range(1, 10):
    result = dan * i
    print(f"{dan} x {i} = {result}")