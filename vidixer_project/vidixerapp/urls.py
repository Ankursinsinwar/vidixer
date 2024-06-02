from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.user_home, name='user_home'),
    path('home/upload/', views.video_upload, name='video_upload'),
    path('login/', LoginView.as_view(template_name='login.html',next_page='home/'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html',next_page=''), name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
