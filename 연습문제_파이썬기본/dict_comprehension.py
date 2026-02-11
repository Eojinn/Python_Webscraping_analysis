# 1. 1부터 5까지의 숫자와 그 제곱값을 담은 딕셔너리 생성
# {key: value for 항목 in 반복객체}
squares_dict = {i: i**2 for i in range(1, 6)}

# 2. 1부터 10까지의 숫자 중 짝수만 골라 제곱값 딕셔너리 생성
# {key: value for 항목 in 반복객체 if 조건}
even_squares_dict = {i: i**2 for i in range(1, 11) if i % 2 == 0}

# 3. 결과 출력
print(f"1부터 5까지의 제곱 딕셔너리: {squares_dict}")
print(f"짝수만의 제곱 딕셔너리: {even_squares_dict}")