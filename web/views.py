import logging

from django.shortcuts import render
from django.views import View
from django_request_mapping import request_mapping

from web.models import Cust


@request_mapping("")
class MyView(View):

    @request_mapping("/", method="get")
    def home(self,request):
        return render(request,'home.html');

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