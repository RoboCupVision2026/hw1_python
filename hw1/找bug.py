if __name__ == "__main__":
	list1=list(range(1000))
	for idx in range(999,-1,-1):
		if list1[idx]%2==1:
			list1.pop(idx)
print("bug就是第四步检验是否是奇数时出错；错误原因：在删除元素时，list的长度一直在变化，而题目的idx忽略了这个，一直在前进检查，这样就会漏掉很多数，导致bug出现")
