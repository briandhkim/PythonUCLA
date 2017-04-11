# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 18:44:51 2017

@author: Brian

this was designed to analyze the number of each words used in a provided text
in this case, the text is Agatha Christie's "The Mysterious Affair at Styles"

"""

from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize
from nltk import FreqDist
import urllib

def lexical_diversity(text):
    return len(set(text)) / len(text)       #5 lexical diversity
#nltk.download()

url = "http://www.gutenberg.org/files/863/863-0.txt"
response = urllib.urlopen(url)
raw = response.read().decode('utf8')
#url open file 

#f = open("863-0.txt")
#txt = f.read()
#raw = txt.decode('utf8')


raw.find("CHAPTER I. I GO TO STYLES") #1215
raw.find("THE END")   #322022           #3**********

raw =  raw [1215: 322022]
#new length: 320807
#includes "CHAPTER I..." at the beginning
#does not include "THE END" at the end

#ss = raw.split()  #dictionary of the words 1F
#dic = {w:ss.count(w) for w in ss}
##dic len = 9967                #4************

raw = raw.replace("_", "")    #5 remove "_" underscores
                                #new raw len = 320509
tokens = word_tokenize(raw)     #5***********

#fdist = FreqDist(raw)
fdist = FreqDist(tokens)  #5843 samples and 72791 outcomes
#len 5886 with tokens
#len 5843 with underscores removed
print lexical_diversity(tokens)

#6 look at 3.1 NLP Pipeline .lower() function
words = [w.lower() for w in tokens]
#removes upper and lower case differences. len: 72791
fdist2 =  FreqDist(words)  #5393 samples and 72791 outcomes

#7***************
porter = nltk.PorterStemmer()
#lancaster = nltk.LancasterStemmer()
st = [porter.stem(w) for w in words]    #eliminating word difference in affixes
#lt = [lancaster.stem(w) for w in tokens]

#8***************
text = nltk.Text(tokens) #turning tokens list from 5 into .Text object
#print text.concordance("point")

#this prints the most commonly used words without ignoring punctuation
print fdist.most_common(30)


#this will print most commonly used words ignoring punctuation
list2 = []
for w in tokens:
    if w.isalpha():
        list2.append(w)
        
print "words only"        
fdist3 =  FreqDist(list2)
print fdist3.most_common(30)