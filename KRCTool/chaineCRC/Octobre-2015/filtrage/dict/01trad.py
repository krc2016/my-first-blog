#!/usr/bin/env python
# -*- coding: utf-8 -*-
##########################################################
### Autor name : 		Firas Hmida		##
### Date de création :		04-06-2015		##
### Date de modification : 	10-06-2015		##
### Contenu : 			similar_examples	##
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
from nltk.tokenize.punkt import PunktSentenceTokenizer
from nltk.collocations import BigramCollocationFinder


'''
tempFR = [ lineFR for lineFR in linesFR]
fr = [lfr.strip().split('\n') for lfr in tempFR]
dictLemmFR = dict()
for i in fr:
	notLemmSentenceFR = ' '.join([ii.split('\t')[0] for ii in i if len(ii.split('\t'))>2])
	
	lemmSentenceFR =  ' '.join([ii.split('\t')[2] for ii in i if len(ii.split('\t'))>2])
	dictLemmFR[notLemmSentenceFR]=lemmSentenceFR
	
tempEN = [ lineEN for lineEN in linesEN]
en = [lEN.strip().split('\n') for lEN in tempEN]
dictLemmEN = dict()
for j in en:
	notLemmSentenceEN = ' '.join([jj.split('\t')[0] for jj in j if len(jj.split('\t'))>2])
	
	lemmSentenceEN =  ' '.join([jj.split('\t')[2] for jj in j if len(jj.split('\t'))>2])
	dictLemmEN[notLemmSentenceEN]=lemmSentenceEN
	
pickle.dump(dictLemmFR,open('dictSentenceLemmFR.p', 'wb'))
pickle.dump(dictLemmEN,open('dictSentenceLemmEN.p', 'wb'))
'''

def main():
	if len(sys.argv) <3 :
		sys.stderr.write("Usage: python preprocess.py [Corpus] [outCorpus]\n")
        	sys.exit(1)
	else:
		sourceSentences = pickle.load(open(sys.argv[1], 'rb'))
		targetSentences = pickle.load(open(sys.argv[2], 'rb'))

		wordsSource = itertools.chain.from_iterable([w.split() for i in sourceSentences.keys() for w in sourceSentences[i]['lemmSentence']])
		wfdSource = FreqDist([wds for wds in wordsSource])	


		wordsTarget = itertools.chain.from_iterable([w.split() for i in targetSentences.keys() for w in targetSentences[i]['lemmSentence']])
		wfdTarget = FreqDist([wdt for wdt in wordsTarget])


#		wordsSource = itertools.chain.from_iterable([w.split() for i in sourceSentences.keys() for w in sourceSentences[i]['lemmSentence']])
#		wordsS = list(set([wd for wd in wordsSource]))
#		wordsTarget = itertools.chain.from_iterable([w.split() for i in targetSentences.keys() for w in targetSentences[i]['lemmSentence']])
#		wordsT = list(set([wwd for wwd in wordsTarget]))		

		dicTrad = open('couples.tsv').read().strip().split('\n')

		#wfdSource = FreqDist([w for w in wordsSource])
		#wfdTarget = FreqDist([w for w in wordsTarget])

		couplesTrad = [(line.split('\t')[0], line.split('\t')[1]) for line in dicTrad]
		couplesTrad = dict(couplesTrad)
	
		#dictionnaire = open('EN-FR-ELRA').read().strip().split('\n')
		dictBilingue = pickle.load(open('dictBilingue.p', 'rb'))
		stopWords = open("stopW/StopWordsEN.txt").read().strip().split('\n')
		stopWordsFR = open("stopW/StopWords.txt").read().strip().split('\n')

		'''
		'''
		for termSource in sourceSentences.keys()[5:6] :
			print "########################################################"
			print "#######################",termSource,
			sourceLemmSentences = sourceSentences[termSource]['lemmSentence']
			sourceNotLemmSentences = sourceSentences[termSource]['notLemmSentence']
			targetTerm = couplesTrad[termSource]
			#print "######### Couple traduction ####### ", 
			print targetTerm

			targetLemmSentences = targetSentences[targetTerm]['lemmSentence']
			targetNotLemmSentences = targetSentences[targetTerm]['notLemmSentence']


			print len(sourceLemmSentences), len(targetLemmSentences)
	
			nbr = 0
			for indice  in range(min(len(sourceLemmSentences),500)):
				sourceLemmSent = sourceLemmSentences[indice]
				sourceNotLemmSent = sourceNotLemmSentences[indice]
				sentTrans = [dictBilingue[w][0] for w in sourceLemmSent.split() if w in dictBilingue.keys() and w not in stopWords]

		
				#allpossible = [poss for poss in itertools.product(*sentTrans)]
				#print "allposs :",len(allpossible)
		
#				if set(allpossible).intersection(set(targetLemmSentences: print True
				for indice_target in range(min(len(targetLemmSentences),500)):
					tarSent = targetLemmSentences[indice_target]
					targ = targetNotLemmSentences[indice_target]
					tarSent = [ww for ww in tarSent.split() if ww not in stopWordsFR]
					#if ((len(set(sentTrans).intersection(set(tarSent)))/float(max(len(sentTrans),len(tarSent)))) > 0.4) or ((len(set(re.findall(r'[0-9]{1,10}',targ)).intersection(set(re.findall(r'[0-9]{3,10}',sourceNotLemmSent))))>0) and ((abs(len(targ.split())-len(sourceNotLemmSent.split()))/float(max(len(targ.split()),len(sourceNotLemmSent.split()))))>0.77)) :

					if (len(set(re.findall(r'[0-9]{4}',targ)).intersection(set(re.findall(r'[0-9]{4}',sourceNotLemmSent))))>0) :
						nbred = re.findall(r'[0-9]{4}',targ)
						for nbre in nbred:
							if re.findall(nbre,sourceNotLemmSent):


								nbr+=1
						
								print "------- Source ----------\n", sourceNotLemmSent#tarSent
							
								print "------- Target ----------\n", targetNotLemmSentences[indice_target]#NotLemmSent[indice]#sentTrans
								if nbr == 3: continue
						
			print nbr
	'''		
	'''

#			for termSen in termSentences :
				



		#sentences=PunktSentenceTokenizer().tokenize(corpus)
		DictSentences = dict()
		for termSource in couples :
			termSource = termSource[1]
			print termSource,
			DictSentences[termSource] = dict()
			DictSentences[termSource]['lemmSentence'] = list()
			DictSentences[termSource]['notLemmSentence'] = list()
			pattern = re.compile(r'\b\W?'+termSource+r'\W?\b')
			nbr = 0
			for sentence in corpusEn :
				#if pattern.search(sentence):
				sentence = sentence.lower()
	
				lemmSentence =' '.join([line.split('\t')[2] for line in [l.strip() for l in sentence.strip().split('\n') if len(sentence.strip()) != 0] if len(line.split('\t'))==3])

				notLemmSentence =' '.join([line.split('\t')[0]
				for line in [l.strip() for l in sentence.strip().split('\n') if len(sentence.strip()) != 0]])
	
				if pattern.search(lemmSentence):
					DictSentences[termSource]['lemmSentence'].append(lemmSentence)
					DictSentences[termSource]['notLemmSentence'].append(notLemmSentence)
					nbr+=1
					#print notLemmSentence
					#print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
			print nbr
		pickle.dump(DictSentences, open('targetDictSentences.p', 'wb'))
	
if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print "Time spent = {:.2f} seconds.".format(
          end_time - start_time)
