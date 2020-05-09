

# class LinkedListDescending:
#     class node:
#         def __init__(self,char,freq=1):
#             this.char = char
#             this.freq = freq
#             this.next = None
#             this.last= None
#
#     def __init__(self, word):
#         self.head = None
#         self.tail = None
#         self.members = [] # O(u) memory. u = the numer of unique characters.
#         for char in word:
#             myll.add(char)
#
#     def add(self, char):
#         # check to see if the char is in the dict.
#         if char in self.members:
#             node = self.members[char]
#             node.freq += 1
            # I regret this...

            # if node.last:
            #     # sort current node (in descending order)
            #     if node.last.freq < node.freq:
            #         # make the last node point to the next node after the current
            #         node.last.next = node.next
            #         # make the current node's next point to the last node
            #         node.next = node.last
            #         # make the last pointer of the next node (what used to be the last node) point to the current node.
            #         node.next.last = node
            #         # 0-1-2-(3)-4 # curr = ()
            #         # 2's next points to 4
            #         # 3's next points to 2
            #         # 2's last points 3
            #         # 0-1-3-2-4
            #         if node.last.last:
            #             node.last.last.next = node
            #         else:
            #             node.last = None
            #         if node.next.next:
            #             node.next.next.last = node
            #         else:


        # else:
        #     # create a new node.
        #     # add it to the member dict and add it to the tail of the list
        #     self.members[char] = node(char)
        #     self.tail.next = self.members[char]
        #     self.tail = self.members[char]
        #
        # # update the linkedlist
        # if self.head == None:
        #     self.head = self.members[char]
        # elif self.tail == None:
        #     self.head.next = self.members[char]
        #     self.tail = self.members[char]
        #     self.tail.last = self.head
#
#     def stringified(self):
#         curr = self.head
#         result = []
#         while curr:
#             result += [curr.char * curr.freq]
#             curr.next
#
#         return "".join(result)
#
#
#
# def sort_freq(word):
#     if not len(word):
#         return ""
#
#     myll = LinkedListDescending(word)
#     return myll.stringified()


from collections import Counter

# "tree" becomes "eert"
def sort__by_freq(word):
    # make a histrogram-dictionary of characters to frequency
    histo = Counter(word)
    # create a dictionary of frequencies to arrays of characters with that frequency
    val_lookup = {}
    for key in histo.keys():
        val = histo[key]
        if val not in val_lookup:
            val_lookup[val] = [key]
        else:
            val_lookup[val].append(key)
    print(val_lookup)

    # sort the values of the histogram (the frequencies) in descending order
    vals = list(histo.values())
    vals.sort(reverse=True)

    # intialize an empty result array
    result = []
    #iterate through the sorted vals
    for val in vals:
        # add the characters from the the dictionary of frequencies
        # to the result array making sure to add the same number
        # of characters as that character's frequency (if that makes sense)
        while(val_lookup[val]):
            result+=[val_lookup[val].pop()]*val

    #return the result array's items as a string
    return "".join(result)

print(sort__by_freq("street"))
