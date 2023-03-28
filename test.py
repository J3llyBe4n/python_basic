'''
x = int(input("insert score"))

if (x > 89):
    print("score : %s, grade A" %x)
elif (80 < x <90):
    print("score : %s, grade B" %x)
elif (70 < x <80):
    print("score : %s, grade C" %x)
else:
    print("score : %s, grade D" %x)
'''
import random

lottery_number = []

for i in range (6):
    lottery_number.append(random.randint(1,45))

print(lottery_number)