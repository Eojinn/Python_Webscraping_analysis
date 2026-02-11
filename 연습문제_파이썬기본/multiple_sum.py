# 1. 3의 배수를 담을 빈 리스트 생성
multiples_of_3 = []

# 2. 1부터 100까지 반복하며 3의 배수 찾기
for i in range(1, 101):
    # i를 3으로 나눈 나머지가 0이면 3의 배수입니다.
    if i % 3 == 0:
        multiples_of_3.append(i)

# 3. 합계와 개수 계산
total_sum = sum(multiples_of_3)
count = len(multiples_of_3)

# 4. 결과 출력
print(f"1부터 100까지 3의 배수: {multiples_of_3}")
print(f"3의 배수의 합: {total_sum}")
print(f"3의 배수의 개수: {count}개")