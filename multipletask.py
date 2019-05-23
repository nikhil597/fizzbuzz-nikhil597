result = 0
for i in range(100):
	result = result+1
	if i % 3 == 0 and i % 5 == 0:
		print("FizzBizz")
		continue
	elif i % 3 == 0:
		print("Fizz")
		continue
	elif i % 5 == 0:
		print("Buzz")
		continue 
	print(i)
