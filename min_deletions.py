"""

Given two words word1 and word2, find the minimum number of steps required to
make word1 and word2 the same, where in each step you can delete
one character in either string.

https://leetcode.com/articles/delete-operation-for-two-strings/
"""

def min_deletions(str1,str2):
    sub_set = set()
    def helper(sub1,sub2,i):
        if i > len(sub1) or i > len(sub2):
            return
        if sub1 == sub2:
            sub_set.add(sub1)
        # what are the base cases?
            # delete nothing from either word, but increment the index
            # delete a letter from str1 and increment index
            # delete a letter from str2 and increment index
        i+=1
        helper(sub1[i:],sub2,i)
        helper(sub1,sub2[i:],i)
        helper(sub1,sub2,i)
    helper(str1,str2,0)
    max_sub = ""
    for sub in sub_set:
        if len(sub) > len(max_sub):
            max_sub = sub
    return len(str1) - len(max_sub) if len(str1) > len(str2) else len(str2) - len(max_sub)
str1 = "slough"
str2 = "through"
print(min_deletions(str1,str2))
