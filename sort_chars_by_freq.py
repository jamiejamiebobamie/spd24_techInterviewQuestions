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
            char = val_lookup[val].pop()
            result += [ char ] * val

    #return the result array's items as a string
    return "".join(result)

print(sort__by_freq("street"))
