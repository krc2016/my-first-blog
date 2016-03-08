import pickle
import xlwt
import re
'''
dico = open("EN-FR-ELRA").read().strip()
lines = open('ADJ-EN-vu.tsv').read().strip().split('\n')
lines2 = open('VER-EN-vu.tsv').read().strip().split('\n')
dictBilingue = pickle.load(open('dictBilingue.p', 'rb'))

n = 0
lll = list()
for i in lines +lines2:
	try:
				
		if i.split('\t')[4] != '' :#and (i.split('\t')[1]+'\t'+i.split('\t')[4] in dico):
			#print i
			lll.append(i.split('\t')[0])
			n+=1
	except Exception:
		pass
print n
print len(set(lll))
for i in set(lll): print i


linesFR = list(set(open('../vulcanoPOS.txt').read().strip().split('.	SENT	.')))
linesEN = list(set(open('../vulcanoEN-POS.txt').read().strip().split('.	SENT	.')))

stop_wordsFR = open('../stopW/StopWords.txt').read().strip().split('\n')
stop_wordsEN = open('../stopW/StopWordsEN.txt').read().strip().split('\n')
styleEntete = xlwt.easyxf('font: name Times New Roman, color-index black, bold on;',
	num_format_str='#,##0.00')

wb = xlwt.Workbook(encoding='utf-8')
ws = wb.add_sheet('TD Sheet', cell_overwrite_ok=True)

ws.write(0, 0, 'TERM_S', styleEntete)
ws.write(0, 1, 'Collocatif_S',styleEntete)
ws.write(0, 2, 'id_phS',styleEntete)
ws.write(0, 3, 'ph_S ',styleEntete)
ws.write(0, 4, 'Term_C',styleEntete)
ws.write(0, 5, 'COLLOCATIF_C',styleEntete)
ws.write(0, 6, 'id_phC', styleEntete)
ws.write(0, 7, 'phC', styleEntete)
    #wr.write(0, 1, 'COLLOCATIF',styleEntete)
    #ws.col(2).width = len('DECISION')* 256

n=0
ll = []
for i in lines+lines2:
	try:
		if i.split('\t')[3] != '':
			ll.append(i.split('\t'))
			#print i
			n+=1
	except Exception:
		pass
print n
print len(ll)


from operator import itemgetter

ll.sort(key=itemgetter(0),reverse=False)

for k in ll:
	print k[0]


rowS = 1

for jj in ll:
	t_S = jj[0]
	coll_S = jj[1]

	t_C = jj[3]
	coll_C = jj[4]

	p=re.compile(r'\b\W?'+t_S+r'\W?\b ([^\s]+ ){0,3}\b\W?'+coll_S+
                     r'\W?\b|\b\W?'+coll_S+r'\W?\b ([^\s]+ ){0,3}\b\W?'+t_S+r'\W?\b')
	pFR=re.compile(r'\b\W?'+t_C+r'\W?\b ([^\s]+ ){0,3}\b\W?'+coll_C+
                     r'\W?\b|\b\W?'+coll_C+r'\W?\b ([^\s]+ ){0,3}\b\W?'+t_C+r'\W?\b')

	ws.write(rowS+1, 0,t_S)
	ws.write(rowS+1, 1,coll_S)
	ws.write(rowS+1, 4,t_C)
	ws.write(rowS+1, 5,coll_C)

        print t_S
	nbr = 0
	nbr_C = 0
	for sentence in linesEN :
		sentence = sentence.lower()
		
                lemmSentence =' '.join([line.split('\t')[2] for line in [l.strip() 
                                             for l in sentence.strip().split('\n')
                                             if len(sentence.strip()) != 0]])
                notLemmSentence =' '.join([line.split('\t')[0] for line in [l.strip() 
                                         for l in sentence.strip().split('\n') 
                                         if len(sentence.strip()) != 0]])	
		if p.search(' '.join([ww for ww in lemmSentence.split() if ww not in stop_wordsEN])):
			rowS+=1
			nbr+=1
 			ws.write(rowS, 0,t_S)
			ws.write(rowS, 1,coll_S)
			ws.write(rowS, 4,t_C)
			ws.write(rowS, 5,coll_C)
			ws.write(rowS, 2,nbr)
			ws.write(rowS, 3,notLemmSentence)

		
        
	if nbr ==0: print "Source", t_S,coll_S
	rowC = rowS-max(nbr_C,nbr)
	
	for sen in linesFR :
		sent = sen.lower()
		
                lemmSen =' '.join([lin.split('\t')[2] for lin in [ll.strip() 
                                             for ll in sent.strip().split('\n')
                                             if len(sent.strip()) != 0]])
                notLemmSen =' '.join([lin.split('\t')[0] for lin in [ll.strip() 
                                         for ll in sent.strip().split('\n') 
                                         if len(sent.strip()) != 0]])	
		if pFR.search(' '.join([www for www in lemmSen.split() if www not in stop_wordsFR])):
			nbr_C+=1
			rowC+=1
			ws.write(rowC, 0,t_S)
			ws.write(rowC, 1,coll_S)
			ws.write(rowC, 4,t_C)
			ws.write(rowC, 5,coll_C)
			ws.write(rowC, 6,nbr_C)
			#ws.write(rowC+1, 7,nbr_C)
			ws.write(rowC, 7,notLemmSen)
	if nbr_C ==0: print "Cible", t_C,coll_C
	rowS = max(rowC,rowS)
wb.save('finall.xls')


n = 0
'''
lines = open('references-last-last00.tsv').read().strip().split('\n')
ff = list()
#out = open('outfinal.xls','w')
posEN = 0
negEN = 0

posFR = 0
negFR = 0
nbrEN = 0
nbrFR = 0
grandDic = dict()
for i in lines :
	try:
		#out.write(i+'	'+str((i.split('\t')[1]+'\t'+i.split('\t')[6] ) in dico)+'\n')
		#if (i.split('\t')[1]+'\t'+i.split('\t')[6] ) in dico:#tBilingue[i.split('\t')[1]] :
		if i.split('\t')[0]!='': 
			termeS = i.split('\t')[0]
			collocatifS = i.split('\t')[1]
			coupleS = (termeS,collocatifS)

			termeC = i.split('\t')[5]
			collocatifC = i.split('\t')[6]
			coupleC = (termeC, collocatifC)
			#print (coupleS, coupleC)		
			if (coupleS, coupleC) not in grandDic.keys():
				
				grandDic[(coupleS,coupleC)]=dict()
				grandDic[(coupleS,coupleC)]=dict()

				if i.split('\t')[3] !='':
					grandDic[(coupleS,coupleC)]["phraseS"]=[i.split('\t')[3]]
				if i.split('\t')[8] !='':
					grandDic[(coupleS,coupleC)]["phraseC"]=[i.split('\t')[8]]
			else :
				if i.split('\t')[3] !='': grandDic[(coupleS,coupleC)]['phraseS'].append(i.split('\t')[3])
				if i.split('\t')[8] !='' :grandDic[(coupleS,coupleC)]['phraseC'].append(i.split('\t')[8])
				
		



		'''
		if i.split('\t')[9] != '': nbrFR+=1
 		if i.split('\t')[9] == str(1): posFR+=1
		elif i.split('\t')[9] == str(0) : negFR+=1
		'''
		#if i in dico:
			#print i.split('\t')[1]+'\t'+i.split('\t')[6]
		#	ff.append((i.split('\t')[1],i.split('\t')[6]))
		#	n+=1
	except Exception:
		pass
from operator import itemgetter
for k in grandDic.keys(): print k, len(grandDic[k]['phraseS']), len(grandDic[k]['phraseC'])

#print n
#print len(set(ff))
'''
print 'nbrEN :', nbrEN
print 'nbrFR :', nbrFR
print "EN valide :", posEN, float(posEN)/nbrEN
print "EN non-valide :", negEN, float(negEN)/nbrEN
print "FR valide :", posFR, float(posFR)/nbrFR
print "FR non-valide :", negFR, float(negFR)/nbrFR
 
#out.close()
'''
