# 1. 언패킹 (Unpacking)
# 튜플이나 리스트의 요소를 개별 변수로 나누어 담는다
point = (10, 20)
x, y = point
print(f"좌표: x={x}, y={y}")

numbers = [1, 2, 3]
a, b, c = numbers
print(f"리스트 언패킹: a={a}, b={b}, c={c}")

# 2. *args (가변 인자: positional arguments)
# 여러 개의 인자를 튜플 형태로 한꺼번에 받음
def sum_all(*args):
    return sum(args)

result = sum_all(10, 20, 30)
print(f"가변 인수의 합: {result}")

# 3. **kwargs (키워드 가변 인자: keyword arguments)
# 키워드와 값을 딕셔너리 형태로 한꺼번에 받음
def print_info(**kwargs):
    # kwargs는 딕셔너리이므로 items() 등을 사용할 수 있음
    info_str = ", ".join([f"{key}={value}" for key, value in kwargs.items()])
    print(f"키워드 인수들: {info_str}")

print_info(name="김철수", age=25, city="서울")