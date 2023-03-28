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
	order = {}
	for i in range(len(menuList)):
		tempList =list(menuList.keys())
		orderCount = input("%s 몇개 주문하실? : " %tempList[i])
		order['{}'.format(tempList[i])] = orderCount

	return order

@logging_time
def confirm_menu(orderList):
	print('\n')
	print("#################################")
	print("주문하신 메뉴는 다음과 같다.")
	print(orderList)
@logging_time
def calculating_recipt(menuList, orderList):
	totalPrice = 0
	tempKeyList = list(menuList.keys())
	tempValueList = list(menuList.values())

	# orderList = {'ice cream': '3', 'coffee': '4', 'latte': '5', 'cake': '6'}

	for i in range(len(orderList)):

		#print(type(int(orderList["{}".format(tempKeyList[i])]))) = 메뉴 갯수 입력값
		#print(type(int((tempValueList[i])))) = 메뉴 가격표

		totalPrice += (int(orderList["{}".format(tempKeyList[i])])) * int((tempValueList[i]))

	print("##########################")
	print("총 가격은 %d 임." %totalPrice)
# Ex ))) orderList = list{"ice cream" : 3, "coffee" : 3}

show_menu(menuList)
orderList = order_menu(menuList)
confirm_menu(orderList)
calculating_recipt(menuList, orderList)

# 생각 해볼 점! : 오더리스트 삼중 리스트로 메뉴 세분화
# [[아아 8, [아아 : 3 뜨아 : 5]], [아크 5], [라떼 5, [뜨라 : 3, 차라 : 2]]]

# 노가다 까지말고 반복문 내일 해야하나?
# 0328 할 것 : 삼중 리스트 구현 구현 속도 테스트 메뉴 갯수 전부다 카운팅 
