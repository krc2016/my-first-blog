from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('KRCTool.views',
	#url(r'^accueil/$', 'home',name='krc-list'),
	url(r'^accueil/$', 'newHome', name='news-archive'),
	url(r'^accueil/(?P<id_couple>\d+)/$', 'affiche_collocations'),
	url(r'^accueil/(?P<id_couple>\d+)/(?P<id_candidate>\d+)/$', 'affiche_collocationsCandidates'),



	#url(r'^article/(\d+)/$', 'association_champ'),
	#url(r'^article/(\d+)/$', 'KRCsentence'),

	#url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})/$','newHome'),
	#url(r'^krc/new/$', views.couple_trad),




)
		