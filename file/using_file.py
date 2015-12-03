#!/usr/bin/python
#filename: using_file.py

hello = 'hello world file \n'

f = file(r'hello.txt', 'w')
f.write(hello)
f.write('hello python world\n')
f.close()

