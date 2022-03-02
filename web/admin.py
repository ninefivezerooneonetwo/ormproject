from django.contrib import admin
from web.models import Guest, Article, Cust, Item, Cart


# Register your models here.
class GuestAdmin(admin.ModelAdmin):
    list_display = ('id','title','content','regdate');
admin.site.register(Guest,GuestAdmin);

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','pub_date');
admin.site.register(Article,ArticleAdmin);

class CustAdmin(admin.ModelAdmin):
    list_display = ('id','name','pwd');
admin.site.register(Cust,CustAdmin);

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','imgname','regdate');
admin.site.register(Item,ItemAdmin);

class CartAdmin(admin.ModelAdmin):
    list_display = ('id','custid','itemid','num','regdate');
admin.site.register(Cart,CartAdmin);