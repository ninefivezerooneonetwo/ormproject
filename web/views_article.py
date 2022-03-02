from django.shortcuts import render, redirect
from django.views import View
from django_request_mapping import request_mapping
from web.models import Article

@request_mapping("/article")
class ArticleView(View):

    @request_mapping("/a", method="get")
    def all(self,request):
        objs = Article.objects.all();
        print(objs.query)
        context = {
            'center':'article/list.html',
            'objs':objs
        };
        return render(request,'home.html',context);

    # guest/g/3
    @request_mapping("/g/<int:pk>/", method="get")
    def get(self, request, pk):
        obj = Article.objects.get(id=pk);
        context = {
            'center':'article/get.html',
            'obj':obj
        };
        return render(request,'home.html',context);

    @request_mapping("/iv", method="get")
    def insertview(self,request):
        context = {
            'center':'article/add.html',
        };
        return render(request,'home.html',context);

    @request_mapping("/i", method="get")
    def insert(self,request):
        name = request.GET['name'];
        price = request.GET['price'];
        obj = Article(name=name, price=price);
        obj.save();

        return redirect('/article/a');

    @request_mapping("/d/<int:pk>/", method="get")
    def delete(self, request, pk):
        obj = Article.objects.get(id=pk)
        obj.delete()

        return redirect('/article/a')

    @request_mapping("/u", method="get")
    def update(self, request):
        name = request.GET['name'];
        price = request.GET['price'];
        id = request.GET['id']

        obj = Article.objects.get(id=id);
        obj.name = name
        obj.price = price
        obj.save()

        return redirect('/article/g/' + id)
        #return render(request,'home.html');

    @request_mapping("/uv/<int:pk>/", method="get")
    def updateview(self, request, pk):
        obj = Article.objects.get(id=pk)
        context = {
            'center':'article/update.html',
            'obj':obj
        };
        return render(request, 'home.html', context);

