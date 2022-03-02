from django_request_mapping import UrlPattern
from web.views import MyView
from web.views_article import ArticleView
from web.views_cart import CartView
from web.views_guest import GuestView
from web.views_item import ItemView

urlpatterns = UrlPattern();
urlpatterns.register(MyView);
urlpatterns.register(GuestView);
urlpatterns.register(ArticleView);
urlpatterns.register(ItemView);
urlpatterns.register(CartView);
