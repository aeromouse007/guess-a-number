import random
start = input('決定開始值:')
end = input('決定結束值:')
start = int(start)
end = int(end)
r = random.randint(start,end)
count = 0
while True:
	count += 1
	num = input('give a number:')
	num = int(num)
	if num == r:
		print('賓果')
		print('這是你猜的第', count,'次')
		break
	if num > r:
		print('比較大')
	else:
		print('比較小')
	print('這是你猜的第', count,'次')