# 1. 분석할 텍스트 파일 내용 생성 (연습용)
sample_text = """파이썬 프로그래밍 언어 배우기 쉬운 강력한 언어
파이썬 프로그래밍 파이썬"""

with open("test.txt", "w", encoding="utf-8") as f:
    f.write(sample_text)

# 2. 단어 빈도 계산
word_count = {}

with open("test.txt", "r", encoding="utf-8") as file:
    # 파일 전체를 읽어 공백 단위로 단어를 분리
    # split()은 줄바꿈과 여러 개의 공백을 한 번에 처리
    words = file.read().split()
    
    for word in words:
        # 딕셔너리에 단어가 있으면 1 증가, 없으면 1로 초기화
        word_count[word] = word_count.get(word, 0) + 1

# 3. 빈도순으로 내림차순 정렬 (람다 사용)
# items()를 사용해 (단어, 빈도) 튜플 리스트를 만들고 정렬
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

# 4. 결과 출력
print("단어 빈도 분석 결과:")
for word, count in sorted_words:
    print(f"{word}: {count}번")