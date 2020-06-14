  # key info: letters indicate numbers.
  # there are 26 letters in the alphabet
  # when you get to 27, the alphabet begins to repeat

  # input: letters (uppercase string)
  # output: integer that indicates column

  # the least significant "digit(s)" is represented by the first letter
  # the length of the string indicates how many 26's are present in the final number.

  # psuedocode:
  #       create a lookup table of letters to digits.
  #       work from the back of the string.

def excel_column_to_number(column):
  alpha = list("abcdefghijklmnopqrstuvwxyz".upper())
  LOOKUP = {n:i+1 for i, n in enumerate(alpha)}
  _sum = 0
  i = 0
  column = column[::-1]
  while i < len(column):
    letter = column[i]
    if letter in LOOKUP:
      _sum += LOOKUP[letter]*26**i
    i+=1
  return _sum
  # return columnd=
alpha = "abc".upper()#731
print(excel_column_to_number(alpha))
