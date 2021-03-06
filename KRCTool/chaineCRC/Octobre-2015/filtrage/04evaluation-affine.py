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
termCollDictS = dict()
SommeLn = 0


nC = 0
nnC = 0
nnnC = 0
teC = list()
termCollDictC = dict()

Couples=dict()
tmp = None
tmpN = 0

Change = False
ChangeC = False

allo = 0
oulala = dict()
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


			if True:#(complexity(sentence,'EN')>(-202.47)) and (sentence_length(sentence,stop_wordsEN)<=20 and sentence_length(sentence,stop_wordsEN )>=9) and (not anaphora_sentence(sentence,'EN')): 

				nn+=1
			
				if re.search(term+'\t'+coll+r'.+?'+sentence, references):

					n+=1
				if re.search(term+'\t'+coll+r'.+?'+sentence+'\t1', references):
					te.append(term)		
					nnn+=1
					if (term,coll) not in termCollDictS.keys(): termCollDictS[(term,coll)]=[sentence]
					else : termCollDictS[(term,coll)].append(sentence)
					Change = True


					if (term,termC,coll,collC) not in oulala.keys():
						oulala[term,termC,coll,collC]=dict()
						oulala[term,termC,coll,collC]['Source']=[sentence]
						oulala[term,termC,coll,collC]['Cible']=[]
					else:oulala[term,termC,coll,collC]['Source'].append(sentence)

		if sentenceC !='':
			if True:#(complexity(sentenceC,'FR')>(-238.94)) and (sentence_length(sentenceC,stop_wordsFR)<=20 and sentence_length(sentenceC,stop_wordsFR )>=8) and (not anaphora_sentence(sentenceC,'FR')): 

				nnC+=1
			
				if re.search(termC+'\t'+collC+r'.+?'+sentenceC, references):
					
					nC+=1
				if re.search(termC+'\t'+collC+r'.+?'+sentenceC+'\t1', references):
					teC.append(termC)		
					nnnC+=1
					if (termC,collC) not in termCollDictC.keys(): termCollDictC[(termC,collC)]=[sentenceC]
					else : termCollDictC[(termC,collC)].append(sentenceC)
					ChangeC = True

					if (term,termC,coll,collC) not in oulala.keys():
						oulala[term,termC,coll,collC]=dict()
						oulala[term,termC,coll,collC]['Cible']=[sentenceC]
						oulala[term,termC,coll,collC]['Source']=[]
					else:oulala[term,termC,coll,collC]['Cible'].append(sentenceC)


		couple = (coll,collC)
		if (term,coll) in termCollDictS.keys() and (termC,collC) in termCollDictC.keys():
				if (term,termC) in Couples.keys():
					Couples[(term,termC)]['coll'].append(couple)
					if Change : 
						Couples[(term,termC)]['Source']+=1#tee[(term,coll)]
					#print tee[(term,coll)]
					if ChangeC:
						Couples[(term,termC)]['Cible'] += 1#teeC[(termC,collC)]
				else : 
					Couples[(term,termC)]=dict()
					Couples[(term,termC)]['coll']=list()
					Couples[(term,termC)]['coll'].append(couple)
					Couples[(term,termC)]['Source'] =0
					Couples[(term,termC)]['Cible'] =0
					if Change :
						Couples[(term,termC)]['Source']=1#tee[(term,coll)]
						#Couples[(term,termC)]['Cible'] =0#teeC[(termC,collC)]
					if ChangeC:			
						#Couples[(term,termC)]['Source']=0#tee[(term,coll)]
						Couples[(term,termC)]['Cible'] =1
	Change,ChangeC = False,False
print '######## MONOLINGUE #######'

print "Nbr CRC source :",nn
print "Nbr CRC évalués :", n
print "Nbr CRC :", nnn, float(nnn)/nn
print "Nbr termes Sources :",len(set(te))
#for i in sorted(termCollDictS.keys()) : print i, len(termCollDictS[i])


print '--------------------'
	
print "Nbr CRC Cibles :",nnC
print "Nbr CRC Cibles évalués :", nC
print "Nbr CRC Cibles :", nnnC, float(nnnC)/nnC
print "Nbr termes Cibles :", len(set(teC))

#for j in sorted(termCollDictC) : print j, len(set(termCollDictC[j]))
print
print '######## BILINGUE #######'
print

#for i in l:print i, len(set(Couples[i]['coll']))#," Source :",Couples[i]['Source']," Cible :",Couples[i]['Cible']
#print sum([tee[j] for j in tee.keys()])


nbrColl=0
nbrSource = 0
nbrCible = 0
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

pickle.dump(Couples, open('Couples.p', 'wb'))
pickle.dump(oulala, open('dicDetails.p', 'wb'))

print "-------------------"
print "Nbr Termes alignés :", len(Couples.keys())
print "Nbr Collocations :",nbrColl
print "Nbr Sources alignées :", nbrSource, " | {:.2f} %".format((float(nbrSource)/nn)*100)
print "Nbr Cibles alignées :", nbrCible, " | {:.2f} %".format((float(nbrCible)/nnC)*100)

'''	
print "-------------------"
print "Gas, Gaz ",
for ii in (set(Couples[('gas','gaz')]['coll'])):
	print ii
'''

'''
s=0
for i in tee.keys(): 
	print i, tee[i]
'''	
