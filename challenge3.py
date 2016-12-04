# http://www.pythonchallenge.com/pc/def/equality.html

import urllib2

url = "http://www.pythonchallenge.com/pc/def/equality.html"
source = urllib2.urlopen(url).read()

source_lines = source.split("\n")
relevant_lines = source_lines[21:1270+1]
line_size = len(relevant_lines[0])
relevant_string = "".join(relevant_lines)

def check(string, index):
    # center
    check1 = not (index+3<len(string)) or string[index+3].islower()
    # left
    check2 = not (index-1>=0) or (string[index:index+3].isupper() and string[index-1].islower())
    # right
    check3 = not (index+7<len(string)) or (string[index+4:index+7].isupper() and string[index+7].islower())

    if check1 and check2 and check3:
        print string[index+3],

for i in range(len(relevant_string)):
    check(relevant_string, i)
