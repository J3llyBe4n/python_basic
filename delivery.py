# 깡통 카테고리(부모 깡통)
class shop_info:
    def __init__(self, cate, name):
        self.cate = cate
        self.name = name

# 풀 레인지(자식 -깡통 상속받음)
class full_shop_info(shop_info):
    def __init__(self,cate,name):
        super().__init__(cate, name)

    def insert(self):
        tempName = input("insert name : ")
        try:
            if(self.name == tempName):
                print("수정할꼐 없는뎁쇼?")
            else:
                self.name = tempName
        except:
            self.name = tempName


    def printF(self):
      #  print("%s" %(shop_info.cate))
        #print("%s" %self.menu)
        print("%s" %self.name)
        print("%s" %self.cate)

Fshop = full_shop_info("야식", "bbq")
Fshop.insert()
Fshop.printF()
#how to upstream data
