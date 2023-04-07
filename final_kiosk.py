# 메뉴 정보에 대한 클래스
class menuInfo(object):
    def __init__(self, menuCategory, menuName, menuPrice):
        self.menuCategory = menuCategory
        self.menuPrice = menuPrice
        self.menuName = menuName

# 메뉴주문에 대한 클래스 (들어갈 정보) 1. 메뉴이름 2.메뉴 갯수 해당 구조체에서 바로 계산 까지 가능
class orderInfo(object):

    def __init__(self,orderMenuName, orderMenuCount):
        self.orderMenuName = orderMenuName
        self.orderMenuCount = orderMenuCount


#성능 테스트
def logging_time(original_fn):
    import time
    from functools import wraps
    @wraps(original_fn)
    def wrapper(*args, **kwargs):
        start_time = time.process_time()
        result = original_fn(*args, **kwargs)

        end_time = time.process_time()
        print("WorkingTime[{}]: {} sec".format(original_fn.__name__, end_time - start_time))
        return result
    return wrapper


#모드 선택자 받아서 필터링 후 해당 모드 인도 _ 시작
@logging_time
def filteringMode():

    while True:
        print("1. 관리자 2. 사용자")
        chooseMode = input("모드를 누르세요 : ")
        #어드민 모드
        if chooseMode == "1":
            adminModeList()

        #사용자 모드
        elif chooseMode == "2":
            customerModeList()
            break

        #예외처리
        else:
            print("잘못 눌럿다.")

#관리자 모드 메뉴 보여주기
def adminModeList():
     while True:
            print("원하는 번호를 눌러라\n 1.메뉴 추가\n 2.메뉴 수정\n 3.메뉴 삭제\n q.상위 메뉴 올라가기")
            chooseAdminMode = input("모드 눌러라 : ")

            if chooseAdminMode == "1":
                adminCreateMenu()

            elif chooseAdminMode == "2":
                print("메뉴 수정")
                return

            elif chooseAdminMode == "3":
                print("메뉴삭제")

            elif chooseAdminMode == "q":
                print("상위 메뉴로 돌아가기")
                filteringMode()

            else:
                print("잘못 눌럿다잉")

# 사용자 모드 메뉴 보여주기
def customerModeList():
    while True:
        print("원하는 번호를 눌러라\n 1.메뉴 보기\n 2.메뉴 주문\n q.상위 메뉴 올라가기")
        chooseCustomerMode = input("모드 눌러라 : ")

        if chooseCustomerMode == "1":
            # 메뉴 보기
            showMenu()

        elif chooseCustomerMode == "2":
            # 메뉴 주문
            orderMenu()
            break

        elif chooseCustomerMode == "q":
            filteringMode()
        else:
            print("잘못 눌럿다.")

# 관리자 모드 메뉴 생성 by class
def adminCreateMenu():
    #클래스 생성해주기
    print("제품 카테고리 목록")
    print("1. 음료 2. 빵 3. 기타")
    menuCategory = input("메뉴 카테고리를 눌러라 : ")
    menuName = input("제품 이름 : ")
    menuPrice = input("제품 가격 : ")

    #임시 메뉴 클래스 생성
    tempMenuClass = menuInfo(menuCategory, menuName, menuPrice)

    #클래스 주소 적재
    storeMenu(tempMenuClass, menuList)
    print("메뉴 추가 완료")
    filteringMode()

# 메뉴 클래스 addr menuList에 인덱싱 저장
def storeMenu(tempMenuClass, menuList):
    menuList.append(tempMenuClass)

# 메뉴 리스트 쭉 보여주기
def showMenu():
    print("1.음료  2.빵  3.기타   q.상위메뉴로 가기")
    print("-----------------------------------")
    tempPickCategory = input("메뉴 카테고리를 선택하라")

    if (tempPickCategory == "q"):
        customerModeList()
    showCategory(tempPickCategory)

#메뉴 카테고리 보여주기
def showCategory(tempPickCategory):

    while True:
        #음료 카테고리 다 보여주기
        if(tempPickCategory == "1"):
            for i in range(len(menuList)):
                if (menuList[i].menuCategory) == "1":
                    print("----------------------------")
                    print("메뉴 이름 : %s" %menuList[i].menuName)
                    print("메뉴 가격 : %s" %menuList[i].menuPrice)
                    print("-----------------------------")
            showMenu()

        #빵 카테고리 다 보여주기
        elif(tempPickCategory == "2"):
            for i in range(len(menuList)):
                if (menuList[i].menuCategory) == "2":
                    print("----------------------------")
                    print("메뉴 이름 : %s" %menuList[i].menuName)
                    print("메뉴 가격 : %s" %menuList[i].menuPrice)
                    print("-----------------------------")
            showMenu()

        #기타 카테고리 다 보여주기
        elif(tempPickCategory== "3"):
            for i in range(len(menuList)):
                if (menuList[i].menuCategory) == "3":
                    print("----------------------------")
                    print("메뉴 이름 : %s" % menuList[i].menuName)
                    print("메뉴 가격 : %s" % menuList[i].menuPrice)
                    print("-----------------------------")
            showMenu()

        #상위 메뉴로 날라가기
        elif(tempPickCategory == "q"):
            showMenu()

        #예외처리
        else:
            print("잘못 눌럿다.")

#메뉴 주문하기
def orderMenu():
        tempOrderMenuName = input("주문할 메뉴를 입력하세요\n 주문을 다했으면 q 눌러라 : ")
        if (tempOrderMenuName == "q"):
            confirmOrder()
        else:
            tempOrderMenuCount = input("%s를 주문 합니다. 몇개를 주문할래?" %tempOrderMenuName)

            tempOrderClass = orderInfo(tempOrderMenuName, tempOrderMenuCount)
            storeMenu(tempOrderClass, orderList)
            orderMenu()

#오더 메뉴를 받아 임시 클래스에 저장 후 orderList에 인덱싱으로 저장
def storeMenu(tempOrderClass, orderList):
    orderList.append(tempOrderClass)

#주문 메뉴 확인 후 빌지 발행
def confirmOrder():
    i = 0

    print("--------------------------")
    print("주문서")
    print("--------------------------")

    temptotalPrice = []
    for i in range(len(orderList)):
        print("주문 메뉴 이름 : %s" %orderList[i].orderMenuName)
        print("주문 메뉴 수량 : %s" %orderList[i].orderMenuCount)
    #   print("해당 품목 총액 : %d",'''menuinfo의 이름과 ordermenu이름이 같을때, menuinfo에서 price를 빼서 오더메뉴카운트와 곱계산''')
        columnPrice = 0
        for j in range(len(menuList)):
            tempName = menuList[j].menuName
            if (tempName == orderList[i].orderMenuName):
                tempProductPrice = menuList[j].menuPrice
                print("해당 품목 가격 : %d" %int(tempProductPrice))

                #tempProductPrice 자료형 확인
                #print(type(tempProductPrice))

                #tempProductPrice 자료형인 str 을 int 로 바꾸기 오더리스트 갯수도 int로 형변환
                convertPrice = int(tempProductPrice)
                convertCount = int(orderList[i].orderMenuCount)


                #해당 품목 토탈 계산 돌려보기
                totalPrice = convertPrice * convertCount

                #리스트에 박아넣기
                temptotalPrice.append(int(totalPrice))


    print("---------------------------")
    calculateTotal(temptotalPrice)

#최종 빌지 빼주기
def calculateTotal(tempTotalPrice):
    totalFee =0
    for i in range(len(tempTotalPrice)):
        totalFee += tempTotalPrice[i]

    print("----------------------------")
    print("총 계산 비용 : %4d" %totalFee)
    return




#메뉴 클래스의 addr이 적재되어지는 list
menuList = []

#주문 내역 class addr.이 적재될 중요 장소
orderList =[]

#DB_넣기 귀찮을때 DB빌드 하는거
menu_1 = menuInfo('1','aa','1000')
menuList.append(menu_1)
menu_2 = menuInfo('2','bb', '2000')
menuList.append(menu_2)

#소스 시작하는 함수
filteringMode()



