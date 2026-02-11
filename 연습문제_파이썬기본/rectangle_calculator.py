# 1. 사용자로부터 가로와 세로 길이 입력 받기
width = int(input("가로 길이를 입력하세요: "))
height = int(input("세로 길이를 입력하세요: "))

# 2. 직사각형의 넓이와 둘레 계산
# 넓이 공식: 가로 * 세로
area = width * height
# 둘레 공식: (가로 + 세로) * 2
perimeter = (width + height) * 2

# 3. 결과 출력
print(f"직사각형의 넓이: {area}")
print(f"직사각형의 둘레: {perimeter}")