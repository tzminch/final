#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
from ArticutAPI import ArticutAPI

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
    
    with open("民間文學與說唱藝術_蔡孟珍.txt", encoding="utf-8") as f:
        inputSTR = f.read()    
    articut = ArticutAPI.Articut()
    resultDICT = articut.parse(inputSTR)
    #resultLIST = articut.getNounStemLIST(resultDICT)
    #print(resultDICT)
    resultLIST = resultDICT["result_segmentation"]
    refLIST = resultLIST.split("/")
    
    score = 0
    for i in refLIST:
        for j in posLIST:
            if i == j:
                score += 1
        for k in negLIST:
            if i == k:
                score -= 1
    print("此門課分數為：", score)
    
    if score > 0:
        print("正面")
    else:
        print("負面")

    