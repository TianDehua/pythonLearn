# -*- coding: utf-8 -*-
def trim(s):
    if len(s) == 0 :
        return s
    start=0
    while s[start]==' ' :
        start+=1
    end=len(s)
    while s[end-1]==' ' and end>start :
        end-=1
    return s[start:end]
	
print(trim('hello  '))