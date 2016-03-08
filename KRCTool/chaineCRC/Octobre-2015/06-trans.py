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

linesEN = list(set(open('../corpus/vulcanoEN-POS.txt').read().strip().split('.	SENT	.')))
linesFR = list(set(open('../corpus/vulcanoPOS.txt').read().strip().split('.	SENT	.')))

dictLemmFR = pickle.load(open('dictSentenceLemmFR.p', 'rb'))
dictLemmEN = pickle.load(open('dictSentenceLemmEN.p', 'rb'))

dictBilingue = pickle.load(open('dict/dictBilingue.p', 'rb'))
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


def lemmatiser(sentence,lang):
	try:
		if lang == 'FR': return [wfr for wfr in dictLemmFR[sentence].split() if wfr not in stop_wordsFR and len(wfr)>1]
		return [wen for wen in dictLemmEN[sentence].split() if wen not in stop_wordsEN and len(wen)>1]
	except KeyError : return [wen for wen in dictLemmEN['* '+sentence].split() if wen not in stop_wordsEN and len(wen)>1] #print sentence

def translate(sentence, lang):
	return [dictBilingue[w][0] for w in lemmatiser(sentence, lang) if w in dictBilingue.keys()]
	
	#(len(set(sentTrans).intersection(set(tarSent)))/float(max(len(sentTrans),len(tarSent)))) > 0.4)

def translated_terms(sentence,lang, termsList):
	return [dictBilingue[word][0] for word in lemmatiser(sentence,lang) if word in termsList and word in dictBilingue.keys()]

def cognate(sentenceSource, sentenceCible):
	return len([wS for wS in sentenceSource for  wC in sentenceCible if wS[:4]==wC[:4]])

termsEN = open('../terminologie-vulcano/terminoEN.txt').read().strip().split('\n')
termsFR = open('../terminologie-vulcano/terminoFR.txt').read().strip().split('\n')
nbrColl = 0
nbrSource = 0
nbrCible = 0
for key in sorted(Couples):
	TermeSource = key[0]
	TermeCible = key[1]

	print key[0], key[1]


#for i in ([ff for ff in dictLemmEN.keys() if '26 september 1995 , p.1 volcano emergency alert' in ff ]): print i
print "----------------------"
Dict = [(t.split('\t')[0],t.split('\t')[1]) for t in open("../EN-FR-ELRA").read().strip().split('\n')]
from difflib import SequenceMatcher

resfinal = dict()

File = open('alignedCouples.csv','w')
File.write('Terme	Collocatif	PhraseS	Terme	Collocatif	PhraseC	Critere\n')

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
		oo,tt,ttt = False,False, False
		for sentenceS in sentencesS:
			lemmS = lemmatiser(sentenceS,'EN')
			sentTrans = translate(sentenceS,'EN')
			transTerm = translated_terms(sentenceS,'EN',termsEN)
			#print transTerm
			for sentenceC in sentencesC:
				Cibsent = lemmatiser(sentenceC,'FR')
				#sentenceS = "modern skills in predicting eruptions go back to the aftermath of the cataclysmic eruption of mount st helens in washington state in 1980"
				#sentenceC = "21 ans après l éruption cataclysmique du mont saint helens , des milliers de troncs d arbres flottent toujours à la surface du lac spirit"
			
				#try: xx = len([w for w in lemmS if (w in termsEN and w!=termS) and w!=collS])/float(len(lemmS)) / len([ww for ww in Cibsent if (ww in termsFR and ww!=termC) and ww!=collC])/float(len(Cibsent)) >0.9
				#except ZeroDivisionError: xx = False
				#if xx	:
#				if NbrTerm(sentenceS,termsEN)/float(len(sentenceS.split()))/NbrTerm(sentenceC,termsFR)/float(len(sentenceC.split()))>0.9:
				
				if (len([wS for wS in sentenceS.split() for  wC in sentenceC.split() if (len(wS)>3 and len(wC)>3 ) and (wS.lower()[:4]==wC.lower()[:4]) and (len(wS)==len(wC)) and 
				(wS.lower() != termS and wS.lower() != collS) and (wC.lower()!=termC and wC.lower()!=collC) and (SequenceMatcher(None, wS.lower(), wC.lower()).ratio() >= 0.7)])>0) or (len([Ws for Ws in transTerm if Ws in Cibsent if ((Ws != termC and Ws != collC) and (Ws !=','))] )>1):
#					oo = True
#				if len([Ws for Ws in transTerm if Ws in Cibsent if ((Ws != termC and Ws != collC) and (Ws !=','))] )>1:#nbr+=1
#						tt = True
#						if len([wS for wS in sentenceS.split() if (wS in sentenceC.split() and wS not in stop_wordsEN) and (wS != termS and wS != collS and len(wS)>1)])>0:#nbr+=1
#							ttt=True	
				#if (len(set(sentTrans).intersection(set(Cibsent)))/float(max(len(sentTrans),len(Cibsent)))) > 0.2 and len(sentenceS.split())>2: 
					#if (oo and tt) and ttt:
					File.write(termS+'\t'+collS+'\t'+sentenceS+'\t'+termC+'\t'+collC+'\t'+sentenceC+'\t')
					if (len([wS for wS in sentenceS.split() for  wC in sentenceC.split() if (len(wS)>3 and len(wC)>3 ) and (wS.lower()[:4]==wC.lower()[:4]) and (len(wS)==len(wC)) and 
				(wS.lower() != termS and wS.lower() != collS) and (wC.lower()!=termC and wC.lower()!=collC) and (SequenceMatcher(None, wS.lower(), wC.lower()).ratio() >= 0.7)])>0):
						File.write(('|'.join([wS for wS in sentenceS.split() for  wC in sentenceC.split() if (len(wS)>3 and len(wC)>3 ) and (wS.lower()[:4]==wC.lower()[:4]) and (len(wS)==len(wC)) and 
				(wS.lower() != termS and wS.lower() != collS) and (wC.lower()!=termC and wC.lower()!=collC) and (SequenceMatcher(None, wS.lower(), wC.lower()).ratio() >= 0.7)]))+'\t')
					if (len([Ws for Ws in transTerm if Ws in Cibsent if ((Ws != termC and Ws != collC) and (Ws !=','))] )>1):
						File.write(('|'.join([Ws for Ws in transTerm if Ws in Cibsent if ((Ws != termC and Ws != collC) and (Ws !=','))]))+'\t')
					File.write('\n')
				
					'''if termS == 'volcan':
					
						print '------------------------- SOURCE ----------------------'
						print sentenceS
						print '------------------------- CIBLE  ------------------'
						print sentenceC
						print '########## VERCTEUR #############'
					
						print [Ws for Ws in transTerm if Ws in Cibsent if ((Ws != termC and Ws != collC) and (Ws !=','))]
					#print '##### ' ,termS, termC
						#print [wS for wS in sentenceS.split() for  wC in sentenceC.split() if (len(wS)>3 and len(wC)>3 ) and (wS.lower()[:4]==wC.lower()[:4]) and (wS.lower() != termS and wS.lower() != collS) and (wC.lower()!=termC and wC.lower()!=collC)and (SequenceMatcher(None, wS.lower(), wC.lower()).ratio() >= 0.7)]'''
					nbr+=1
		if nbr>0:
			print couple, len(oulala[couple]['Source']),len(oulala[couple]['Cible']), '[', nbr,' ]'
			if termS in resfinal.keys():
				resfinal[termS]['Align']+=nbr
				resfinal[termS]['Coll'].append((collS,collC))
			else: 
				resfinal[termS]=dict()
				resfinal[termS]['Align']=nbr
				resfinal[termS]['Coll']=[(collS,collC)]
File.close()
aaa = 0
bbb = 0
for key in sorted(resfinal.keys()):
	print key, len(resfinal[key]['Coll']), resfinal[key]['Align']
	aaa+=len(resfinal[key]['Coll'])
	bbb+=resfinal[key]['Align']
	
print aaa, bbb

'''
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


