from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from administration import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', LoginView.as_view(), name='login'),
    path('home/', views.home, name="home"),
    path('theme', views.theme, name="theme"),
    path('profile/', views.profile, name="profile"),
    path('administration/', include('administration.urls')),
    path('create-user/', views.create_user, name="register"),
    path('social-auth/', include('social_django.urls', namespace='social')),
    # path('issues/', include('ticket_system.urls')),
]

handler404 = 'administration.views.error_404'
handler500 = 'administration.views.error_500'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)