# Vefify check for name of issuer there are many issuer which are not listed below
def verify(p,q,r,s):
	if(p==5):
		if(q==1 or q==2 or q==3 or q==4 or q==5):
			print "Mastercard"
		elif(q==0 or q==6 or q==7 or q==8):
			print "Maestro"
	elif(p==4):
		print "Visa"
	elif(p==6):
		if(q==0 or (q==5 and r==2 and s==1)):
			print "RuPay"
	elif(p==3):
		if(q==4 or q==7):
			print "American Express"
# only valid for 16 digit card number
print("Enter your 16 Digit Card Number:"),
ccn=int(raw_input())
if(len(str(ccn))!=16):
	print "Unable to verify please check number"
else:
	w=ccn
	sum=0
	a=[]
	while(w):
		h=w%10
		a.append(h)
		w=w//10
# warning: reverse storage
for i in range(1,16,2):
	x=2*a[i]
	if(x>9):
		p1=x
		y=0
		while(p1):
			y+=p1%10
			p1=p1//10
		sum+=y
	else:
		sum+=x
for i in range(0,16,2):
	sum+=a[i]
if(sum%10==0):
	print("valid card number, Card Issuer is:"),
	verify(a[15],a[14],a[13],a[12])
else:
	print("Invalid card number")