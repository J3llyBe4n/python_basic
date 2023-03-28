# 메뉴 정보에 대한 클래스
class menuInfo(object):

    def __init__(self, menuCategory, menuName, menuPrice):
        self.menuCategory = menuCategory
        self.menuPrice = menuPrice
        self.menuName = menuName

# 메뉴주문에 대한 클래스 (들어갈 정보) 1. 메뉴이름 2.메뉴 갯수 해당 구체에서 바로 계산 까지 가능

# 메뉴주문에 대한 클래스 메뉴 정보 클래스를 참조에 추가로 갯수 카운트 하는 변수만 추가하여 클래스 주소를 리스트로 반환 후 계산할때는 해당 구조체 참조

#모드 선택자 받아서 필터링 후 해당 모드 인도
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
            print("메뉴 주문")
            return

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

# 메뉴 클래스 addr menuList에 인덱싱 저장.
def storeMenu(tempMenuClass, menuList):
    menuList.append(tempMenuClass)

# 메뉴 리스트 쭉 보여주기
def showMenu():
    print("1.음료  2.빵  3.기타   q.상위메뉴로 가기")
    print("-----------------------------------")
    tempPickCategory = input("메뉴 카테고리를 선택하라")
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




#메뉴의 class addr.이 적재될 중요 장소
menuList = []

filteringMode()



