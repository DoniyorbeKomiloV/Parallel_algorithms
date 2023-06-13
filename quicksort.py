def quick_sort(arr, left, right):
	if left < right:
		partition_pos = partition(arr, left, right)
		quick_sort(arr, left, partition_pos-1)
		quick_sort(arr, partition_pos+1, right)		


def partition(arr, left, right):
	i = left
	j = right - 1
	pivot = arr[right]
	
	while i < j:
		while i < right and arr[i] < pivot:
			i += 1
		while j > left and arr[j] and arr[j] >= pivot:
			j -= 1
			
		if i<j:
			arr[i], arr[j] = arr[j], arr[i]
	
	if arr[i] > pivot:
		arr[i], arr[right] = arr[right], arr[i]
	
	return i


arr = [11, 55, 66, 33, 88, 22, 44, 99, 77]
quick_sort(arr, 0, len(arr)-1)
print(*arr)

""" Output

11 22 33 44 55 66 77 88 99

"""
