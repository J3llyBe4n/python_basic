import time
startTime = time.process_time()

class Osk():
    def __init__(self, name, drinkmenu, cakemenu, temper, size, order_l={}):
        self.name = name
        self.drinkmenu = drinkmenu
        self.drinkmenu_k = list(drinkmenu.keys())
        self.drinkmenu_v = list(drinkmenu.values())
        self.cakemenu = cakemenu
        self.cakemenu_k = list(cakemenu.keys())
        self.cakemenu_v = list(cakemenu.values())
        self.temper = temper
        self.temper_k = list(size.keys())
        self.temper_v = list(size.values())
        self.size = size
        self.size_k = list(size.keys())
        self.size_v = list(size.values())
        self.order_l = order_l
        self.order_n = list(order_l.keys()) # 주문 이름
        self.order_p = list(order_l.values()) # 가격
        self.order_v = [] # 수량
        self.Option1 = [] # 온도
        self.Tp = [] # 온도 요금
        self.Option2 = [] # 사이즈
        self.Sp = [] # 사이즈 요금
        self.total = 0 # 가격 총합
        self.value_1 = 0 # 수량 총합
        self.A = ["y", "n", "Y", "N"]
    # 음료 선택 함수
    def drinkorder(self):
        while True:
            for i in range(len(self.drinkmenu_k)):
                print(f"{i+1}. {self.drinkmenu_k[i]}        {self.drinkmenu_v[i]}")
            a1 = input("원하시는 메뉴의 번호를 눌러주세요.")
            a1 = int(a1)
            try:
                if a1<1 or a1>len(self.drinkmenu_k):
                    raise ValueError
            except ValueError:
                print("잘못된 입력입니다. 다시 입력해주세요.")
                continue
            self.order_n.append(self.drinkmenu_k[a1-1])
            break
        while True:
            for i in range(len(self.temper_k)):
                print(f"{i+1}. {self.temper_k[i]}        {self.temper_v[i]}")
            a2 = input("원하시는 옵션의 번호를 눌러주세요.")
            a2 = int(a2)
            try:
                if a2<1 or a2>len(self.temper_k):
                    raise ValueError
            except ValueError:
                print("잘못된 입력입니다. 다시 입력해주세요.")
                continue
            self.Option1.append(self.temper_k[a2-1])
            self.Tp.append(self.temper_v[a2-1])
            break
        while True:
            for i in range(len(self.size_k)):
                print(f"{i+1}. {self.size_k[i]}        {self.size_v[i]}")
            a3 = input("원하시는 옵션의 번호를 눌러주세요.")
            a3 = int(a3)
            try:
                if a3<1 or a3>len(self.size_k):
                    raise ValueError
            except ValueError:
                print("잘못된 입력입니다. 다시 입력해주세요.")
                continue
            self.Option2.append(self.size_k[a2-1])
            self.Sp.append(self.size_v[a2-1])
            break
        while True:
            a4 = input("원하시는 수량을 입력해주세요.")
            a4 = int(a4)
            try:
                if a4 <1:
                    raise ValueError
            except ValueError:
                print("잘못된 입력입니다. 다시 입력해주세요.")
                continue
            self.order_v.append(a4)
            self.order_p.append((int(self.drinkmenu_v[a1-1])+int(self.temper_v[a2-1])+int(self.size_v[a2-1]))*a4)
            self.value_1 += a4
            self.total += (int(self.drinkmenu_v[a1-1])+int(self.temper_v[a2-1])+int(self.size_v[a2-1]))*a4
            break
    # 케이크 선택 함수
    def cakeorder(self):
        while True:
            for i in range(len(self.cakemenu_k)):
                print(f"{i+1}. {self.cakemenu_k[i]}        {self.cakemenu_v[i]}")
            a1 = input("원하시는 메뉴의 번호를 눌러주세요.")
            a1 = int(a1)
            try:
                if a1<1 or a1>len(self.cakemenu_k):
                    raise ValueError
            except ValueError:
                print("잘못된 입력입니다. 다시 입력해주세요.")
                continue
            self.order_n.append(self.cakemenu_k[a1-1])
            break
        while True:
            a2 = input("원하시는 수량을 입력해주세요.")
            a2 = int(a2)
            try:
                if a2 <1:
                    raise ValueError
            except ValueError:
                print("잘못된 입력입니다. 다시 입력해주세요.")
                continue
            self.order_v.append(a2)
            self.order_p.append(int(self.cakemenu_v[a1-1])*a2)
            self.Option1.append("-")
            self.Option2.append("-")
            self.value_1 += a2
            self.total += int(self.cakemenu_v[a1-1])*a2
            break
    # 주문 취소 함수
    def cancel(self):
        while True:
            cancel = input("주문을 취소하시겠습니까? [ y / n ]")
            if cancel == "y":
                c_1 = input("취소하실 메뉴의 번호를 눌러주세요.\n 취소하실 메뉴가 없다면 q를 눌러주세요.")
                if c_1 == "q":break
                try:
                    c_1 = int(c_1)
                    if c_1 < 1 or c_1 >len(self.order_n):
                        raise ValueError
                except ValueError:
                    print("잘못된 입력입니다. 다시 입력해주세요")
                    continue
                name = self.order_n[int(c_1)-1]
                price_1 = self.order_p[int(c_1)-1]
                value = self.order_v[int(c_1)-1]
                self.order_n.remove(name)
                self.value_1 = self.value_1 - int(value)
                self.total = self.total - price_1
                print("주문이 취소되었습니다.")
                print("""
   주문품목                    수량           가격""")
                for i in range(len(self.order_n)):
                    print(f"""
{i+1}. {self.order_n[i]}({self.Option2[i]}, {self.Option1[i]})      {self.order_v[i]}             {self.order_p[i]}
    """)
                print(f"""========================================================
     합계                       {self.value_1}             {self.total}
""")
                continue
            try:
                if cancel != "y" and cancel != "n":
                    raise ValueError
            except ValueError:
                print("잘못된 입력입니다. 다시 입력해주세요")
                continue
            else:
                print("""
   주문품목                    수량           가격""")
                for i in range(len(self.order_n)):
                    print(f"""
{i+1}. {self.order_n[i]}({self.Option2[i]}, {self.Option1[i]})      {self.order_v[i]}             {self.order_p[i]}
    """)
                print(f"""========================================================
     합계                       {self.value_1}             {self.total}
""")
                break
    # 결제 함수
    def pay(self):
        while True:
            if int(self.total) == 0:
                print("이용해주셔서 감사합니다.")
                break
            else:
                check = input(f"\n\n총 {self.total}원을 결제합니다. \n결제수단을 선택해주세요 [ 1. 카드 / 2. 현금 ]")
                check = int(check)
                if check == 1:
                    print("\nIC카드가 윗면에 가도록 카드를 넣어주세요\n")
                    point = input("포인트를 적립하시겠습니까? [ y / n ]")
                    if point == "y":
                        num = input("포인트 적립번호 4자리를 입력해주세요.")
                        print(f"\n{num}번호로 포인트가 {int(self.total/100)}만큼 적립되었습니다.")
                        print("\n결제가 완료되었습니다. 카드를 제거해주세요.\n")
                        print("이용해주셔서 감사합니다.")
                        break
                    try:
                        if point != "n" and point != "y":
                            raise ValueError
                    except ValueError:
                        print("잘못된 입력입니다. 다시 입력해주세요.")
                        continue
                    else:
                        print("\n결제가 완료되었습니다. 카드를 제거해주세요.\n")
                        print("이용해주셔서 감사합니다.")
                        break
                else:
                    money = input(f"\n\n총 {self.total}원을 결제합니다. 결제 금액을 넣어주세요.")
                try:
                    money = int(money)
                    if money < self.total:
                        raise ValueError
                except ValueError:
                    print("금액이 모자랍니다.")
                    continue
            change = money - self.total
            print("\n")
            print(f"거스름돈은 {change}원입니다. \n이용해주셔서 감사합니다!")
            break
    # 주문 내역
    def orders(self):
        print("         제품 목록                  수량                  가격          ")
        for i in range(len(self.order_n)):
            print(f"""    {i+1} {self.order_n[i]}({self.Option2[i]}) {self.Option1[i]}              {self.order_v[i]}                  {self.order_p[i]}""")
    # 추가주문 루프
    def loof(self):
        while True:
            fix = input("추가 주문하시겠습니까? [ y / n ]")
            try:
                if fix not in A:
                    raise ValueError
            except ValueError:
                print("잘못된 접근입니다.")
                continue
            break
C = {'휘낭시에    ':6000, "치즈 케이크 ":6000, "초코 케이크 ":7000,
        "생크림케이크":8000, "티라미수    ":8000, "생과일케이크":9000}
D = {"  아메리카노   ":3000, "  바닐라 라떼  ":4000, "  망고바나나   ":5000,
    "  에스프레소   ":5000, "카라멜 마끼아또":5500, "   딸기라떼    ":6000,
    "자몽허니블랙티 ":6400, " 제주유기녹차  ":7000, "    밀크티     ": 7000}
S = {"S":0, "M":200, "L":400}
T = {"Hot":0, "Ice":200}
A = ["y", "n", "Y", "N"]
star = Osk("스타벅스", D,C,T,S,{})
print(f"{star.name}에 오신것을 환영합니다.")
press_any_button = input("아무 곳이나 누르세요")
while True:
    print("""
    1. 음료
    2. 케익
    """)
    menubutton = input("원하시는 메뉴를 누르세요. 종료하려면 q를 누르세요")
    if menubutton == "q":
        break
    elif menubutton == "1":
        star.drinkorder()
        star.orders()
        while True:
            fix = input("추가 주문하시겠습니까? [ y / n ]")
            try:
                if fix not in A:
                    raise ValueError
            except ValueError:
                print("잘못된 접근입니다.")
                continue
            break
        if fix == "n":
            break
        else:
            continue
    elif menubutton == "2":
        star.cakeorder()
        star.orders()
        while True:
            fix = input("추가 주문하시겠습니까? [ y / n ]")
            try:
                if fix not in A:
                    raise ValueError
            except ValueError:
                print("잘못된 접근입니다.")
                continue
            break
        if fix == "n":
            break
        else:
            continue
    else:
        print("다른 버튼을 눌러주세요")
        continue
star.cancel()
star.pay()

endTime = time.process_time()
print("-----------------------------")
print("-----------------------------")
print("-----------------------------")
print()