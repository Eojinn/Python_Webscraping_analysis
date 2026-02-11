# 1. 사용자로부터 상품 가격과 할인율 입력 받기
price = int(input("상품 가격을 입력하세요: "))
discount_rate = int(input("할인율을 입력하세요(%): "))

# 2. 할인 금액 및 최종 가격 계산
# 할인 금액 = 원래 가격 * (할인율 / 100)
discount_amount = int(price * (discount_rate / 100))
# 최종 가격 = 원래 가격 - 할인 금액
final_price = price - discount_amount

# 3. 결과 출력
print(f"원래 가격: {price}원")
print(f"할인율: {discount_rate}%")
print(f"할인 금액: {discount_amount}원")
print(f"최종 가격: {final_price}원")