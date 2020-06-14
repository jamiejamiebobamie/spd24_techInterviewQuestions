# # input: an array of integers
# # output: an integer, how many da operations are needed to sort this array
# def da_sort(nums):
#   def helper():
#     min_indices = []
#     min_value = float("inf")
#     for n in nums:
#       if n != None:
#         if n < min_value:
#           min_value = n
#     for i, n in enumerate(nums):
#       if n:
#         if n == min_value:
#           min_indices.append(i)
#           nums[i] = None
#     return len(min_indices)
#
#   sum_operations = 0
#   while any(nums):
#     sum_operations+=helper()
#     print(nums)
#   return sum_operations
#
# nums = [3,4,5,1,1,1,2,2,1]
# print(da_sort(nums))


# def color_sort(nums):
#   i = 0
#   j = len(nums)-1
#   while i < j:
#     if nums[i] > nums[j]:
#       nums[i], nums[j] = nums[j], nums[i]
#     i+=1
#     j-=1
#     print(i,j,len(nums))
#
# nums = [0,0,1,1,1,2,2]
# color_sort(nums)


# def k_backspace(inputString):
#   i = len(inputString)-1
#   intended_string_array = []
#   while i >= 0:
#     if inputString[i] != "<":
#       intended_string_array.append(inputString[i])
#       i-=1
#     else:
#       i-=2
#   return "".join(intended_string_array[::-1])
#
# # don't forget to actually call your answer's function!
# testInput = 'a<bc<'
# actualOutput = k_backspace(testInput)
# print(actualOutput)

# def k_backspace(inputString):
#     i = len(inputString)-1
#     stack=0
#     intended_string_array = []
#     while i >= 0:
#         if inputString[i] != "<":
#             if not stack:
#                 intended_string_array.append(inputString[i])
#             else:
#                 stack-=1
#         else:
#             stack+=1
#         i-=1
#
#     return "".join(intended_string_array[::-1])
#
# # don't forget to actually call your answer's function!
# testInput = '<a<aaa<<<'
# actualOutput = k_backspace(testInput)
# print(actualOutput)

def backspaceCompare(String1, String2):
  i = len(String1)-1
  j = len(String2)-1

  i_count = 0
  j_count = 0

  while i >= 0 and j >= 0:
    if String1[i] != "#" or String2[j] != "#":
      if i_count or j_count:
        if i_count:
          i-=1
          i_count-=1
        else:
          j-=1
          j_count-=1
      else:
        if String1[i] == String2[j]:
          i-=1
          j-=1
        else:
          return False
    else:
      if String1[i] != "#":
        i_count+=1
        i-=1
      if String2[j] != "#":
        j_count+=1
        j-=1

    return True

print("hi")
sampleInput1A = "ab#"
sampleInput1B = "ab#"
print(backspaceCompare(sampleInput1A, sampleInput1B))
