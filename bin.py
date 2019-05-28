i=1
arr=[]
while i<=100:
	arr.append(i)
	i+=1
i=100
z=0
num=float(input("What me find:"))

while True:
	z+=1
	if num>i:
		i=i+(i/2)
	elif num<i:
		i=i/2
	else:
		print("I find number {}. Number comands:{}".format(num,z))
		break
