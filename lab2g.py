#!/usr/bin/env python3
# Author: Your Name
# Author ID: Your Seneca ID
# Date Created: yyyy/mm/dd
import sys

if len(sys.argv) > 1:
    timer = int(sys.argv[1])
else:
    timer = 3

while timer > 0:
    print(timer)
    timer -= 1
print('blast off!')
