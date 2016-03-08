#!/usr/bin/env python
# -*- coding: utf-8 -*-
##########################################################################
### Autor name : 		Firas HMIDA				##
### Adresse :			firas.hmida@univ-nantes.fr		##
### Date de création :		21-07-2014				##
### Date de modification : 	22-07-2014		          	##
### Contenu : 			Baseline : linguistic-collocations	##
##########################################################################
import re
import os
import sys
import time
import nltk
import pickle
import itertools
from math import *
from nltk.collocations import *
from operator import itemgetter
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.metrics import BigramAssocMeasures
from nltk.tokenize.regexp import RegexpTokenizer
from nltk import word_tokenize, wordpunct_tokenize
from nltk.collocations import BigramCollocationFinder



#defined_terms = open('termsCible.txt','r').read().lower().strip().split('\n')

#lines = list(set(open('corpus/vulcanoPOS.txt').read().strip().split('.	SENT	.')))
reference = open("corpus/vulcanoFR.txt").read().strip()


for file_ in os.listdir('outCRC'):
    fich= open('outCRC/'+file_,'r').read().strip().split('\n')
    out = open('outBrutCRC/'+file_,'w')
    print file_
    for line in fich:
        term = line.strip().split('\t')[0]
        coll = line.strip().split('\t')[1]
        context = line.strip().split('\t')[2]
        inf2 = line.strip().split('\t')[3]
        inf3 = line.strip().split('\t')[4]
        inf4 = line.strip().split('\t')[5]
        inf5 = line.strip().split('\t')[6]
	


        sentence = re.sub('\?','\?', context)
	sentence = re.sub('\*','\*', sentence)
        sentence = re.sub(term,term.lower(),sentence)
       
        if re.search(term.upper()+'S',sentence): sentence = re.sub(term.upper()+'S',term.lower()+'s',sentence)
        elif re.search(term.upper(),sentence): sentence = re.sub(term.upper(),term.lower(),sentence)

        sentence = re.sub('<term>|</term>','',sentence)
        #sentence = re.sub('','',sentence)
        patron = re.sub(r'\[','\[', sentence)
        patron = re.sub(r'\]','\]',patron)
	patron = re.sub(r'\+','\+',patron)
	
        brut = re.findall(re.sub(' ','.{0,5}',patron), reference,re.IGNORECASE)
        print term, len(set(brut))
	
        for sentBrut in list(set(brut)):
            out.write(term+'	'+coll+'	')
            try:
                           		
                out.write(re.sub(re.findall(term+'s?',sentBrut)[0],'<term>'+re.findall(term+'s?',sentBrut)[0].upper()+'</term>',sentBrut)+'	')

            except IndexError:
                out.write(sentBrut+'	')
                

            out.write(inf2+'	'+inf3+'	'+inf4+'	'+inf5+'	\n')

out.close()
        #if len(brut)<1:
            #print patron
        #print re.sub(' ','.*?',patron)
#lines = list(set(open('amelieFR.txt').read().lower().strip().split('\n')))


'''
for term in defined_terms:
	term = term.split('\t')[2]
	print term

	n = 0

	p = re.compile(term)
	for sentence in lines :
		

		lemmSentence =' '.join([line.split('\t')[2] for line in [l.strip() 
       	                                     for l in sentence.strip().split('\n')
       	                                     if len(sentence.strip()) != 0]])
       	        notLemmSentence =' '.join([line.split('\t')[0] for line in [l.strip() 
       	                                 for l in sentence.strip().split('\n') 
       	                                 if len(sentence.strip()) != 0]])
		
		if p.search(lemmSentence.lower()):
			
			markers=open('hyper.txt','r').read().strip().split('\n')
			
			for mark in markers:
				mark = re.sub("Y",term,mark)
				mark = re.sub('X','.+?', mark)
				#mark = re.sub('\n','|',mark)
				mark = re.sub('ADJ',r'.+?',mark)
				#mark = '('+mark+')'
				#print mark
				#print "------------"
				pattern = re.compile(mark.lower())
				

				if pattern.search(lemmSentence) or pattern.search(notLemmSentence):
					n+=1
					#print mark
					#out.write(term+'	'+notLemmSentence+'	'+str(n)+'	'+MARQ+'	'+corpus+'\n')
					aa = notLemmSentence
					begin = notLemmSentence.split()[0]
					end   = notLemmSentence.split()[len(notLemmSentence.split())-1]
					notLemmSentence = re.sub('\?','\?',notLemmSentence)
					notLemmSentence = re.sub('\*','\*',notLemmSentence)
					#patron = re.sub(' ','.*?',notLemmSentence)#.join([word for word in notLemmSentence.split()])

					patron = re.sub(r'\[','\[',notLemmSentence)
					patron = re.sub(r'\]','\]',patron)
					patron = re.sub(r'\+','\+',patron)
					#print patron
					#print '-----------------'		
					brut = re.findall(re.sub(' ','.*?',patron), reference)#begin+'.+?'+term+r'.+?'+end,reference)		
					if len(brut) <1:
						print "-----ERROR : not found ----"
						print aa# re.sub(' ','.*?',patron)
					print len(set(brut)),
					
					#if len([ww for ww in notLemmSentence.split() is in br
	
					try:

						for sen in brut:
							sen = re.sub(re.findall(term+'s?',sen)[0],'<term>'+re.findall(term+'s?',sen)[0].upper()+'</term>',sen)
							out.write(term+'	'+sen+'	'+str(n)+'	'+MARQ+'	'+corpus+'\n')

					except IndexError:
						out.write(term+'	'+notLemmSentence+'	'+str(n)+'	'+MARQ+'	'+corpus+'\n')
	


	print n
out.close()



'''

	
	
	

	
