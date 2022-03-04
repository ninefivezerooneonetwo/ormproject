import json
import logging

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django_request_mapping import request_mapping

from web.models import Cust


@request_mapping("")
class MyView(View):

    @request_mapping("/", method="get")
    def home(self,request):
        return render(request,'home.html');

    @request_mapping("/ajax", method="get")
    def ajax(self, request):
        context = {
            'center': 'ajax.html'
        }

        return render(request, 'home.html', context);

    @request_mapping("/ajaximpl", method="get")
    def ajaximpl(self, request):
        data = [];

        for i in range(1, 10):
            dic = {}
            dic['id'] = 'id' + str(i);
            dic['name'] = 'james' + str(i);
            dic['age'] = i;
            data.append(dic);

        return HttpResponse(json.dumps(data), content_type='application/json')

    @request_mapping("/geoimpl", method="get")
    def geoimpl(self, request):
        data = [];

        dic1 = {}
        dic1['content'] = 'naver'
        dic1['lat'] = 35.170028766799225
        dic1['lng'] = 129.0850187151504
        dic1['target'] = 'http://www.naver.com'

        dic2 = {}
        dic2['content'] = 'daum'
        dic2['lat'] = 35.180128766799225
        dic2['lng'] = 129.0751187151504
        dic2['target'] = 'http://www.daum.net'

        dic3 = {}
        dic3['content'] = 'google'
        dic3['lat'] = 35.190025766799225
        dic3['lng'] = 129.0750185151504
        dic3['target'] = 'http://www.google.com'

        dic4 = {}
        dic4['content'] = 'instagram'
        dic4['lat'] = 35.187028766799225
        dic4['lng'] = 129.0720187151504
        dic4['target'] = 'http://www.instagram.com'

        data.append(dic1)
        data.append(dic2)
        data.append(dic3)
        data.append(dic4)
        return HttpResponse(json.dumps(data), content_type='application/json')

    @request_mapping("/iot", method="get")
    def iot(self, request):
        id = request.GET['id']
        temp = request.GET['temp']
        el = request.GET['el']

        #-----------------------------------
        el_logger = logging.getLogger('el_file')
        el_logger.debug(id + ', ' + temp + ', ' + el)
        #-----------------------------------

        return render(request, 'ok.html');

    @request_mapping("/login", method="get")
    def login(self, request):
        context = {
            'center': 'login.html'
        };
        return render(request, 'home.html', context);

    @request_mapping("/loginimpl", method="post")
    def loginimpl(self, request):
        # id, pwd 를 확인 한다.
        id = request.POST['id'];
        pwd = request.POST['pwd'];
        context = {};

        # cust = Cust.objects.get(id=id)
        # if (cust.id == id) and (cust.pwd == pwd):
        #     request.session['sessionid'] = id;
        #     context['center'] = 'loginok.html';
        # elif (cust.id != id) or (cust.pwd != pwd):
        #     # request.session['sessionid'] = id;
        #     context['center'] = 'loginfail.html';

        try:
            cust = Cust.objects.get(id=id)
            if cust.pwd == pwd:
                request.session['sessionid'] = cust.id;
                request.session['sessionname'] = cust.name;
                context['center'] = 'loginok.html'
            else:
                raise Exception
        except:
            context['center'] = 'loginfail.html';

        return render(request, 'home.html', context);

    @request_mapping("/logout", method="get")
    def logout(self, request):
        if request.session['sessionid'] != None:
            del request.session['sessionid'];
        return render(request, 'home.html');

    @request_mapping("/register", method="get")
    def register(self, request):
        context = {
            'center': 'register.html'
        };
        return render(request, 'home.html', context);

    @request_mapping("/registerimpl", method="post")
    def registerimpl(self, request):
        id = request.POST['id'];
        pwd = request.POST['pwd'];
        name = request.POST['name'];
        context = {}
        try:
            Cust.objects.get(id=id)
            context['center'] = 'registerfail.html'
            context['rname'] = name
        except:
            Cust(id=id, pwd=pwd, name=name).save()
            context['center'] = 'registerok.html'
            context['rname'] = name

        return render(request, 'home.html', context);

    @request_mapping("/geo", method="get")
    def geo(self, request):
        context = {
            'center': 'geo.html'
        };
        return render(request, 'home.html', context)

    @request_mapping("/location", method="get")
    def location(self, request):
        context = {
            'center': 'location.html'
        };
        return render(request, 'home.html', context)

