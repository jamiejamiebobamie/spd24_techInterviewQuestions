def find_index_of_min(starting_i, nums):
  index = -1
  for i in range(starting_i+1, len(nums)):
    if nums[index] > nums[i]:
      index = i
  return index if index != -1 else len(nums)-1

def da_sort(nums):
  # look for the smallest value.
  # from the index of the smallest value to the end of the list
  # look for the next smallest value that is not larger than the elements
  # already iterated over.

    # 2,1,4,3
    # value 1 at index 1 is the only value sorted / that matters.
    # 3 is the next smallest value but is invalidated by the skipped 2

    # return len(arr) - "values that matter"
  vals_iterated = set()
  i = 0
  count = 0
  smallest_val_index = 0
  while i < len(nums):
    store_i = smallest_val_index
    smallest_val_index = find_index_of_min(smallest_val_index, nums)
    for val in vals_iterated:
      if val < nums[smallest_val_index]:
        return len(nums) - store_i
    if store_i == smallest_val_index:
      i+=1
    else:
      for j in range(store_i+1,smallest_val_index):
        vals_iterated.add(nums[j])
      i = smallest_val_index
  if not vals_iterated:
    return 0
  else:
    return store_i



nums = [1, 3, 2, 4, 5, 6, 7] # 5
# nums = [6,5,4,3,2,1] # 5
# nums = [1, 2, 3, 4]
# nums = [5,4,3,2,1]
# nums = [1, 5, 2, 4, 3, 6,7,8]


print(da_sort(nums))
