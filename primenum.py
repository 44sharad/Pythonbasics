num = int(input("Enter the number:\n"))
for x in range(2,num):
	if num%x == 0:
		print("The number {} is not prime\n".format(num))
		break
else:
	print("The number {} is prime\n".format(num))
		
