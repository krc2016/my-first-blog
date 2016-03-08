#!/usr/bin/env python
# -*- coding: utf-8 -*-
##########################################################
### Autor name : 		Firas HMIDA		##
### Date de création :		07-07-2014		##
### Date de modification : 	23-09-2014		##
### Contenu : 			CRC-Collocations	##
##########################################################

import re
import os
import sys
import xlrd
import time
import nltk
import xlwt
import pickle
import itertools
import subprocess
from math import *
from nltk.collocations import *
from operator import itemgetter
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.metrics import BigramAssocMeasures
from nltk.tokenize.regexp import RegexpTokenizer
from nltk import word_tokenize, wordpunct_tokenize
from nltk.collocations import BigramCollocationFinder


linesFR = list(set(open('corpus/vulcanoPOS.txt').read().strip().split('.	SENT	.')))
linesEN = list(set(open('corpus/vulcanoEN-POS.txt').read().strip().split('.	SENT	.')))

stop_wordsFR = open('stopW/StopWords.txt').read().strip().split('\n')
stop_wordsEN = open('stopW/StopWordsEN.txt').read().strip().split('\n')
styleEntete = xlwt.easyxf('font: name Times New Roman, color-index black, bold on;',
	num_format_str='#,##0.00')

wb = xlwt.Workbook(encoding='utf-8')
ws = wb.add_sheet('TD Sheet', cell_overwrite_ok=True)


from operator import itemgetter

test = open("test.tsv").read().strip().split('\n')



rowS = 1

for jj in test:
	t_S = jj.split('\t')[0]
	coll_S = jj.split('\t')[1]

	t_C = jj.split('\t')[2]
	coll_C = jj.split('\t')[3]
	
	p=re.compile(r'\b\W?'+t_S+r'\W?\b ([^\s]+ ){0,3}\b\W?'+coll_S+
                     r'\W?\b|\b\W?'+coll_S+r'\W?\b ([^\s]+ ){0,3}\b\W?'+t_S+r'\W?\b')
	pFR=re.compile(r'\b\W?'+t_C+r'\W?\b ([^\s]+ ){0,3}\b\W?'+coll_C+
                     r'\W?\b|\b\W?'+coll_C+r'\W?\b ([^\s]+ ){0,3}\b\W?'+t_C+r'\W?\b')
	'''
	p=re.compile(r'\b\W?'+t_S+r'\W?\b \b\W?'+coll_S+
                     r'\W?\b|\b\W?'+coll_S+r'\W?\b \b\W?'+t_S+r'\W?\b')
	pFR=re.compile(r'\b\W?'+t_C+r'\W?\b \b\W?'+coll_C+
                     r'\W?\b|\b\W?'+coll_C+r'\W?\b \b\W?'+t_C+r'\W?\b')'''
        
	'''
        p=re.compile(r'\b\W?'+t_S+r'\W?\b \b\W?'+coll_S+
                     r'\W?\b|\b\W?'+coll_S+r'\W?\b \b\W?'+t_S+r'\W?\b')
	pFR=re.compile(r'\b\W?'+t_C+r'\W?\b ([^\s]+ ){0,2}\b\W?'+coll_C+
                     r'\W?\b|\b\W?'+coll_C+r'\W?\b ([^\s]+ ){0,2}\b\W?'+t_C+r'\W?\b')
	'''
	ws.write(rowS+1, 0,t_S)
	ws.write(rowS+1, 1,coll_S)
	ws.write(rowS+1, 4,t_C)
	ws.write(rowS+1, 5,coll_C)

        print t_S
	nbr = 0
	nbr_C = 0
	for sentence in linesEN :
		sentence = sentence.lower()
		
                lemmSentence =' '.join([line.split('\t')[2] for line in [l.strip() 
                                             for l in sentence.strip().split('\n')
                                             if len(sentence.strip()) != 0]])
                notLemmSentence =' '.join([line.split('\t')[0] for line in [l.strip() 
                                         for l in sentence.strip().split('\n') 
                                         if len(sentence.strip()) != 0]])
		if len(notLemmSentence)<311:	
			if p.search(' '.join([ww for ww in lemmSentence.split() if ww not in stop_wordsEN])):
				rowS+=1
				nbr+=1
 				ws.write(rowS, 0,t_S)
				ws.write(rowS, 1,coll_S)
				ws.write(rowS, 4,t_C)
				ws.write(rowS, 5,coll_C)
				ws.write(rowS, 2,nbr)
				ws.write(rowS, 3,notLemmSentence)

		
        
	if nbr ==0: print "Source", t_S,coll_S
	rowC = rowS-max(nbr_C,nbr)
	
	for sen in linesFR :
		sent = sen.lower()
		
                lemmSen =' '.join([lin.split('\t')[2] for lin in [ll.strip() 
                                             for ll in sent.strip().split('\n')
                                             if len(sent.strip()) != 0]])
                notLemmSen =' '.join([lin.split('\t')[0] for lin in [ll.strip() 
                                         for ll in sent.strip().split('\n') 
                                         if len(sent.strip()) != 0]])
		if len(notLemmSen)<311:	
			if pFR.search(' '.join([www for www in lemmSen.split() if www not in stop_wordsFR])):
				nbr_C+=1
				rowC+=1
				ws.write(rowC, 0,t_S)
				ws.write(rowC, 1,coll_S)
				ws.write(rowC, 4,t_C)
				ws.write(rowC, 5,coll_C)
				ws.write(rowC, 6,nbr_C)
				#ws.write(rowC+1, 7,nbr_C)
				ws.write(rowC, 7,notLemmSen)
	if nbr_C ==0: print "Cible", t_C,coll_C
	rowS = max(rowC,rowS)
wb.save('finall.xls')


