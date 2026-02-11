import os
import sys

# 1. 현재 작업 디렉토리 및 파이썬 정보
cwd = os.getcwd()
print(f"현재 작업 디렉토리: {cwd}")
print(f"Python 버전: {sys.version}")

# 2. 운영체제 및 환경 변수
# os.name은 'posix'(리눅스/맥) 또는 'nt'(윈도우)를 반환
print(f"운영체제: {os.name}")

# PATH 환경 변수 중 앞부분 일부만 출력
path_env = os.environ.get("PATH", "")
print(f"환경 변수 PATH 일부: {path_env[:50]}...")

# 3. 파일 경로 다루기
# 실제 경로가 아니더라도 문자열 기반으로 경로를 분해하고 결합할 수 있음
full_path = "/Users/username/documents/report.txt"

# 경로에서 디렉토리와 파일명 분리
directory = os.path.dirname(full_path)
filename = os.path.basename(full_path)
# 파일명과 확장자 분리
name_only, extension = os.path.splitext(filename)

print("파일 경로 정보:")
print(f"- 디렉토리: {directory}")
print(f"- 파일명: {filename}")
print(f"- 확장자: {extension}")

# 4. 파일 존재 여부 확인
exists = os.path.exists(full_path)
print(f"파일 존재 여부: {exists}")