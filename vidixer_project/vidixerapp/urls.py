from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
# from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('home/', views.user_home, name='user_home'),
<<<<<<< HEAD
    path('accounts/profile/', views.user_home, name='user_home'),
    path('home/upload/', views.video_upload, name='video_upload'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html',next_page=''), name='logout'),
    path('accounts/logout/', LogoutView.as_view(template_name='logout.html',next_page=''), name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
=======
    path('home/upload/', views.upload_video, name='video_upload'),
    path('home/vedio_decription/', views.vedio_decription, name='vedio_decription'),
    path('logout/', views.logout_view, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> d0e15a3bc5e1018cdf1b187c6bac350e6c113c64
