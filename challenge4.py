# http://www.pythonchallenge.com/pc/def/linkedlist.php

import re
import urllib2

base_url="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
url = base_url+"12345"


while True:
    source = urllib2.urlopen(url).read()
    match = re.findall("[0-9]+",source)
    if match:
        next_number = match[-1]
        print next_number
    else:
        print source, url
        next_number = str(int(next_number)/2)
    url = base_url+next_number
