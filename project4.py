latinnum= []
number= input ("Dwse enan arithmo apo to 1 ews 1000000: ")
if number < 1000000 :
	ekatxil = number / 100000
	dekxil = (number % 100000) / 10000
	xilia = ((number % 100000) % 10000 ) / 1000
	ekato = (((number % 100000) % 10000 ) % 1000 ) / 100
	dekada = (((( number % 100000) % 10000 ) % 1000 ) % 100 ) / 10
	monada = number % 10
	if ekatxil == 9 :
		 latinnum.append('-C-M')
	elif ekatxil >= 5 :
		latinnum.append('-D')
		for i in range (ekatxil - 5 ):
			latinnum.append('-C')
	elif ekatxil == 4 :
		latinnum.append('-C-D')
	else: 
		for i in range (ekatxil):
			latinnum.append ('-C')
	if dekxil == 9 :
		latinnum.append('-X-C')
	elif dekxil >= 5 :
		latinnum.append('-L')
		for i in range (dekxil - 5 ):
			latinnum.append('-X')
	elif dekxil == 4 :
		latinnum.append ('-X-L')
	else :
		for i in range (dekxil) :
			latinnum.append('-X')
	if xilia == 9 :
		latinnum.append('-I-X')
	elif xilia >= 5 :
		latinnum.append('-V')
		for i in range (xilia - 5 ):
			latinnum.append('-I')
	else :
		for i in range (xilia) :
			latinnum.append('M')
	if ekato == 9 :
		latinnum.append('CM')
	elif ekato >= 5 :
		latinnum.append('D')
		for i in range (ekato - 5):
			latinnum.append('C')
	elif ekato == 4 :
		latinnum.append('CD')
	else :
		for i in range (ekato):
			latinnum.append('C')
	if dekada == 9:
		latinnum.append('XC')
	elif dekada >= 5:
		latinnum.append('L')
		for i in range (dekada - 5) :
			latinnum.append('X')
		
	elif dekada == 4 :
		latinnum.append('XL')
	else :
		for i in range (dekada ):
			latinnum.append('X')
	if monada == 9 :
		latinnum.append('IX')
	elif monada >= 5 :
		latinnum.append('V')
		for i in range (monada - 5 ):
			latinnum.append('I')
	elif monada == 4 :
		latinnum.append('IV')
	else :
		for i in range ( monada ):
			latinnum.append ('I')
elif number == 1000000 :
	latinnum.append('-M')
latinnumber = ''.join(latinnum)	
print "O arithmos", number, "sta latinika grafetai: ", latinnumber