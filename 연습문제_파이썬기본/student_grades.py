# 1. 학생들의 성적을 딕셔너리에 저장
grades = {
    "김철수": 85,
    "이영희": 92,
    "박민수": 78,
    "최수진": 95
}

# 2. 학생 성적 목록 출력
print("학생 성적:")
# items() 메서드를 사용하여 이름과 점수를 동시에 가져옴
for name, score in grades.items():
    print(f"{name}: {score}점")

# 3. 평균 점수 계산
# values() 메서드로 점수들만 모은 뒤 sum()과 len()으로 평균을 구함
scores = grades.values()
average = sum(scores) / len(scores)

# 4. 평균 점수 출력
print(f"평균 점수: {average:.1f}점")