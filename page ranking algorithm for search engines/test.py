Ca=1.00
Cb=1.00

PRa=0.00
PRb=0.00

d=0.85

PRa_prev=0.00
PRb_prev=0.00

i=0
x=1

while i<2:
	print("iteration ",x)

	PRa=(1-d)+d*(PRb/Cb)

	PRb=(1-d)+d*(PRa/Ca)
	
	if (PRa-PRa_prev)<0.0000001 and (PRb-PRb_prev)<0.0000001:
		print("Optimized PR(A)=",PRa)
		print("Optimized PR(B)=",PRb)
		i=3
		break
	else:
		print("PR(A)=",PRa)
		print("PR(B)=",PRb)

	PRa_prev=PRa
	PRb_prev=PRb

	x+=1

	print("\n")

