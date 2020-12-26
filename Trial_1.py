#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json

def createJson(jsonPath, inputDICT):
    with open(jsonPath, 'w', encoding='utf-8') as f:
        json.dump(inputDICT, f, indent=4, ensure_ascii=False)

if __name__== "__main__":
    adjDICT = {}    
    with open("ntusd-positive.txt", encoding="utf-8") as f:
        posSTR = f.read() 
    posLIST = posSTR.split()
    
    with open("ntusd-negative.txt", encoding="utf-8") as f:
        negSTR = f.read() 
    negLIST = negSTR.split()  
    
    adjDICT["positive"] = posLIST
    adjDICT["negative"] = negLIST
    
    createJson('./adjectives.json', adjDICT)
    