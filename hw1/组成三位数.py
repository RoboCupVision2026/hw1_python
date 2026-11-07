for a in range(1,5):
	for b in range(1,5):
		for c in range(1,5):
			if a!=b and b!=c and c!=a:
				n=a*100+b*10+c
				print(n,end=" ")
