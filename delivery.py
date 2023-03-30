# 깡통 카테고리(부모 깡통)
class shop_info:
    def __init__(self, cate, name):
        self.cate = cate
        self.name = name

    def printB(self):
        print("%s %s" %(self.cate, self.name))


# 풀 레인지(자식 -깡통 상속받음)
class full_shop_info(shop_info):
    def __init__(self, menu):
        super.__init__()
        self.menu = ["닭", 'chicken']

    def printF(self):
        print("%s %s %s" %())


pshop = shop_info('야식', 'bbq')
pshop.printB()
