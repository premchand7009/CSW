import re
def find_repeated_letters(s):
    pattern=r"(\w)\1+"
    
    for i in re.finditer(pattern,s):
        print(i.group(0),i.group(1),i.span())


s="aa jfodhh bbbb df jjjjjj"
find_repeated_letters(s)