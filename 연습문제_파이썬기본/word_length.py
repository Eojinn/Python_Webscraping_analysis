# 1. 단어 목록 리스트 생성
words = ['cat', 'elephant', 'dog', 'butterfly', 'ant']

# 2. 단어 목록 출력
print(f"단어 목록: {words}")

# 3. 가장 긴 단어 찾기
# max 함수의 key 인자에 len을 지정하면 글자 수가 가장 많은 요소를 찾습니다.
longest_word = max(words, key=len)

# 4. 가장 짧은 단어 찾기
# min 함수의 key 인자에 len을 지정하면 글자 수가 가장 적은 요소를 찾습니다.
shortest_word = min(words, key=len)

# 5. 결과 출력
print(f"가장 긴 단어: {longest_word} ({len(longest_word)}글자)")
print(f"가장 짧은 단어: {shortest_word} ({len(shortest_word)}글자)")