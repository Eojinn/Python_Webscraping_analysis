# 1. 사용자로부터 두 개의 정수 입력 받기
try:
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))

    # 2. 사칙연산 수행 및 결과 출력
    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    print(f"{num1} * {num2} = {num1 * num2}")

    # 3. 나눗셈 처리 (0으로 나누는 경우 예외 처리 및 소수점 2자리 제한)
    if num2 != 0:
        # 결과 예시인 3.33에 맞춰 소수점 둘째 자리까지 출력합니다.
        print(f"{num1} / {num2} = {num1 / num2:.2f}")
    else:
        print("0으로 나눌 수 없습니다.")

except ValueError:
    print("정수만 입력 가능합니다. 프로그램을 다시 실행해 주세요.")