from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import createview, deletepost, postdetails, updatepost
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.Listedview.as_view(),name='home'),
    path('postdetails/<int:pk>/',postdetails.as_view(),name='post-details'),
    path('postupdate/<int:pk>/',updatepost.as_view(),name='post-update'),
    path('postdelete/<int:pk>/',deletepost.as_view(),name='post-delete'),
    path('signup/',views.user,name='signup'),
    path('profile/',views.profile,name='profile'),
    path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('newpost/',createview.as_view(),name='newpost')

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)