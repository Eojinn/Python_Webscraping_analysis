import json

# 1. 저장할 데이터 준비 (파이썬 딕셔너리 구조)
user_data = {
    "이름": "김철수",
    "나이": 25,
    "직업": "개발자",
    "취미": ["독서", "영화감상", "코딩"],
    "주소": "서울시 강남구"
}

filename = "data.json"

# 2. JSON 파일 저장 (Serialization)
# indent=4 옵션은 가독성을 위해 들여쓰기를 추가
# ensure_ascii=False 옵션은 한글이 깨지지 않고 그대로 저장
with open(filename, "w", encoding="utf-8") as file:
    json.dump(user_data, file, indent=4, ensure_ascii=False)

print(f"데이터가 {filename}에 저장되었습니다.\n")

# 3. JSON 파일 읽기 (Deserialization)
print("JSON에서 읽어온 데이터:")
with open(filename, "r", encoding="utf-8") as file:
    loaded_data = json.load(file)
    
    # 읽어온 데이터 출력
    print(f"이름: {loaded_data['이름']}")
    print(f"나이: {loaded_data['나이']}")
    print(f"직업: {loaded_data['직업']}")
    print(f"취미: {loaded_data['취미']}")
    print(f"주소: {loaded_data['주소']}")