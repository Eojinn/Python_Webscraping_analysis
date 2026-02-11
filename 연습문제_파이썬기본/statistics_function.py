import math

def calculate_statistics(numbers):
    # 1. 리스트가 비어있는지 확인 (에러 방지)
    if not numbers:
        return None

    # 2. 기초 통계량 계산
    total = sum(numbers)
    count = len(numbers)
    mean = total / count  # 평균
    
    maximum = max(numbers) # 최댓값
    minimum = min(numbers) # 최솟값
    
    # 3. 표준편차(Standard Deviation) 계산
    # 편차 제곱의 평균에 루트를 씌움
    variance = sum((x - mean) ** 2 for x in numbers) / count
    std_dev = math.sqrt(variance)
    
    return mean, maximum, minimum, std_dev

# 데이터 준비
data = [10, 20, 30, 40, 50]

# 함수 호출 및 결과 언패킹
avg, high, low, sd = calculate_statistics(data)

# 결과 출력
print(f"숫자들: {data}")
print(f"평균: {avg:.1f}")
print(f"최댓값: {high}")
print(f"최솟값: {low}")
print(f"표준편차: {sd:.2f}")