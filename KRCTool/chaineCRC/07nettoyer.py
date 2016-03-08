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
terms = open('termsFR.txt').read().strip().split('\n')
termFR = sys.argv[1]

phrases = dict()
alldic = dict()
out = open("CRCbrut.tsv",'w')
#out.write('Terme	Identifiant_CRC	CRC	Position_terme	Nom_corpus	Type_CRC	Collocatif	Nb_autres_termes	Liste_autres_termes	Champs_vide_1	champs_vide_2\n')
for file_ in os.listdir('FR'):
    fich= open('FR/'+file_,'r').read().strip().split('\n')
    
    print file_
    
    for line in fich:
        '''
        term = line.strip().split('\t')[0]
        context = line.strip().split('\t')[1]
        indice = line.strip().split('\t')[2]
        type_c = line.strip().split('\t')[3]
        corpus = line.strip().split('\t')[4]
        #inf4 = line.strip().split('\t')[5]
        #inf5 = line.strip().split('\t')[6]
	'''
	
       
	#print line.split('\t')
	#print'------------'
        term = line.strip().split('\t')[0]
        colloc = line.strip().split('\t')[1]
        context = line.strip().split('\t')[2]
        indice = line.strip().split('\t')[3]
        type_c = line.strip().split('\t')[5]
        corpus = line.strip().split('\t')[6]
        #inf4 = line.strip().split('\t')[5]
        #inf5 = line.strip().split('\t')[6]


        if term not in phrases.keys():
	        phrases[term]=[]
	        alldic[term] = []

        sentence = re.sub('\?','\?', context)
	sentence = re.sub('\*','\*', sentence)
        sentence = re.sub(term.upper(),term.lower(),sentence)
        sentence = re.sub(term.upper()+'S',term.lower()+'s',sentence)
        sentence = re.sub(term.lower()+'S',term.lower()+'s',sentence)
        #sentence = sentence.lower()
        sentence = re.sub('<term>|</term>','',sentence)
	s = sentence
        sentence = re.sub('','',sentence)
        
        sentence = re.sub(term+r'es\b','<term>'+term+'es'+'</term>',sentence,re.IGNORECASE)
        sentence = re.sub(term+r's\b','<term>'+term+'s'+'</term>',sentence,re.IGNORECASE)
        sentence = re.sub(term+r'e\b','<term>'+term+'e'+'</term>',sentence,re.IGNORECASE)
        sentence = re.sub(term+r'\b','<term>'+term+'</term>',sentence,re.IGNORECASE)



        sentence = re.sub(term.upper()+r'ES\b','<term>'+term.lower()+'es'+'</term>',sentence,re.IGNORECASE)
        sentence = re.sub(term.upper()+r'S\b','<term>'+term.lower()+'s'+'</term>',sentence,re.IGNORECASE)
        sentence = re.sub(term.upper()+r'E\b','<term>'+term.lower()+'e'+'</term>',sentence,re.IGNORECASE)
        sentence = re.sub(term.upper()+r'\b','<term>'+term.lower()+'</term>',sentence,re.IGNORECASE)
        
	#print sentence
       


	sent = re.sub(term,re.sub(' ','_',term),s)


        

	try:
            indd= sentence.split().index([i for i in sentence.split() if re.search(term,i,re.IGNORECASE)][0])+1
          



        except IndexError:
            print '--------------------------> ERROR :', term
            indd = '---'

        if sentence.lower() not in phrases[term]:
            phrases[term].append(sentence.lower())
            termsin = [w for w in terms if re.search(w+r's?\b',re.sub('(,|\?|\!\)|\(|<term>|</term>)',' ',sentence.lower())) and w != term]
            alldic[term].append((sentence,indd,corpus,type_c,colloc,len(set(termsin)),':'.join(list(set(termsin))),'',''))
	    #print indd
            #print 'one context added'
           
            
        #print len(phrases[term])
	#print sentence
	#print 'rrrrr'
pos = 0
for t in sorted(alldic.keys()): 
	#print t, len(alldic[t]), len(phrases[t])
        ind = 1
	for crc in alldic[t]:
            out.write(t+'	'+str(ind)+'	'+crc[0]+'	'+str(crc[1])+'	'+crc[2]+'	'+crc[3]+'	'+crc[4]+'	'+str(crc[5])+'	'+crc[6]+'	'+crc[7]+'	\n')
	    ind+=1
            pos+=1
            if  (str(crc[1]) == '---'): print t, pos
out.close()
#Terme	Identifiant_CRC	CRC	Position_terme	Nom_corpus	Type_CRC	Collocatif	Nb_autres_termes	liste_autres_termes	Champs_vide_1	champs_vide_2
	
