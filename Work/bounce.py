# bounce.py
#
# Exercise 1.5

#Initial parameters
height = 100
bounce = 0

while bounce < 10:
	height = height * 0.6
	bounce = bounce + 1
	print(bounce, round(height,	4))

print('Bounces taken:', bounce)
