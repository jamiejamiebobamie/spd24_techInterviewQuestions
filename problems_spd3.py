"""
Tuesday, February 11th
Warmup
You're given this problem at a technical interview:
Rotate a given linked list counter-clockwise by k nodes, where k is a given integer.

Write your answers to these in your notebook:
What clarifying questions would you ask?
What reasonable assumptions could you state?
What are 2-3 ways you can simplify the problem?
Brainstorm 2-3 ways to approach the problem.
Choose one idea and write pseudocode for it.

Activity
Choose a problem below at the appropriate difficulty level for your own experience.
What are edge case inputs that could be challenging to handle in your solution?
How can you simplify the problem to ensure you make progress and don’t get stuck?

Linked List Problems
Given a singly-linked list, find the middle value in the list.
Example: If the given linked list is A → B → C → D → E, return C.
Assumptions: The length (n) is odd so the linked list has a definite middle.
Given a singly-linked list, reverse the order of the list by modifying the nodes’ links.
Example: If the given linked list is A → B → C → D → E, nodes should be
modified/rearranged so the list becomes E → D → C → B → A.
Given a singly-linked list, rearrange the nodes by interleaving the first half
of the linked list with the second half.
Example: If the given linked list is A → B → C → D → E → F → G → H, nodes should be
rearranged so the list becomes A → C → E → G → B → D → F → H.
Rotate a given singly-linked list counter-clockwise by k nodes, where k is a given integer.
Example: If the given linked list is A → B → C → D → E → F and k is 4, nodes
should be modified so the list becomes E → F → A → B → C → D.
Assumptions: k is positive and smaller than n, the length of the linked list.
Given an array of k singly-linked lists, each of whose values are in sorted
order, combine all nodes (do not create new nodes) into one singly-linked list
with all values in order.


Homework – Due next week: Tuesday, February 18th
Fully solve at least two of the above linked lists problems in real
working code. Use your idea sketches and pseudocode, type it in your code
editor, run some test cases, and debug your code so it works correctly.
Implement at least one solution for 2 or more of the problems above.
"""

class LL:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.len = 0

    def add(self, node):
        self.tail.next = node
        self.tail = node
        self.len += 1

    def print_list(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def rotate_counter_clockwise(self,k):
        for _ in range(k):
            self.tail.next = self.head
            self.tail = self.head
            temp = self.head
            self.head = self.head.next
            temp.next = None

    def find_middle(self):
        node = self.head
        count = 0
        while node and count < self.len/2:
            node = node.next
            count+=1
        print(node.data)

    # first simplification: dont worry about doing it in place.
    def interleave(self):
        odds = LL()
        odds.head, odds.tail = self.head, self.head
        evens = LL()
        evens.head, evens.tail = self.head.next, self.head.next

        node = self.head
        count = 1
        odd = count % 2
        while node:
            if odd:
                odds.add(node)
            else:
                evens.add(node)
            node = node.next
            count += 1
            odd = count % 2
            # print(node.data)
        odds.tail.next = evens.head
        odds.print_list()


class LLNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# myLL = LL()
# head = LLNode('a')
# myLL.head, myLL.tail = head, head
# myLL.add(LLNode('b'))
# myLL.add(LLNode('c'))
# myLL.add(LLNode('d'))
# myLL.add(LLNode('e'))

# Rotate a given linked list counter-clockwise by k nodes, where k is a given integer.
"""
    k = 3   # num to rotate
    12345   # list
    <-      # counterclockwise
    23451   #1 iteration
    34512   #2 iteration
    45123   #3 iteration
"""

# myLL.print_list()
# myLL.rotate_counter_clockwise(3)
# print()
# myLL.print_list()
# print()

# Given a singly-linked list, find the middle value in the list.

"""
What are edge case inputs that could be challenging to handle in your solution?

    some edge cases might be: what if the list is even?
    should we return two nums or favor the first/second middle node?

    what if the list is empty?

    what if the list is composed of only one node?

    what if the list is circular? where the list's tail's next points to the head?

How can you simplify the problem to ensure you make progress and don’t get stuck?

    one simplification is to assume the list is odd and then work out edge cases later...
"""
# myLL.print_list()
# myLL.find_middle()
# print()
# myLL.add(LLNode('f'))
# myLL.print_list()
# myLL.find_middle()

"""
HW
Given a singly-linked list, rearrange the nodes by interleaving the first half
of the linked list with the second half.
Example: If the given linked list is A → B → C → D → E → F → G → H, nodes should be
rearranged so the list becomes A → C → E → G → B → D → F → H.
"""
# 1 2 3 4 5 6 7 8
# 1 3 5 7 2 4 6 8
# A → B → C → D → E → F → G → H
# A → C → E → G → B → D → F → H

# myLL.print_list()
# myLL.interleave()


# myLL = LL()
# head = LLNode('a')
# myLL.head, myLL.tail = head, head
# myLL.add(LLNode('g'))
# myLL.add(LLNode('c'))
# myLL.add(LLNode('i'))
# myLL.add(LLNode('e'))
#
# myLL2 = LL()
# head2 = LLNode('f')
# myLL2.head, myLL.tail = head2, head2
# myLL2.add(LLNode('b'))
# myLL2.add(LLNode('h'))
# myLL2.add(LLNode('d'))
# myLL2.add(LLNode('j'))


"""
Given an array of k singly-linked lists, each of whose values are
in sorted order, combine all nodes (do not create new nodes)
into one singly-linked list with all values in order.
"""

odd = LL()
odd_head = LLNode(1)
odd.head, odd.tail = odd_head, odd_head
odd.add(LLNode(3))
odd.add(LLNode(5))
odd.add(LLNode(7))
odd.add(LLNode(9))
odd.print_list()
print()

even = LL()
even_head = LLNode(2)
even.head, even.tail = even_head, even_head
even.add(LLNode(4))
even.add(LLNode(6))
even.add(LLNode(8))
even.add(LLNode(10))
even.print_list()
print()

# in progress...
def combineLL(LL1, LL2):

    if LL1.head.data < LL2.head.data:
        listToAdd = LL1
        listToTakeFrom = LL2
    else:
        listToAdd = LL2
        listToTakeFrom = LL1

    add = listToAdd.head
    add_prev = listToAdd.head
    take = listToTakeFrom.head

    while add.next and take:
        # if the data in the node in the listToAdd is greater than the listToTakeFrom
            # the lists are out of order and we need to make the
            # listToTakeFrom node point to the listToAdd node.
            # we need to save the current next pointer of listToTakeFrom before we change it.
        # print(add.data, take.data)
        if add.data > take.data:
            temp_node = take.next
            take.next = add
            if add != add_prev:
                add_prev.next = take
            else:
                listToAdd.head = take
            add_prev = take
            take = temp_node
            # print(take.data)
            take = take.next
        else:
            add_prev = add

        if not add.next:
            listToAdd.tail = add

        add = add.next

    if take:
        # add_prev.next = take
        listToAdd.tail = take

    return listToAdd

combined = combineLL(even, odd)

combined.print_list()
print()
