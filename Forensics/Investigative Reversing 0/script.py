with open('mystery.png','rb') as file:
	corrupt_flag=bytearray(file.read())[-26:]
	flag=""
	for i in range(len(corrupt_flag)):
	    if 5<i<=15:
		if i ==15:
		    flag+=chr(corrupt_flag[i]+3)
		else:
		    flag+=chr(corrupt_flag[i]-5)
	    else:
		flag+=chr(corrupt_flag[i])
	print(flag)

