from django.urls import path
from django.conf.urls.static import static 
from . import views
from django.conf import settings 

urlpatterns = [
    path('', views.index.as_view()),
    path('Addsport',views.Create_Sport,name='Addsport'),
    path('sportGame',views.sportViews,name='sportGame'),
    path('home', views.home,name='home'),
    path('AddSV',views.Add_V,name='AddSV'),
    path('delete/<int:id>/', views.deleteS, name='delete'),
    path('edit/<int:id>/', views.editSport, name='edit'),
    path('volunteering', views.volunteView,name='volunteering'),
    path('VonterAction',views.volunterAdd,name='VonterAction'),
    path('volunteViewAdd',views.volunteViewAdd,name='volunteViewAdd'),
    path('deleteV/<int:id>/', views.deleteV, name='deleteV'),
    path('editV/<int:id>/', views.editV, name='editV'),
    path('news',views.Newsm,name='news'),
    path('Add_News',views.newsp,name='Add_News'),
    path('class', views.classv,name='class'),
    path('login',views.login_views, name='login'),
    path('login_request',views.login_request,name='login_request'),
    path('register',views.register,name='register'),
    path('login',views.login_,name='login'),
   path('booking',views.bookings,name='booking'),
   path('bookClass',views.bookClasses,name='bookClass'),
   path('registr', views.user_register, name='registr'),
   path('join', views.reg, name='join'),
   path('booksport',views.booksport,name='booksport'),
   path('FAQ',views.faq,name='FAQ'),
   path('home-section',views.index.as_view()),
   path('GameEnd',views.endGames.as_view()),
   path('post_Comment',views.post_summary,name='post_Comment'),
   path('teams',views.teams,name='teams'),
   path('full',views.GamesFull,name='full'),

]
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 