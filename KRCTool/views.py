#-*- coding: utf-8 -*-

from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import render

from datetime import datetime
from KRCTool.models import KRCrequest, KRCdata,TranslationCandidate, valider
from KRCTool.forms import KRCform, validerForm

from django.views.generic import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy

import re
import os
import sys


def home(request):
	KRCdata.objects.all().delete()
	
	KRCrequest.objects.all().delete()
	TranslationCandidate.objects.all().delete()
	#Candidates()

	if request.method =='POST':
		form = KRCform(request.POST)
		if form.is_valid():

			#Candidates()
			krcrequest = form.save(commit=False)
			krcrequest.termSource = form.cleaned_data['termSource']
			krcrequest.termTarget = form.cleaned_data['termTarget']
			krcrequest.translSens = form.cleaned_data['translSens']
			krcrequest.corpus = form.cleaned_data['corpus']
			krcrequest.save()
			envoi=True
			Krcrequest = KRCdata.objects.filter(ttermSource=krcrequest.termSource,ttermTarget=krcrequest.termTarget)
			liste_coll = list(set([(krc.collocationSource,krc.collocationTarget) for krc in Krcrequest]))
			liste_collADJ = list(set([(krc.collocationSource,krc.collocationTarget) for krc in Krcrequest.filter(collocationType='ADJ')]))
			liste_collNOM = list(set([(krc.collocationSource,krc.collocationTarget) for krc in Krcrequest.filter(collocationType='NOM')]))
			liste_collVER = list(set([(krc.collocationSource,krc.collocationTarget) for krc in Krcrequest.filter(collocationType='VER')]))
			liste_collAUT = list(set([(krc.collocationSource,krc.collocationTarget) for krc in Krcrequest.filter(collocationType='ADJ-VER')]))

			liste_candidates = TranslationCandidate.objects.filter(tttermSource=krcrequest.termSource)
								
	else:
		form = KRCform()
	#print len(KRCdata.objects.all())
	#Krcrequest=association_champ()
	return render(request, 'KRC.html',locals())


def newHome(request):
	#Candidates()
	#TranslationCandidate.objects.all().delete()
	KRCrequest.objects.all().delete()
	if request.method =='POST':
		form = KRCform(request.POST)
		validForm = validerForm(request.POST)
		#print "#######", request.POST
		if form.is_valid():
			krcrequest = form.save(commit=False)
			krcrequest.termSource = form.cleaned_data['termSource']
			krcrequest.termTarget = form.cleaned_data['termTarget']
			#krcrequest.translSens = form.cleaned_data['translSens']
			#krcrequest.corpus = form.cleaned_data['corpus']
			krcrequest.save()
			envoi=True
			return redirect('KRCTool.views.affiche_collocations',id_couple=krcrequest.id)						
	else:
		form = KRCform()
	return render(request, 'base.html',locals())

def processus(request, id_couple):
	queryCouple = KRCrequest.objects.get(id = id_couple)
	#os.system('cd KRCTool/chaineCRC')
	#os.system('ls')
	os.chdir("KRCTool/chaineCRC")
	command = 'python processus.py '+queryCouple.termTarget+' '+queryCouple.termSource
	os.system(command)

	KRCdata.objects.all().delete()
	KRCfile = open('alignedCouples.csv').read()
	#print len(KRCfile.strip().split('\n'))
	for line in KRCfile.strip().split('\n'):
		champs = line.split('\t')
		krc = KRCdata()	
		kreq = KRCrequest(termSource=champs[0],termTarget=champs[3])
		#kreq.save()
		
		#krc.krcrequest=kreq
		krc.ttermTarget=champs[3]
		krc.ttermSource=champs[0]
		krc.collocationSource = champs[1]
		krc.collocationTarget = champs[4]
		krc.sentenceSource = champs[2]
		krc.sentenceTarget = champs[5]
		krc.collocationType = 'VER'#champs[8]
		#print krc.ttermSource, ' ## ', krc.ttermTarget

		krc.save()
	text = KRCdata.objects.all()
	return HttpResponse(len(text))



	#return HttpResponse('finish')




def affiche_collocations(request, id_couple):
	print os.getcwd()
	#Candidates()
	#l = len(KRCrequest.objects.all())
	queryCouple = KRCrequest.objects.get(id = id_couple)
	#os.system('cd KRCTool/chaineCRC')
	#os.system('ls')
	os.chdir("KRCTool/chaineCRC")
	print queryCouple.termTarget
	print queryCouple.termSource
	command = 'python processus.py '+queryCouple.termTarget.encode('utf8')+' '+queryCouple.termSource.encode('utf8')
	os.system(command)

	KRCdata.objects.all().delete()
	KRCfile = open('alignedCouples.csv').read()
	#print len(KRCfile.strip().split('\n'))
	for line in KRCfile.strip().split('\n'):
		champs = line.split('\t')
		krc = KRCdata()	
		try:
			kreq = KRCrequest(termSource=champs[0],termTarget=champs[3])
			#kreq.save()
			
			#krc.krcrequest=kreq
			krc.ttermTarget=champs[3]
			krc.ttermSource=champs[0]
			krc.collocationSource = champs[1]
			krc.collocationTarget = champs[4]
			krc.sentenceSource = champs[2]
			krc.sentenceTarget = champs[5]
			krc.collocationType = 'VER'#champs[8]
		#print krc.ttermSource, ' ## ', krc.ttermTarget


			krc.save()
		except Exception:
			pass




	queryCouple = KRCrequest.objects.get(id = id_couple)
	queryCollocations = KRCdata.objects.filter(ttermSource=queryCouple.termSource,ttermTarget=queryCouple.termTarget)
	liste_coll = list(set([(krc.collocationSource,krc.collocationTarget) for krc in queryCollocations]))
	liste_collADJ = list(set([(krc.collocationSource,krc.collocationTarget) for krc in queryCollocations.filter(collocationType='ADJ')]))
	liste_collNOM = list(set([(krc.collocationSource,krc.collocationTarget) for krc in queryCollocations.filter(collocationType='NOM')]))
	liste_collVER = list(set([(krc.collocationSource,krc.collocationTarget) for krc in queryCollocations.filter(collocationType='VER')]))
	liste_collAUT = list(set([(krc.collocationSource,krc.collocationTarget) for krc in queryCollocations.filter(collocationType='ADJ-VER')]))

	liste_candidates = TranslationCandidate.objects.filter(tttermSource=queryCouple.termSource)

	#return HttpResponse(queryCouple)
	form = KRCform(request.POST)
	
	
	#print request
	os.chdir("../../")
	return render(request, 'autre.html',locals())

def affiche_collocationsCandidates(request, id_couple, id_candidate):
	queryTrans = TranslationCandidate.objects.get(id= id_candidate)
	queryC = KRCrequest.objects.get_or_create(termSource= queryTrans.tttermSource, termTarget=queryTrans.transCandidate)
	queryC = KRCrequest.objects.get(termSource= queryTrans.tttermSource, termTarget=queryTrans.transCandidate)
	return redirect('KRCTool.views.affiche_collocations',id_couple=queryC.id)
	#print queryTrans.tttermSource
	#return HttpResponse(queryTrans.tttermSource)


def KRCsentence(request, id_krc):
	req = KRCdata.objects.get(id=id_krc)
	#krcrequest = KRCdata.objects.filter(ttermSource=krcrequest.termSource,ttermTarget=krcrequest.termTarget)
	return render(request,'KRC.html',{'KRCsentences':req})
	
	#return redirect('KRCTool.views.home' )

def association_champ(request,id):
	KRCdata.objects.all().delete()
	KRCfile = open('./KRCTool/data/crc.csv').read()
	#print len(KRCfile.strip().split('\n'))
	for line in KRCfile.strip().split('\n'):
		champs = line.split('\t')
		krc = KRCdata()	
		kreq = KRCrequest(termSource=champs[0],termTarget=champs[4])
		#kreq.save()
		
		#krc.krcrequest=kreq
		krc.ttermTarget=champs[4]
		krc.ttermSource=champs[0]
		krc.collocationSource = champs[1]
		krc.collocationTarget = champs[5]
		krc.sentenceSource = champs[2]
		krc.sentenceTarget = champs[6]
		krc.collocationType = champs[8]
		#print krc.ttermSource, ' ## ', krc.ttermTarget

		krc.save()
	text = KRCdata.objects.all()
	return HttpResponse(len(text))


def Candidates():
	candidatesFile = open('./KRCTool/data/traduction-candidates.csv').read().strip().split('\n')
	for couples in candidatesFile:
		couple = TranslationCandidate(tttermSource=couples.split('\t')[0], transCandidate=couples.split('\t')[1])
		couple.save()
	#return render(request, 'todo/KRC.html',locals())

# Create your views here.
