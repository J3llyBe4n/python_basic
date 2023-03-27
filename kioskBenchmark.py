import time

# 메뉴 리스트 딕셔너리
startTime = time.process.time()
menuList = {"ice cream": "1000", "coffee": "3000", "latte": "4000", "cake" : "5000"}

# 일단 메뉴 보여주기
print("################################")
print("메뉴 리스트")
print(list(menuList.keys()))

#리스트 변환
#print(list(menuList.keys())[0])

# 주문 어케 할껴?
# 주문 한 놈들 이름 갯수 리바이브 변수 생성
# 1번 음료 갯수 받기 무한 루프돌릴꺼면 리스트 갯수 만큼 지정후 for 문 돌리기

firstMenuCount = input("%s 몇개 주문하쉴? : " %list(menuList.keys())[0])
secondMenuCount = input("%s 몇개 주문하쉴? : " %list(menuList.keys())[1])

orderList = {"ice cream" : firstMenuCount, "coffee" : secondMenuCount}


#메뉴 확인 해주기
print('\n')
print("#################################")
print("주문하신 메뉴는 다음과 같다.")
print(orderList)

#총합 계산하기
totalPrice = int(menuList["ice cream"]) * int(firstMenuCount) + int(menuList["coffee"]) * int(secondMenuCount)
print('\n')
print("#################################")
print("총합은 다음과 같다")
print(totalPrice)

endTime = time.process.time()

operateTime = endTime - startTime
print(operateTime)

# 생각 해볼 점! : 오더리스트 삼중 리스트로 메뉴 세분화
# [[아아 8, [아아 : 3 뜨아 : 5]], [아크 5], [라떼 5, [뜨라 : 3, 차라 : 2]]]

# 노가다 까지말고 반복문 내일 해야하나?