class test():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

addrList = []

a1 = test(3,4)
print(a1)
addrList.append(a1)
print(addrList[0].num1)
