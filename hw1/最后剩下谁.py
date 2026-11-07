if __name__ == "__main__":
	people=list(range(1,234))
	idx=0
	count=0
	while len(people)>1:
		count=count+1
		if count==3:
			people.pop(idx)
			count=0
			if idx>=len(people):
				idx=0

		else:
			idx=idx+1
			if idx>=len(people):
				idx=0
	print("最后留下的是原来第{}号".format(people[0]))
