# 1. 쇼핑 카트 데이터를 딕셔너리로 구현 (상품명: [수량, 단가])
cart = {
    "사과": {"quantity": 2, "price": 1000},
    "바나나": {"quantity": 3, "price": 800},
    "오렌지": {"quantity": 1, "price": 1500}
}

print("쇼핑 카트:")

total_price = 0

# 2. 카트 아이템 출력 및 총 가격 계산
for item, info in cart.items():
    # 품목별 합계 = 수량 * 단가
    item_total = info["quantity"] * info["price"]
    
    # 출력 결과 형식에 맞게 출력
    print(f"{item}: {info['quantity']}개 (개당 {info['price']}원) = {item_total}원")
    
    # 전체 총 가격에 누적
    total_price += item_total

# 3. 최종 총 가격 출력
print(f"총 가격: {total_price}원")