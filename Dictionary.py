def negfive():
	msg = " down by at least 5 pts \U0001F610"
	return msg
def negten():
	msg = "down by at least 10 pts \U0001F610"	
	return msg
def negtwenty():
	msg = " down by at least 20 pts \U0001F62D"
	return msg
def upfive():
	msg = " up by at least 5 pts \U0001F44C"	
	return msg
def upten():
	msg = " up by at least 10 pts \U0001F919"
	return msg
def uptwenty():
	msg = " up by at least 20 pts \U0001F600"
	return msg
def close():
	msg = " +/- 4 pts, it's close \U0001F525"						
	return msg
def even():
	msg = "Tie Game!!! \U0001F525 \U0001F525 \U0001F525"
	return msg
Number = {
	'-1' : close,
	'-2' : close,
	'-3' : close,
	'-4' : close,						
	'-5' : negfive,
	'-6' : negfive,
	'-7' : negfive,
	'-8' : negfive,
	'-9' : negfive,
	'-10' : negten,
	'-11' : negten,
	'-12' : negten,
	'-13' : negten,
	'-14' : negten,
	'-15' : negten,
	'-16' : negten,
	'-17' : negten,
	'-18' : negten,
	'-19' : negten,
	'-20' : negtwenty,
	'-21' : negtwenty,
	'-22' : negtwenty,
	'-23' : negtwenty,
	'-24' : negtwenty,
	'-25' : negtwenty,
	'-26' : negtwenty,
	'-27' : negtwenty,
	'-28' : negtwenty,
	'-29' : negtwenty,
	'-30' : negtwenty,
	'0' : even,
	'1' : close,
	'2' : close,
	'3' : close,
	'4' : close,
	'5' : upfive,
	'6' : upfive,
	'7' : upfive,
	'8' : upfive,
	'9' : upfive,
	'10' : upten,
	'11' : upten,
	'12' : upten,
	'13' : upten,
	'14' : upten,
	'15' : upten,
	'16' : upten,
	'17' : upten,
	'18' : upten,
	'19' : upten,
	'20' : uptwenty,
	'21' : uptwenty,
	'22' : uptwenty,
	'23' : uptwenty,
	'24' : uptwenty,
	'25' : uptwenty,
	'26' : uptwenty,
	'27' : uptwenty,
	'28' : uptwenty,
	'29' : uptwenty,
	'30' : uptwenty
}
