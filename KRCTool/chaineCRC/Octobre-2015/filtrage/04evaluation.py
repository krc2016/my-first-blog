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


references = open("../references/references-last-last00.tsv").read().strip()
test = open('../all.tsv').read().strip().split('\n')

stop_wordsFR = open('../stopW/StopWords.txt').read().strip().split('\n')
stop_wordsEN = open('../stopW/StopWordsEN.txt').read().strip().split('\n')

#verifier si la phrase contient une anaphore
def anaphora_sentence(sentence,lang) :# True s'il y a une anaphore
	anaphora=r"^(ils?|elles?|leurs?|cela|ceci|celui|celles?|ceux)|\?"#|ils|elles)"#(il|elle|ils|elles)"
	anaphoraEN=r"^(it|he|she|they|their)|\?"#(il|elle|ils|elles)"
	if lang =='FR': return re.search(anaphora,sentence) != None
	return re.search(anaphoraEN,sentence) != None

def sentence_length(sentence, SW) :
	return len([w for w in sentence.split() if w not in SW])



def complexity(sentence, lang) :
	parsedFR = open("OutFR.txt").read().strip().split('\n')
	parsedEN = open("OutEN.txt").read().strip().split('\n')

	dict_parsedFR = dict([(l.split('\t')[1],l.split('\t')[0]) for l in parsedFR])
	dict_parsedEN = dict([(l.split('\t')[1],l.split('\t')[0]) for l in parsedEN])
	if lang == 'EN': return float(dict_parsedEN[sentence])#/len(sentence.split())
	return float(dict_parsedFR[sentence])#/len(sentence.split())



n = 0
nn = 0
nnn = 0
te = list()
tee = dict()
SommeLn = 0


nC = 0
nnC = 0
nnnC = 0
teC = list()
teeC = dict()

Couples=dict()
tmp = None
tmpN = 0

Change = False
ChangeC = False

for line in test:
	#print test.index(line)
	lineSplit = line.split('\t')
	if len(lineSplit)>7:
		term = lineSplit[0]
		coll = lineSplit[1]
		sentence = lineSplit[3]


		termC = lineSplit[4]
		collC = lineSplit[5]
		sentenceC = lineSplit[7]
		#if term not in tee.keys(): tee[term]=0
#		else : tee[term]['nbrCRC']+=1
					
                #te.append(term)
		
					
		if sentence !='':
#			n+=1
#			SommeLn+= complexity(sentence,"EN")

			#if (complexity(sentence,'FR')>(-238.94)) and (sentence_length(sentence,stop_wordsFR)<=20 and sentence_length(sentence,stop_wordsFR )>=8) and (not anaphora_sentence(sentence)): 
			#if (complexity(sentence,'EN')>(-202.47)) and (sentence_length(sentence,stop_wordsEN)<=20 and sentence_length(sentence,stop_wordsEN )>=9) and (not anaphora_sentence(sentence,'EN')): 
			if complexity(sentence,'EN')>(-202.47):
				nn+=1
			
				if re.search(term+'\t'+coll+r'.+?'+sentence, references):
					#print sentence
					#print term+'\t'+coll+r'.+?'+sentence+'\t0'
					n+=1
				if re.search(term+'\t'+coll+r'.+?'+sentence+'\t1', references):
				#print term+'\t'+coll+'\t'+r'.+?\t'+sentence+'\t0'
					te.append(term)		
					nnn+=1
					



		if sentenceC !='':
			#if (complexity(sentenceC,'FR')>(-238.94)) and (sentence_length(sentenceC,stop_wordsFR)<=20 and sentence_length(sentenceC,stop_wordsFR )>=8) and (not anaphora_sentence(sentenceC,'FR')): 
			if (complexity(sentenceC,'FR')>(-238.94)):
				nnC+=1
			
				if re.search(termC+'\t'+collC+r'.+?'+sentenceC, references):
					#print sentence
					#print term+'\t'+coll+r'.+?'+sentence+'\t0'
					nC+=1
				if re.search(termC+'\t'+collC+r'.+?'+sentenceC+'\t1', references):
				#print term+'\t'+coll+'\t'+r'.+?\t'+sentence+'\t0'
					teC.append(termC)		
					nnnC+=1
					
					#if termC == 'dome':
					#	print "############# ", termC, '#### :',collC
					#	print sentenceC

print "Nbr CRC source :",nn
print "Nbr CRC évalués :", n
print "Nbr CRC :", nnn, float(nnn)/nn
print len(set(te))
#for i in tee.keys() : print i, tee[i]
'''
#for i in sorted(tee.keys()) : print i, tee[i]
#print list(set(te))
print '--------------------'
'''	
print "Nbr CRC Cibles :",nnC
print "Nbr CRC Cibles évalués :", nC
print "Nbr CRC Cibles :", nnnC, float(nnnC)/nnC
print len(set(teC))
'''
#for j in sorted(teeC) : print j, teeC[j]
print
print '###############'
print

#print len(Couples.keys())
print
#for i in l:print i, len(set(Couples[i]['coll']))#," Source :",Couples[i]['Source']," Cible :",Couples[i]['Cible']
#print sum([tee[j] for j in tee.keys()])
for key in sorted(Couples):
	TermeSource = key[0]
	TermeCible = key[1]

	print len(set(Couples[key]['coll'])),
	print TermeSource, TermeCible,sum([tee[key[0],collocS[0]] for collocS in set(Couples[key]['coll'])]),
	print  sum([teeC[key[1],colloca[1]] for colloca in set(Couples[key]['coll'])])

	for colocations in set(Couples[key]['coll']):
		print '       ',colocations,  tee[key[0],colocations[0]], teeC[key[1],colocations[1]]


	print Couples[key]['Source'],"|", sum([tee[key[0],colloc[0]] for colloc in set(Couples[key]['coll'])]), "[]",
	print Couples[key]['Cible'],"|",sum([teeC[key[1],colloca[1]] for colloca in set(Couples[key]['coll'])])
	


'''	
