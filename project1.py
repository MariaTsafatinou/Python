import random
sum =0 

for i in range (1000):
	paiktes = []
	bingo = []
	for i in range (99):
		bingo.append[0]
	for i in range 	
	num1 = int(raw_input("Dwse ton 1o arithmo apo to 1 ews to 80: "))
	num2 = int(raw_input("Dwse ton 2o arithmo apo to 1 ews to 80: "))
	num3 = int(raw_input("Dwse ton 3o arithmo apo to 1 ews to 80: "))
	num4 = int(raw_input("Dwse ton 4o arithmo apo to 1 ews to 80: "))
	num5 = int(raw_input("Dwse ton 5o arithmo apo to 1 ews to 80: "))
	paiktes.append[num1, num2, num3, num4, num5]
		
		
	#a =0 #metritis 1ou bingo
	sum1 =0 #meta apo posous arithmous egine prwti fora bingo



	arithmoi = [1]
	for i in range (2,81):
		arithmoi.append(i)
	print arithmoi	
	for i in range (80):
		ar = random.randrange(len(arithmoi))
		elem = arithmoi[ar]
		del arithmoi[ar] 
		print elem
		sum1 +=1
		for i in range (99):
		if (elem in paiktes[i]) == True :		
			bingo[i] = bingo[i] + 1
			
			if bingo[i] == 5 :
				break

	print "Anaggelthikan synolika", sum1, "arithoi mexri o prwtos paikths na kanei bingo"
	sum = sum + sum1
average	= sum // 1000
print "o mesos oros twn arithmwn pou prepei na anaggelthoun gia na upar3ei bingo einai peripou",average
	
		
 
		
