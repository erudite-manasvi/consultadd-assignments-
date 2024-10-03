# Write a Python function that finds the median of a list of numbers.

def find_median(v):
	v.sort()
		
	mid = len(v)//2
		
	if len(v)%2!=0:
		return v[mid]
		
	return ((v[mid])+v[mid-1])//2

print(find_median([7, 2, 5, 1, 9, 3]))