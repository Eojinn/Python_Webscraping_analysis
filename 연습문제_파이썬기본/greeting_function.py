# 1. 인사말 생성 함수 정의
# greeting과 suffix에 기본값을 설정
def create_greeting(name, greeting="안녕하세요", suffix="!"):
    return f"{greeting}, {name}님{suffix}"

# 2. 영문 인사를 위한 별도 함수 (출력 예시 맞춤)
def create_greeting_en(name, greeting="Hello", suffix="!"):
    return f"{greeting}, {name}{suffix}"

# 3. 결과 출력
# 인자를 하나만 전달 (나머지는 기본값 사용)
print(create_greeting("김철수"))

# 모든 인자를 커스텀하게 전달 (영문 버전)
print(create_greeting_en("John"))

# 모든 인자를 전달 (기본값 대신 입력한 값 사용)
print(create_greeting("이영희", suffix="님! 좋은 하루 되세요!"))