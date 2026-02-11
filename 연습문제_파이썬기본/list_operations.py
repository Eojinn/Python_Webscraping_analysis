# 1. 두 개의 리스트 생성
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

print(f"리스트1: {list1}")
print(f"리스트2: {list2}")

# 2. 리스트를 집합(Set)으로 변환
set1 = set(list1)
set2 = set(list2)

# 3. 병합된 리스트 (합집합)
# 두 집합을 합치면서 중복된 요소(4, 5)는 하나씩만 남김
merged_list = sorted(list(set1 | set2))

# 4. 공통 요소 (교집합)
# 두 집합에 공통으로 존재하는 요소만 추출
common_elements = sorted(list(set1 & set2))

# 5. 결과 출력
print(f"병합된 리스트: {merged_list}")
print(f"공통 요소: {common_elements}")