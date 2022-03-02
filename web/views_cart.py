from django.shortcuts import render, redirect
from django.views import View
from django_request_mapping import request_mapping

from config.settings import UPLOAD_DIR
from web.models import Guest, Article, Item, Cart, Cust


@request_mapping("/cart")
class CartView(View):

    @request_mapping("/a", method="get")
    def all(self,request):
        objs = Cart.objects.select_related('custid', 'itemid'); # join을 걸 항목들
        print(objs.query);

        context = {
            'center':'cart/list.html',
            'objs':objs
        };
        return render(request,'home.html',context);

    @request_mapping("/i/<int:num>/<int:itempk>/<str:custpk>/", method="get")
    def insert(self, request, num, itempk, custpk):
        print(itempk, num, custpk);
        cust = Cust.objects.get(id=custpk);
        item = Item.objects.get(id=itempk);
        obj = Cart(custid=cust, itemid=item, num=num);
        obj.save();
        return redirect('/cart/a');


