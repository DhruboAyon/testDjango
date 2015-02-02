from django.conf.urls import patterns, url

from nsApicall import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^articles/(?P<searchparam>[\w|\W]+)$', views.articles, name='articles'),
                       url(r'^topics/(?P<searchparam>[\w|\W]+)$', views.topics, name='topics'),
                       url(r'^article/(?P<guid>[\w|\W]+)$', views.singleArticle, name='single_article'),
                       url(r'^topic/(?P<guid>[\w|\W]+)$', views.singleTopic, name='single_topic'),
                       url(r'^results/(?P<api>article|topic)/(?P<guid>[\w|\W]+)$', views.results, name='results'),
)
