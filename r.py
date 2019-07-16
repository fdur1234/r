#生一個隨機整數1～100(不要印出來)
#讓使用者重複輸數字去猜
#猜對的話：印出'猜對了！'
#猜錯的話要告訴他的數字比答案大／小


import random
r = random.randint(1, 100)

while True:
	num = input('請輸入數字：')
	num = int(num)
