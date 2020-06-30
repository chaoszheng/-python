nums = [1, 2, 2, 2, 4, 6]

##1 二分查找
def binary_search(nums, tar):
	"""
	:type nums:list
	:type tar:int
	:rtype int
	"""
	left, right = 0, len(nums) - 1
	while left <= right:
		mid = int(left + (right - left)/2)
		if nums[mid] == tar:
			return mid
		elif nums[mid] > tar:
			right = mid - 1
		elif nums[mid] < tar:
			left = mid + 1
	return -1

##2 搜索左边界
def binary_search_left(nums, tar):
	"""
	:type nums:list
	:type tar:int
	:rtype int
	"""
	if len(nums) == 0: return -1
	left, right = 0, len(nums) - 1
	while left <= right:
		mid = int(left + (right - left)/2)
		if nums[mid] == tar:
			right = mid - 1
		elif nums[mid] > tar:
			right = mid - 1
		elif nums[mid] < tar:
			left = mid + 1
	if left >= len(nums) or nums[left] != tar:
		return -1
	return left

##3 搜索右边界
def binary_search_right(nums, tar):
	"""
	:type nums:list
	:type tar:int
	:rtype int
	"""
	if len(nums) == 0: return -1
	left, right = 0, len(nums) - 1
	while left <= right:
		mid = int(left + (right - left)/2)
		if nums[mid] == tar:
			left = mid + 1
		elif nums[mid] > tar:
			right = mid - 1
		elif nums[mid] < tar:
			left = mid + 1
	if right < 0 or nums[right] != tar:
		return -1
	return right


if __name__ == '__main__':
	index = binary_search_right(nums, 2)
	print(index)