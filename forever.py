#!/usr/bin/python
from subprocess import Popen
import sys

filname = sys.argv[1]
while True:
    print('\nStarting' + filename)
    p = Popen('python ' + filename, shell=True)
    p.wait()
