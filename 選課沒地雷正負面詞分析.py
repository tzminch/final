#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
from ArticutAPI import ArticutAPI
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def createJson(jsonPath, inputDICT):
    with open(jsonPath, 'w', encoding='utf-8') as f:
        json.dump(inputDICT, f, indent=4, ensure_ascii=False)
        
def wordcloud(inputSTR):
    font = 'SourceHanSansTW-Regular.otf'
    my_wordcloud = WordCloud(font_path=font).generate(inputSTR)
    plt.imshow(my_wordcloud)
    plt.axis("off")
    plt.show() 
    
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
    resultDICT = articut.parse(inputSTR, userDefinedDictFILE="adjectives.json")    
    #resultDICT = articut.parse(inputSTR)
    #resultLIST = articut.getNounStemLIST(resultDICT)
    #print(resultDICT)
    resultLIST = resultDICT["result_segmentation"]
    refLIST = resultLIST.split("/")
    
    posScore = 0
    negScore = 0
    posSTR = ""
    negSTR = ""
    for i in range(len(refLIST)):
        for j in posLIST:
            if refLIST[i] == j:
                if j == "很多":
                    print(refLIST[i], refLIST[i+1])
                    posSTR = posSTR + refLIST[i] + refLIST[i+1] + " "
                else:
                    posScore += 1
                    print("positive", refLIST[i])
                    posSTR = posSTR + refLIST[i] + " "
        for k in negLIST:
            if refLIST[i] == k:
                if k == "沒有":
                    print(refLIST[i], refLIST[i+1])
                    negSTR = negSTR + refLIST[i] + refLIST[i+1] + " "
                else:
                    negScore += 1
                    print("negative", refLIST[i])
                    negSTR = negSTR + refLIST[i] + " "
    
    allSTR = posSTR + negSTR
    print("此門課分數為：", posScore // negScore)
    
    if posScore // negScore > 1:
        print("正面")
    else:
        print("負面")
    
    print(posSTR)
    print(negSTR)
    
    wordcloud(posSTR)
    wordcloud(negSTR)
    wordcloud(allSTR)
    
    