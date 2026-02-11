import csv

# 1. 저장할 데이터 준비 (이름, 점수)
grades_data = [
    ["김철수", 85],
    ["이영희", 92],
    ["박민수", 78],
    ["최수진", 95]
]

filename = "grades.csv"

# 2. CSV 파일 저장
with open(filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    # 한꺼번에 모든 행을 씀
    writer.writerows(grades_data)

print(f"학생 성적이 {filename}에 저장되었습니다.\n")

# 3. CSV 파일 읽기 및 평균 계산
print("성적 분석 결과:")
total_score = 0
student_count = 0

with open(filename, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        name = row[0]
        score = int(row[1]) # 읽어온 데이터는 문자열이므로 숫자로 변환
        
        print(f"{name}: {score}점")
        
        total_score += score
        student_count += 1

# 4. 전체 평균 계산 및 출력
if student_count > 0:
    average = total_score / student_count
    print(f"전체 평균: {average:.1f}점")