class Point:
    def __init__(self):
        self.point = 1000

    def orderOpt(self):

        orderDef = input("insert option : ")
        if orderDef == "takeout":
            print("포장을 선택하셨습니다")
            self.point_give()
        else:
            print("here")

    def point_give(self):
        print(f"포장 주문시 {self.point}원이 적립 됩니다.")


order = Point()
order.orderOpt()