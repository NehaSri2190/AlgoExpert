# Function to find two numbers from a given array of distinct numbers whose sum is equal to a Target Sum. Time Complexity of the solutions is O(nlog(n)) and space complexity of O(1)

def twoNumberSum(array, targetSum):
	array.sort()
	left = 0
	right = len(array) - 1
	while left < right:
		Sum = array[left] + array[right]
		if Sum == targetSum:
			return [array[left],array[right]]
		elif Sum > targetSum :
			right = right - 1
		elif Sum < targetSum :
			left = left + 1
	return []