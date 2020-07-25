"""Merge k sorted linked lists and return it as one sorted list.
Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6"""

# TOUGH

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# some ideas:
    # if you can merge two lists you can merge all lists.
    # you could also have a variable number of pointers and build a new list
    # as you iterate through all of the lists at once. (nvm... that wouldn't work?)
def mergeKLists(lists):
    def helper(l1_head,l2_head):
        # curr1 and main_list_head are set to the lower of the two head values.
        if not l1_head:
            return l2_head
        elif not l2_head:
            return l1_head
        if l1_head.val < l2_head.val:
            main_list_head = curr1 = l1_head
            curr2 = l2_head
        else:
            main_list_head = curr1 = l2_head
            curr2 = l2_head
        tail = main_list_head
        while curr1 and curr2:
            # print(curr1.val,curr2.val,curr1.next.val,curr2.next.val)
            # curr2 goes after curr1
            if curr1.val < curr2.val:
                if curr1.next:
                    if curr1.next.val > curr2.val or curr1.val == curr2.val:
                        temp1 = curr1.next
                        curr1.next = curr2
                        temp2 = curr2.next
                        curr2.next = temp1
                        if temp1:
                            tail = temp1
                        curr1 = temp1
                        curr2 = temp2
                    # increment curr1
                    elif curr1.next.val < curr2.val:
                        curr1 = curr1.next
            # curr1 goes after curr2
            elif curr1.val > curr2.val:
                if curr2.next:
                    if curr2.next.val < curr1.val:
                        temp1 = curr2.next
                        curr2.next = curr1
                        temp2 = curr1.next
                        curr1.next = temp1
                        if temp2:
                            tail = temp2
                        curr1 = temp2
                        curr2 = temp1
                    # increment curr2
                    elif curr2.next.val < curr1.val:
                        curr2 = curr2.next
        if curr2:
            tail.next = curr2

        return main_list_head
    main_list = None
    for i in range(len(lists)):
        main_list = helper(main_list, lists[i])
    return main_list


# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# head1 = one = ListNode(1)
# four = ListNode(4)
# one.next = four
# five = ListNode(5)
# four.next = five
#
# head2 = one_a = ListNode(1)
# three = ListNode(3)
# one_a.next = three
# four_a = ListNode(4)
# three.next = four_a
#
# head3 = two = ListNode(2)
# six = ListNode(6)
# two.next = six

head1 = one = ListNode(1)
four = ListNode(2)
one.next = four
five = ListNode(3)
four.next = five

head2 = one_a = ListNode(4)
three = ListNode(5)
one_a.next = three
four_a = ListNode(6)
three.next = four_a

head3 = two = ListNode(7)
six = ListNode(8)
two.next = six

l = [head1,head2,head3]
merged = mergeKLists(l)
curr = merged
while curr:
    print(curr.val)
    curr = curr.next
