from django.urls  import path
from . import views
from users import views as user_views

urlpatterns = [ #list
    path('',views.index,name='index'),
    path('buisness', views.buisness,name='buisness'),
    path('sports',views.sports,name='sports'),
    path('enter',views.enter,name='enter'),
    path('our',views.our,name='our'),
    path('register/',user_views.register,name='register'),
   
    
]
