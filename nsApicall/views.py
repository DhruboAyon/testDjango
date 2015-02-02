import json
from django.shortcuts import render
from nsApicall.utils import GenericApiCaller
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse


def index(request):
    return render(request,"nsApicall/index.html",{})


def articles(request,searchparam):
    payload = {'access_key':'c4bcc3f7c9bf9ec159f51da0a86ca658',
               'format':'json',
               'pagesize':'10',
               'query':searchparam,
    }
    data = []
    data = GenericApiCaller.getJsonData('http://api.newscred.com/articles',payload);

    return HttpResponse(json.dumps(data), content_type="application/json");


def topics(request,searchparam):
    payload = {'access_key':'c4bcc3f7c9bf9ec159f51da0a86ca658',
               'format':'json',
               'pagesize':'10',
               'query':searchparam,
    }
    data = []
    data = GenericApiCaller.getJsonData('http://api.newscred.com/topics',payload);

    return HttpResponse(json.dumps(data), content_type="application/json");


def singleArticle(request,guid):

    payload = {'api':'article',
               'guid':guid}
    return render(request,'nsApicall/next.html',payload)


def singleTopic(request,guid):
    payload = {'api':'topic',
               'guid':guid}
    return render(request,'nsApicall/next.html',payload)
    

def results(request,api,guid):
    payload = {'access_key':'c4bcc3f7c9bf9ec159f51da0a86ca658',
               'format':'json',
    }
    url = 'http://api.newscred.com/'+api+'/'+guid
    print url
    data = []
    data = GenericApiCaller.getJsonData(url,payload);

    return HttpResponse(json.dumps(data), content_type="application/json");
