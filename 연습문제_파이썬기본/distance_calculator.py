import math

# 1. 좌표를 튜플로 저장
point1 = (0, 0)
point2 = (3, 4)

# 2. 좌표 정보 출력
print(f"점1: {point1}")
print(f"점2: {point2}")

# 3. 두 점 사이의 거리 계산
# 공식: 루트((x2 - x1)^2 + (y2 - y1)^2)
distance = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# 4. 결과 출력
print(f"두 점 사이의 거리: {distance}")