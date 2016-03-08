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


references = open("references/references-last-last00.tsv").read().strip()
test = open('all.tsv').read().strip().split('\n')

n = 0
nn = 0
nnn = 0
te = list()
for line in test:
	#print test.index(line)
	lineSplit = line.split('\t')
	if len(lineSplit)>7:
		term = lineSplit[4]
		coll = lineSplit[5]
		sentence = lineSplit[7]
                te.append(term)
		if sentence !='': 
			nn+=1
			
			if re.search(term+'\t'+coll+r'.+?'+sentence, references):
				
				#print term+'\t'+coll+r'.+?'+sentence+'\t0'
				n+=1
			if re.search(term+'\t'+coll+r'.+?'+sentence+'\t1', references):
			#print term+'\t'+coll+'\t'+r'.+?\t'+sentence+'\t0'		
				nnn+=1
print "Nbr CRC source :",nn
print "Nbr CRC évalués :", n
print "Nbr CRC :", nnn, float(nnn)/nn
print len(set(te))
print list(set(te))
