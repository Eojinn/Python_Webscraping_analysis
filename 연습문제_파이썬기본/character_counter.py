# 1. 사용자로부터 전체 문자열과 찾을 문자 입력 받기
text = input("문자열을 입력하세요: ")
char_to_find = input("찾을 문자를 입력하세요: ")

# 2. 특정 문자가 몇 번 나타나는지 세기
# count() 메서드는 인자로 전달된 문자가 문자열 내에 몇 개 있는지 반환합니다.
count = text.count(char_to_find)

# 3. 결과 출력
print(f"문자 '{char_to_find}'이 {count}번 나타납니다.")