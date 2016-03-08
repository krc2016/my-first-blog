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

Couples = pickle.load(open('Couples.p', 'rb'))
	  
oulala = pickle.load(open('dicDetails.p', 'rb'))

#verifier si la phrase contient une anaphore

def sentence_length(sentence, SW) :
	return len([w for w in sentence.split() if w not in SW])

def lenSim(sentenceS, sentenceC):
	return min(sentence_length(sentenceS,stop_wordsEN)/float(sentence_length(sentenceC,stop_wordsFR)), float(sentence_length(sentenceC,stop_wordsFR)/sentence_length(sentenceS,stop_wordsEN)))

def posTerm(sentence,term,ST):
	#return sentence.index(term)
	try:
		return [w for w in sentence.split() if w not in ST].index(term)/float(len([w for w in sentence.split() if w not in ST]))
	except ValueError: return [i for i in range(len([w for w in sentence.split() if w not in ST])) if term in [w for w in sentence.split() if w not in ST][i]][0]/float(len([w for w in sentence.split() if w not in ST]))
	
def NbrTerm(sentence,listTerm):
	return len([w for w in sentence.split() if w in listTerm])

corpusEN = open('../corpus/vulcanoEN-POS.txt').read()
corpusFR = open('../corpus/vulcanoPOS.txt').read()
def lemmatiser(sentence,corpus,SW):
	return [re.findall(r'\n'+w.replace('#','')+'	.+?	(.+?)\n',corpus) for w in sentence.split() if w not in SW]

def translate(sentence, corpus, SW):	
	dictBilingue = pickle.load(open('dict/dictBilingue.p', 'rb'))
	return [dictBilingue[w][0] for w in lemmatiser(sentence, corpus, SW) if w in dictBilingue.keys()]
	#(len(set(sentTrans).intersection(set(tarSent)))/float(max(len(sentTrans),len(tarSent)))) > 0.4)
	


nbrColl = 0
nbrSource = 0
nbrCible = 0
for key in sorted(Couples):
	TermeSource = key[0]
	TermeCible = key[1]

	print key[0], key[1]

print "----------------------"
Dict = [(t.split('\t')[0],t.split('\t')[1]) for t in open("../EN-FR-ELRA").read().strip().split('\n')]

'''

for couple in sorted(oulala.keys()):
	sentencesS = oulala[couple]['Source']
	sentencesC = oulala[couple]['Cible']
	nbr = 0
	if len(sentencesS)!=0 and len(sentencesC)!=0:
		#print couple, len(oulala[couple]['Source']),len(oulala[couple]['Cible'])
		termS = couple[0]
		termC = couple[1]
		collS = couple[2]
		collC = couple[3]
		oulala[couple]['aligner']=[]
		oulala[couple]['SA'] = []
		oulala[couple]['CA'] = []
		for sentenceS in sentencesS:
			#lemmatiser(sentenceS,corpusEN,stop_wordsEN)
			#sentTrans = translate(sentenceS,corpusEN,stop_wordsEN)
			for sentenceC in sentencesC:
				minPos = min(posTerm(sentenceS,termS,stop_wordsEN),
					posTerm(sentenceC,termC,stop_wordsFR))
				maxPos = max(posTerm(sentenceS,termS,stop_wordsEN),
					posTerm(sentenceC,termC,stop_wordsFR))
				if maxPos == 0: maxPos=1
				#if (len(set(sentTrans).intersection(set(sentenceC)))/float(max(len(sentTrans),len(sentenceC)))) > 0:lenSim(sentenceS,sentenceC)>=0.8:# and
				if  lenSim(sentenceS,sentenceC)>=0.8 and (minPos/float(maxPos))>=0.8:
					oulala[couple]['aligner'].append((sentenceS,sentenceC))
					oulala[couple]['SA'].append(sentenceS)
					oulala[couple]['CA'].append(sentenceC)
					nbr+=1
					#print sentTrans
			
		if nbr + len(set(oulala[couple]['SA'])) + len(oulala[couple]['aligner']) +len(set(oulala[couple]['CA'])) >0: 
			print couple, len(oulala[couple]['aligner'])
			#print len(set(oulala[couple]['SA'])), len(set(oulala[couple]['CA']))
			
			print 	oulala[couple]['aligner'][0][0]
			print '------------'
			print oulala[couple]['aligner'][0][1]
			
	
	
'''		

'''
for key in sorted(Couples):
	TermeSource = key[0]
	TermeCible = key[1]

	print len(set(Couples[key]['coll'])),
	print TermeSource, TermeCible,#sum([ len(set(termCollDictS[key[0],colloc[0]])) for colloc in set(Couples[key]['coll'])]),
	#print  sum([len(set(termCollDictC[key[1],colloc[1]])) for colloc in set(Couples[key]['coll'])])

	print sum([len(oulala[key[0],key[1],colo[0],colo[1]]['Source']) for colo in set(Couples[key]['coll'])]),
	print sum([len(oulala[key[0],key[1],colo[0],colo[1]]['Cible']) for colo in set(Couples[key]['coll'])])

	nbrColl+= len(set(Couples[key]['coll']))
	nbrSource+= sum([len(oulala[key[0],key[1],colo[0],colo[1]]['Source']) for colo in set(Couples[key]['coll'])])
	nbrCible+= sum([len(oulala[key[0],key[1],colo[0],colo[1]]['Cible']) for colo in set(Couples[key]['coll'])])
'''
'''
print "-------------------"
print "Nbr Termes alignés :", len(Couples.keys())
print "Nbr Collocations :",nbrColl
print "Nbr Sources alignées :", nbrSource
print "Nbr Cibles alignées :", nbrCible
'''


