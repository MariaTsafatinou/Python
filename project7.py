day = str(raw_input("Dwse thn shmerini hmera ths evdomadas: "))
date = int(raw_input("Dwse thn shmerini hmerominia: "))
month = int(raw_input("Dwse ton trexwn mhna: "))
year = int(raw_input("Dwse tin twrini xronologia: "))

if ((year % 4) == 0) and ((year % 100) != 0) :
	if (month == 1 or month == 2) :
		year2 = year + 5
		print "Mesa sta epomena 10 xronia mono to", year2 ,"tha exoume thn hmerominia", day , date,"/",month,"/",year2 ,"opou h hmera o mhnas kai h hmerominia antistoixoun me th shmerinh"
		
	else :	
		year2 = year +6
		print "Mesa sta epomena 10 xronia mono to", year2 ,"tha exoume thn hmerominia", day , date,"/",month,"/",year2 ,"opou h hmera o mhnas kai h hmerominia antistoixoun me th shmerinh"
		
elif (((year - 1) % 4) == 0) and (((year - 1) % 100) != 0) :		
	year2 = year + 6
	print "Mesa sta epomena 10 xronia mono to", year2 ,"tha exoume thn hmerominia", day , date,"/",month,"/",year2 ,"opou h hmera o mhnas kai h hmerominia antistoixoun me th shmerinh"
	
elif (((year - 2) % 4) == 0) and (((year - 2) % 100) != 0) : 	
	if (month == 1 or month == 2) :
		year2 = year + 6
		print "Mesa sta epomena 10 xronia mono to", year2 ,"tha exoume thn hmerominia", day , date,"/",month,"/",year2 ,"opou h hmera o mhnas kai h hmerominia antistoixoun me th shmerinh"
		
	else :	
		print "Mesa sta epomena 10 xronia den yparxei etos opou h hmera o mhnas kai h hmerominia antistoixoun me th shmerinh"
		
elif (((year + 1) % 4) == 0) and (((year + 1) % 100) != 0) :
	if (month == 1 or month == 2) :
		print "Mesa sta epomena 10 xronia den yparxei etos opou h hmera o mhnas kai h hmerominia antistoixoun me th shmerinh"
		
	else :	
		year2 = year + 5
		print "Mesa sta epomena 10 xronia mono to", year2 ,"tha exoume thn hmerominia", day , date,"/",month,"/",year2 ,"opou h hmera o mhnas kai h hmerominia antistoixoun me th shmerinh"
				