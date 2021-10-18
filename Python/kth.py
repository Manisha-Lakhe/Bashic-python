def element(li,k): 
	small = sorted(li)[k-1] 
	print('Smallest {}th element is {}'.format(k,small))	
	high = sorted(li)[-k]
	print('highest {}th element is {}'.format(k,high))	
	
li = list(map(int, input('Enter your list').split()))
k = int(input("Enter the position"))
element(li,k)
