#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, re
configFilePath = sys.argv[1]
value = sys.argv[2]


rC = re.compile(r'.*CC_LOGO_FLAG%S*=.*')
def match(str):
    pattern = ".*CC_LOGO_FLAG.*"
    matchObj = re.match(pattern, str)
    if matchObj:
        return "CC_LOGO_FLAG = %s\n"%value


pFile = open(configFilePath)
lines = pFile.readlines()

for k in range(0, len(lines)):
    print(lines[k])
    str = match(lines[k])
    if str:
        lines[k] = str;

pFile.close()

pFile = open(configFilePath, "w")
pFile.writelines(lines)
pFile.close()
