from django.conf.urls import url
from . import views
urlpatterns = [
      url(r'^home4/$',views.home4),
      url(r'^home3/$',views.home3),
      url(r'^home2/$',views.home2,name='spage'),
      url(r'^home1/$',views.home1,name='fpage'),
      url(r'^$',views.home, name='homepage'),       
      url(r'^home3/check_pass/$',views.check_pass),   
      url(r'^home4/calculate/$',views.calculate),      

]
