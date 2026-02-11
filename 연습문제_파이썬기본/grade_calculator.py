# 1. 사용자로부터 점수 입력 받기
score = int(input("점수를 입력하세요: "))

# 2. 조건문을 사용하여 학점 결정
# 상위 조건부터 순차적으로 검사하므로 범위 설정이 간결해짐
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

# 3. 결과 출력
print(f"점수 {score}점의 학점은 {grade}입니다.")