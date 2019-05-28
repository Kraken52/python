def verde(max,min):
	while(max!=min):
		if(max>min):
			max=max-min
		else:
			min=min-max
	print(max)
x=int(input("max:"))
y=int(input("min:"))
print("X:{0};Y:{1}".format(x,y))
verde(x,y)
