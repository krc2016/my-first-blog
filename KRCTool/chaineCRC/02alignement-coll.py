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



def main():
    collocationsSource = pickle.load(open('outCollocations/collocationLemmaPropEN.p','rb'))
    collocationsCible = pickle.load(open('outCollocations/collocationLemmaPropFR.p','rb'))

    dico = [(t.split('\t')[0],t.split('\t')[1]) for t in open("dictionnaries/EN-FR-ELRA").read().strip().split('\n')]
    
    traductionList={sys.argv[2]:sys.argv[1]}

    out = open('test.tsv','w')
    for c in sorted(collocationsSource.keys()):

       
       
        node  = re.sub('_',' ',c)
        node    = re.sub("\A[()\,\.\?']|[()\,\.\?']$","",node)

        nodeCible = traductionList[node]
        
        col_listSource = collocationsSource[node].items()
        col_listSource.sort(key=itemgetter(1), reverse=True)


        col_listCible = collocationsCible[nodeCible].items()
        col_listCible.sort(key=itemgetter(1), reverse=True)
        #print col_listSource
        #print col_listCible
        #print '-------------------------'
        for collocatif in map(itemgetter(0), col_listSource):
            #print '\t', collocatif
            collocatif = re.sub('_',' ',collocatif).lower()
            collocatif = re.sub("\A[()\,\.\?']|[()\,\.\?']$|[\[\]]","",collocatif).lower()
            for collocatifCible in map(itemgetter(0), col_listCible):
                if (collocatif,collocatifCible) in dico:#'\n'+collocatif+'\t'+collocatifCible+'\n' in dico:
                    print node+'\t'+collocatif+'\t'+nodeCible+'\t'+collocatifCible

                    out.write(node+'\t'+collocatif+'\t'+nodeCible+'\t'+collocatifCible+'\n')
    out.close()
if __name__ == "__main__" :
    main()




