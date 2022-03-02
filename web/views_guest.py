from django.shortcuts import render, redirect
from django.views import View
from django_request_mapping import request_mapping
from web.models import Guest

@request_mapping("/guest")
class GuestView(View):

    @request_mapping("/a", method="get")
    def all(self,request):
        objs = Guest.objects.all();
        print(objs.query)
        context = {
            'center':'guest/list.html',
            'objs':objs
        };
        return render(request,'home.html',context);

    # guest/g/3
    @request_mapping("/g/<int:pk>/", method="get")
    def get(self, request, pk):
        obj = Guest.objects.get(id=pk);
        context = {
            'center':'guest/get.html',
            'obj':obj
        };
        return render(request,'home.html',context);

    @request_mapping("/iv", method="get")
    def insertview(self,request):
        context = {
            'center':'guest/add.html',
        };
        return render(request,'home.html',context);

    @request_mapping("/i", method="get")
    def insert(self,request):
        title = request.GET['title'];
        content = request.GET['content'];
        obj = Guest(title=title, content=content);
        obj.save();

        return redirect('/guest/a');

    @request_mapping("/d/<int:pk>/", method="get")
    def delete(self, request, pk):
        obj = Guest.objects.get(id=pk)
        obj.delete()

        return redirect('/guest/a')

    @request_mapping("/u", method="get")
    def update(self, request):
        title = request.GET['title'];
        content = request.GET['content'];
        id = request.GET['id']

        obj = Guest.objects.get(id=id);
        obj.title = title
        obj.content = content
        obj.save()

        return redirect('/guest/g/' + id)
        #return render(request,'home.html');

    @request_mapping("/uv/<int:pk>/", method="get")
    def updateview(self, request, pk):
        obj = Guest.objects.get(id=pk)
        context = {
            'center':'guest/update.html',
            'obj':obj
        };
        return render(request, 'home.html', context);

