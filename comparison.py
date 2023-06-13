import time
import random

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

def merge_sort(arr):
	if len(arr) > 1:
		left_arr = arr[:len(arr)//2]
		right_arr = arr[len(arr)//2:]
		
		merge_sort(left_arr)
		merge_sort(right_arr)
		
		i = 0
		j = 0
		k = 0
		while i < len(left_arr) and j < len(right_arr):
			if left_arr[i] < right_arr[j]:
				arr[k] = left_arr[i]
				i += 1
				k += 1
			else:
				arr[k] = right_arr[j]
				j += 1
				k += 1
		while i < len(left_arr):
			arr[k] = left_arr[i]
			i += 1
			k += 1
		while j < len(right_arr):
			arr[k] = right_arr[j]
			j += 1
			k += 1	


for i in range(3, 10):
	noe = 10**i
	arr = []
	for j in range(noe):
		arr.append(random.randint(0, 10e9))
	arr2 = [*arr]
	t1 = time.time()*1000
	merge_sort(arr)
	t2 = time.time()*1000
	quick_sort(arr2, 0, len(arr2)-1)
	t3 = time.time()*1000
	print(f"Test {i-2}: Elements: {noe}")  
	print(f"Merge sort: {(t2-t1):.2f} ms")
	print(f"Quick sort: {(t3-t2):.2f} ms")

		





