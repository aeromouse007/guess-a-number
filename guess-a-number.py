import random
r = random.randint(1,100)
while True:
	num = input('give a number:')
	num = int(num)
	if num == r:
		print('賓果')
		break
	if num > r:
		print('比較大')
	else:
		print('比較小')