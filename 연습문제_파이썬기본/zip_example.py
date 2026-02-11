# 1. 데이터 리스트 준비
students = ['김철수', '이영희', '박민수', '최수진']
scores = [85, 92, 78, 95]

# 2. zip을 사용한 학생과 점수 매칭 출력
print("학생과 점수 매칭:")
# zip은 두 리스트에서 요소를 하나씩 꺼내 튜플 형태로 전달
for student, score in zip(students, scores):
    print(f"{student}: {score}점")

# 3. zip을 사용하여 리스트를 딕셔너리로 변환
# dict() 함수에 zip 객체를 넣으면 첫 번째 리스트가 Key, 두 번째가 Value가 됨
student_dict = dict(zip(students, scores))

print(f"\n점수별 학생 딕셔너리: {student_dict}")