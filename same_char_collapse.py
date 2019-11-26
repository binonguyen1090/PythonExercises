# Same Char Collapse
# Write a method same_char_collapse that takes in a string and returns a collapsed version of the string. To collapse the string, we repeatedly delete 2 adjacent characters that are the same until there are no such adjacent characters. If there are multiple pairs that can be collapsed, delete the leftmost pair. For example, we take the following steps to collapse "zzzxaaxy": zzzxaaxy -> zxaaxy -> zxxy -> z



def same_char_collapse(str):
  
  condition = True
  while condition:
    condition = False
    splt = list(str)
    for i in range(0 ,len(splt)-1):
      if splt[i] == splt[i+1]:
        splt[i] = ""
        splt[i+1] = ""
        condition = True
        break
    str = "".join(splt)
  print(str)

    

same_char_collapse("zzzxaaxy")   #=> "zy"
# because zzzxaaxy -> zxaaxy -> zxxy -> zy


same_char_collapse("uqrssrqvtt") #=> "uv"
# because uqrssrqvtt -> uqrrqvtt -> uqqvtt -> uvtt -> uv