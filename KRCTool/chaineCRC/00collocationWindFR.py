#!/usr/bin/env python
# -*- coding: utf-8 -*-
##########################################################################
### Autor name :         Firas HMIDA                ##
### Adresse :            firas.hmida@univ-nantes.fr        ##
### Date de création :        21-07-2014                ##
### Date de modification :     22-07-2014                      ##
### Contenu :             Baseline : linguistic-collocations    ##
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

def collocations(words,defined_terms):

    
    # Count the words and bigrams
    wfd = FreqDist([w[2] for w in words])
    
    #tri = [tuple(x[1:] for x in words[i:i+3]) for i in range(len(words)-2) if 
    #       tuple(x[1:] for x in words[i:i+3])[1][1] in [token.split('\t')[2] for token in defined_terms]]
    tri = [tuple(x[1:] for x in words[i:i+7]) for i in range(len(words)-6) if 
           tuple(x[1:] for x in words[i:i+7])[3][1] == defined_terms ]#in [token.split('\t')[2] for token in defined_terms]  ]
           #tuple(x[1:] for x in words[i:i+2])[2][1] in [token.split('\t')[2] for token in defined_terms] ]
    #tri = nltk.bigrams([w[1:] for w in words])
    ite = [itertools.combinations(trigram,2) for trigram in tri]



   
    #for i in ite[:10]: print i

    
    bigrams_tag_fd = FreqDist([ff for it in ite for ff in it])

    filtre = nltk.bigrams([w[1:] for w in words])


    '''
    for ii in bigrams_tag_fd.keys():
        if ((ii[0][1] or ii[1][1]) in [token.split('\t')[2] for token in defined_terms]) and (bigrams_tag_fd[ii]>1):
            bigrams_tag_fd[ii] = bigrams_tag_fd[ii]- filtre.count(tuple(ii))
    '''      
   

    ADJ = r"JJ|VVG|VVN|VVD"
    NOM = r"NN|VV$"
    VER = r"VVP|VVZ"

    adj = "ADJ|VER:[(ppre|pper)]"
    nom = "NAM|NOM|VER:infi"
    ver = "VER:[^(ppre|pper|infi)]"
    
    pfd = { (a,b):bigrams_tag_fd[(a,b)] for (a, b) in sorted(bigrams_tag_fd.keys())
                                    if (b[1] == defined_terms and#in [token.split('\t')[2] for token in defined_terms] and
                                    re.match(ver,a[0]))
                                    or (a[1] == defined_terms and#in [token.split('\t')[2] for token in defined_terms] and
                                    re.match(ver,b[0])) }

    
    # score them
    scored = [((w1,w2), score(w1, w2, wfd, pfd)) for w1, w2 in pfd]
    scored.sort(key=itemgetter(1), reverse=True)
   
    
    return scored#map(itemgetter(0), scored)
    
def score(word1, word2, wfd, pfd, power=3):
   # print word1, '----', word2
    Ngrams = 7
    freq1 = wfd[word1[1]]
    freq2 = wfd[word2[1]]
    freq12 = pfd[(word1, word2)]

    p = freq2/float(len(wfd.keys()) - freq2 )
    q = 1 - p
    E = p * freq1 * Ngrams
    return (freq12 - E ) / float( sqrt(E * q))
    
def main():
    if len(sys.argv) < 4 or len(sys.argv)>4:
        sys.stderr.write("Usage: python collocation-Zscore.py [TaggedPOScorpusName] [termsList] \n")
        sys.exit(1)
    else :
        defined_terms = sys.argv[2]# open(sys.argv[2],'r').read().lower().strip().split('\n')
        stopwords = open(sys.argv[3],'r').read().lower().strip().split('\n')
        words_tagged = open(sys.argv[1],'r').read().strip().split('\n')
        words_tagged_tuple = [ tuple(token.split('\t')) for token in words_tagged
                               if token.split('\t')[0].lower() not in stopwords ]


        words_tagged_tuple = [(word.lower(),tag,lem.lower()) for (word,tag,lem) in words_tagged_tuple]
        start_time = time.time()
        all_collocations = collocations(words_tagged_tuple,defined_terms)
        end_time = time.time()
        print "Time spent finding collocations = {:.2f} seconds.".format(
          end_time - start_time)
        print "Collocations lenth = ", len(all_collocations)
        pickle.dump(all_collocations, open('outCollocations/collocationLemmaFR.p', 'wb'))
   
    
if __name__ == "__main__":
    main()

















