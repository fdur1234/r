#生一個隨機整數1～100(不要印出來)
#讓使用者重複輸數字去猜
#猜對的話：印出'猜對了！'
#猜錯的話要告訴他的數字比答案大／小


import random
r = random.randint(1, 100)
while True:
	num = input('請猜數字：')
	num = int(num)
	if num == r:
		print('你猜對了！')
		break 
	elif num > r:
		print('你猜得比較大，請再猜')
	elif num < r:
		print('你猜得比較小，請再猜')