# 1. 중복된 요소가 포함된 원본 리스트 생성
original_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(f"원본 리스트: {original_list}")

# 2. 중복 제거
# set() 함수는 리스트를 집합으로 변환하며 중복을 자동으로 제거
unique_set = set(original_list)

# 3. 리스트로 다시 변환 및 정렬
# sorted() 함수는 데이터를 오름차순으로 정렬한 새로운 리스트를 반환
result_list = sorted(list(unique_set))

# 4. 결과 출력
print(f"중복 제거 후: {result_list}")