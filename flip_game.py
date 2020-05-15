"""

given a string, return all possible permutations of a string where two plus
    signs have been flipped

input: "++++"
output:["--++", "+--+", "++--"]

"""

def return_first_move_flip_game(s):
    string_array = list(s)
    result = []
    for i, char in enumerate(s):
        if i != len(s) - 1:
            if char == "+" and s[i+1] == "+":
                string_array[i],string_array[i+1] = "-", "-"
                result.append("".join(string_array))
                string_array[i],string_array[i+1] = "+", "+"
    return result

s = "++++"
print(return_first_move_flip_game(s))
