# 1. 사용자로부터 숫자 입력 받기
number = int(input("숫자를 입력하세요: "))

# 2. 소수 판별 로직
is_prime = True

# 1은 소수가 아니므로 별도로 체크
if number < 2:
    is_prime = False
else:
    # 2부터 해당 숫자 직전까지 나누어 떨어지는지 확인
    for i in range(2, number):
        if number % i == 0:
            is_prime = False  # 나누어 떨어지는 수가 있으면 소수가 아님
            break             # 더 이상 검사할 필요 없으므로 탈출

# 3. 결과 출력
if is_prime:
    print(f"{number}은(는) 소수입니다.")
else:
    print(f"{number}은(는) 소수가 아닙니다.")