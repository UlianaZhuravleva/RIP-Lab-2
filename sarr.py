def findmin(arr):
	min=arr[0]
	for i in range(len(arr)):
		if min>= arr[i]:
			min=arr[i]
	print(min)


def sarr(arr):
	s=0
	for i in range(len(arr)):
		s=s+arr[i]
	s=s/len(arr)
	print(s)


arr1=[5, 2, 4, 0, 9]
findmin(arr1)
sarr(arr1)

