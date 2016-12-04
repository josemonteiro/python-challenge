# http://www.pythonchallenge.com/pc/def/ocr.html

import urllib2

url = "http://www.pythonchallenge.com/pc/def/ocr.html"
source = urllib2.urlopen(url).read()

source_lines = source.split("\n")

relevant_lines = source_lines[37:1256+1]

count_dict = dict()

for line in relevant_lines:
    for char in line:
        if count_dict.has_key(char):
            count_dict[char]+=1
        else:
            count_dict[char]=1

#print count_dict

#for key in count_dict:
#    print key, count_dict[key]

new_string = "".join(relevant_lines)

for key in count_dict:
    if count_dict[key]>1:
        new_string = new_string.replace(key, "")

print new_string
