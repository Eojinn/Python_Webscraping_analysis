# 1. 원본 문자열 정의
text = "Python is awesome programming language"

# 2. split()을 사용하여 단어별로 분리
# split()은 인자가 없으면 공백을 기준으로 문자열을 잘라 리스트로 만듦
words = text.split()

# 3. join()을 사용하여 하이픈(-)으로 연결
# "-".join(리스트)는 리스트 요소 사이에 하이픈을 넣어 하나의 문자열로 합침.
hyphen_text = "-".join(words)

# 4. 모든 단어를 대문자로 변환 후 공백으로 연결
# 리스트 컴프리헨션을 사용하여 각 단어를 대문자로 바꾼 뒤 join
upper_text = " ".join([word.upper() for word in words])

# 5. 결과 출력
print(f"원본 문자열: {text}")
print(f"분리된 단어들: {words}")
print(f"하이픈으로 연결: {hyphen_text}")
print(f"대문자로 변환 후 공백으로 연결: {upper_text}")