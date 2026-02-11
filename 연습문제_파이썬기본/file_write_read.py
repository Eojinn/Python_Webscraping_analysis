# 1. 파일에 저장할 내용 준비
content = """안녕하세요
파이썬 파일 처리를 연습하고 있습니다
오늘은 좋은 날씨입니다"""

# 2. 파일 쓰기 ('w' 모드)
# 'w' 모드는 파일이 없으면 생성하고, 있으면 내용을 덮어씀
filename = "practice.txt"

print("파일에 저장할 내용:")
print(content)

with open(filename, "w", encoding="utf-8") as file:
    file.write(content)

print("\n" + "-"*20 + "\n")

# 3. 파일 읽기 ('r' 모드)
# 'r' 모드는 파일의 내용을 읽어옴
print("파일에서 읽어온 내용:")
with open(filename, "r", encoding="utf-8") as file:
    read_data = file.read()
    print(read_data)