#-*- coding:utf-8 -*-
from django import template
from django.utils.html import escape
register = template.Library()
from KRCTool.models import KRCdata
import re
from django.utils.safestring import mark_safe
@register.filter
def crc_correspondant(couple,coll):
	return KRCdata.objects.filter(ttermSource=couple.termSource,ttermTarget=couple.termTarget,
			collocationSource=coll[0], collocationTarget=coll[1])

@register.filter(is_safe=True)
def citation(texte):
	"""
	Affiche le texte passé en paramètre, encadré de guillemets français
	doubles et d'espaces insécables.
	"""
	return "4444 %s 4444" % escape(texte)


@register.filter(is_safe=True)
def posId(co,liste):
	return liste.index(co)

@register.filter(is_safe=True)
def colorTerm(text,term):
	#t = text.split()
 text = re.sub(term.ttermSource, r'<b style="color:DodgerBlue ;">'+term.ttermSource+'</b>',text)
 text = re.sub(term.collocationSource, r'<b style="color:DodgerBlue ;">'+term.collocationSource+'</b>',text)
 text = re.sub(term.ttermTarget, r'<b style="color:DodgerBlue ;">'+term.ttermTarget+'</b>',text)
 text = re.sub(term.collocationTarget, r'<b style="color:DodgerBlue ;">'+term.collocationTarget+'</b>',text)
 #print "sakyt"
  #text = re.sub('scories', r'<b style="color:DodgerBlue ;">'+'scories'+'</b>',text)
  #text = re.sub('incandescents', r'<b style="color:DodgerBlue ;">'+'incandescents'+'</b>',text)
	#text = re.sub(col, r'<b>'+col+'</b>',text)
 return mark_safe(text)


'''  <div class="panel-group" id="accordion">
    <div class="panel panel-default">
      <div class="panel-heading">
        
          <a data-toggle="collapse" data-parent="#accordion" href="#collapse1">ADJ</a>
        
      </div>
      <div id="collapse1" class="panel-collapse collapse in">
        <div class="panel-body">Contenu</div>
      </div>
    </div>
    <div class="panel panel-default">
      <div class="panel-heading">
        <a data-toggle="collapse" data-parent="#accordion" href="#collapse2">NOM</a>
      </div>
      <div id="collapse2" class="panel-collapse collapse">
        <div class="panel-body">Contenu</div>
      </div>
    </div>
    <div class="panel panel-default">
      <div class="panel-heading">
        
          <a data-toggle="collapse" data-parent="#accordion" href="#collapse3">VER</a>
       
      </div>
      <div id="collapse3" class="panel-collapse collapse">
        <div class="panel-body">Contenu</div>
      </div>
    </div>
  </div> '''