#生一個隨機整數1～100(不要印出來)
#讓使用者重複輸數字去猜
#猜對的話：印出'猜對了！'
#猜錯的話要告訴他的數字比答案大／小


import random
x = input('請決定範圍開始值：')
y = input('請決定完結值：')
x = int(x)
y = int(y)



r = random.randint(x, y)
count = 0
while True:
	count += 1
	num = input('請猜數字：')
	num = int(num)
	if num == r:
		print('你猜對了！')
		break 
	elif num > r:
		print('你猜得比較大，請再猜')
	elif num < r:
		print('你猜得比較小，請再猜')
	print('這是你猜的第', count, '次')