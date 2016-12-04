# http://www.pythonchallenge.com/pc/def/map.html

original_string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
new_string = ""

# try

for i in range(len(original_string)):
    old_char = original_string[i]
    if ord(old_char) >= ord("a") and ord(old_char) <= ord ("z"):
        new_char = chr(ord("a") + (ord(old_char)+2 - ord("a")) % (ord("z")-ord("a")+1))
    else:
        new_char = old_char
    new_string += new_char

print new_string

# solution

import string

stringin = "abcdefghijklmnopqrstuvwxyz"
stringout = "cdefghijklmnopqrstuvwxyzab"

translation = string.maketrans(stringin, stringout)

new_string = original_string.translate(translation)

print new_string

# next

print "http://www.pythonchallenge.com/pc/def/map.html".translate(translation)
