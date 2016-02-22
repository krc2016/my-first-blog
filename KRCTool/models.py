#-*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models

# Create your models here.
imTarget ='''img src="http://vignette3.wikia.nocookie.net/scrubs/images/c/c7/Flag-France.jpg/revision/latest?cb=20090820235843"  title=" traduction français"  border="0" height="16" width="16">'''
imSource ='''<img src="http://vignette2.wikia.nocookie.net/poths-pirates-of-the-high-seas/images/a/a8/British_Flag_Wallpapers_%281%29.png/revision/latest?cb=20131117031203" title=" traduction anglais" border="0" height="16" width="16">'''

class valider(models.Model):
	oui = models.BooleanField(default=True)
	non = models.BooleanField(default=True)


class KRCrequest(models.Model):
	"""docstring for KRC"models.Modelf __init__(self, arg):
		super(KRC,models.Model.__init__()
		self.arg Model"""
	translSens = models.CharField(max_length=20,choices=(('EN-FR','EN-FR'),('FR-EN','FR-EN')),default='EN-FR')
	termSource = models.CharField(max_length=20, null=True)
	termTarget = models.CharField(max_length=20, null=True)
	corpus = models.CharField(max_length=20,choices=(('Vulcanologie','Vulcanologie'),('Diabète','Diabète'),('Cancer du sein', 'Cancer du sein')),default='Vulcanologie')

	case_val = models.ManyToManyField(valider)
	#valide = models.CharField(max_length=1, null=True)

	def __unicode__(self):
		return "termSource : {0} , termTarget : {1} ".format(self.termSource,self.termTarget)



class KRCdata(models.Model):
	KRCfile = open('./KRCTool/data/crc.csv').read()#	.strip().split('\n')
#	termSource =
#	termTarget = 
	ttermSource = models.CharField(max_length=20, null=True)
	ttermTarget = models.CharField(max_length=20, null=True)
	sentenceSource = models.CharField(max_length=500)
	sentenceTarget = models.CharField(max_length=500)
	collocationSource = models.CharField(max_length=20, null=True)
	collocationTarget = models.CharField(max_length=20, null=True)
	collocationType = models.CharField(max_length=20, null=True)
	#krcrequest = models.ForeignKey('KRCrequest')

class TranslationCandidate(models.Model):
	tttermSource = models.CharField(max_length=20, null=True)
	transCandidate = models.CharField(max_length=20, null=True)



