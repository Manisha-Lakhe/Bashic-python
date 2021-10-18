def sortt(li):
	s = []
	for i in range(0,3):
		for j in range(0,len(li)):
			if(li[j] == i):
				s.append(li[j])
	return s
	
	
li = list(map(int,input('Enter your list').split()))
print(sortt(li))
