####### File Handling ######

''' Modes
r,r+
w,w+
a,a+'''

import csv
import json

file = open('demo.txt','w+')
file.write('hello world\n')
file.write('hello world')
file.seek(0)
f = file.readlines()
print(f)
file.close()
