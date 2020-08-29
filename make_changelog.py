#!/usr/bin/python3

import io
import sys
import lxml.html
mytext = open('./build/changes/changes.html').read()
doc = lxml.html.fromstring(mytext)

title = doc.xpath('.//title/text()')
modified_items = doc.xpath('.//a/text()')
original_stdout = sys.stdout
with open('./build/changes/changelog.txt', 'w') as filename :
    sys.stdout = filename
    print(title[0])
    for item in modified_items :
        print(item)
    sys.stdout=original_stdout
