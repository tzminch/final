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
    
    score = 0
    posSTR = ""
    negSTR = ""
    for i in refLIST:
        for j in posLIST:
            if i == j:
                score += 1
                print("positive", i)
                posSTR = posSTR + i + " "
        for k in negLIST:
            if i == k:
                score -= 1
                print("negative", i)
                negSTR = negSTR + i + " "
    
    allSTR = posSTR + negSTR
    print("此門課分數為：", score)
    
    if score > 0:
        print("正面")
    else:
        print("負面")
    
    print(posSTR)
    print(negSTR)
    
    wordcloud(posSTR)
    wordcloud(negSTR)
    wordcloud(allSTR)
    
    