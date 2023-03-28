menuList = {"ice cream": "1000", "coffee": "3000", "latte": "4000", "cake" : "5000"}

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

@logging_time
def show_menu(menuList):
	print("#########################")
	print("메뉴 리스트")
	print(list(menuList.keys()))
	print("#########################")

@logging_time
def order_menu(menuList):
	firstMenuCount = input("%s 몇개 주문하쉴? : " % list(menuList.keys())[0])
	secondMenuCount = input("%s 몇개 주문하쉴? : " % list(menuList.keys())[1])
	orderList = {"ice cream": firstMenuCount, "coffee": secondMenuCount}
	return orderList

@logging_time
def confirm_menu(orderList):
	print('\n')
	print("#################################")
	print("주문하신 메뉴는 다음과 같다.")
	print(orderList)

@logging_time
def calculating_recipt(menuList, orderList):
	#print(orderList)

	totalPrice = int(menuList["ice cream"]) * int(orderList["ice cream"]) + int(menuList["coffee"]) * int(orderList["coffee"])
	print('\n')
	print("#################################")
	print("총합은 다음과 같다")
	print(totalPrice)

# Ex ))) orderList = list{"ice cream" : 3, "coffee" : 3}

show_menu(menuList)
orderList = order_menu(menuList)
confirm_menu(orderList)
calculating_recipt(menuList, orderList)

# 생각 해볼 점! : 오더리스트 삼중 리스트로 메뉴 세분화
# [[아아 8, [아아 : 3 뜨아 : 5]], [아크 5], [라떼 5, [뜨라 : 3, 차라 : 2]]]

# 노가다 까지말고 반복문 내일 해야하나?
# 0328 할 것 : 삼중 리스트 구현 구현 속도 테스트 메뉴 갯수 전부다 카운팅 
