# 1. 사용자로부터 문장 입력 받기
sentence = input("문장을 입력하세요: ")

# 2. 단어 단위로 쪼개기
# split()은 인자를 넣지 않으면 연속된 모든 공백(Space, Tab 등)을 하나로 처리하여 
# 실제 단어들만 리스트로 만들어줍니다.
word_list = sentence.split()

# 3. 공백 제거 및 단어 재결합
# " ".join()은 리스트에 담긴 단어들 사이에 공백을 하나씩 넣어 하나의 문자열로 합칩니다.
clean_sentence = " ".join(word_list)

# 4. 단어 개수 세기
word_count = len(word_list)

# 5. 결과 출력
print(f"공백 제거: {clean_sentence}")
print(f"단어 개수: {word_count}개")