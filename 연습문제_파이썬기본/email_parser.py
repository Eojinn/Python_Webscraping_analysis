# 1. 사용자로부터 이메일 주소 입력 받기
email = input("이메일 주소를 입력하세요: ")

# 2. @ 기호를 기준으로 사용자명(Username)과 도메인(Domain) 분리
# split() 함수는 기준 문자를 중심으로 문자열을 잘라 리스트로 만듦
# 예: "user@example.com".split('@') -> ["user", "example.com"]
user_info = email.split('@')

# 3. 리스트의 인덱스를 활용해 결과 출력
# 인덱스 0번은 앞부분(사용자명), 1번은 뒷부분(도메인)임
username = user_info[0]
domain = user_info[1]

print(f"사용자명: {username}")
print(f"도메인: {domain}")