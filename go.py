#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 10:35:28 2019

@author: wannaphong
"""
from test import *
from pythainlp.tokenize import  word_tokenize
data=getdata()
'''cut="\n".join(["|".join(word_tokenize(i))+"|" for i in data])
save(cut,"p1")
from testcut import cutok as cut1
from testcut2 import cutok as cut2
from testcut3 import cutok as cut3
from testcut4 import cutok as cut4
cut="\n".join([cut1(i)+"|" for i in data])
save(cut,"p2")
cut="\n".join([cut2(i)+"|" for i in data])
save(cut,"p3")
cut="\n".join([cut3(i)+"|" for i in data])
save(cut,"p4")
cut="\n".join([cut4(i)+"|" for i in data])
save(cut,"p5")
cut="\n".join(["|".join(word_tokenize(i,engine="ulmfit"))+"|" for i in data])
save(cut,"p6")
cut="\n".join(["|".join(word_tokenize(i,engine="longest"))+"|" for i in data])
save(cut,"p7")
cut="\n".join(["|".join(word_tokenize(i,engine="mm"))+"|" for i in data])
save(cut,"p8")
cut="\n".join(["|".join(word_tokenize(i,engine="icu"))+"|" for i in data])
save(cut,"p9")'''
from wordcut import Wordcut
wordcut = Wordcut.bigthai()
cut="\n".join(["|".join(wordcut.tokenize(i))+"|" for i in data])
save(cut,"p11")
cut="\n".join(["|".join(word_tokenize(i,engine="deepcut"))+"|" for i in data])
save(cut,"p10")