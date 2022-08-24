"""
Definition of urls for ElectionGuard.
"""

from datetime import datetime
from traceback import format_stack
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('search_spoiled/', views.search_spoiled, name='search_spoiled'),
    path('about/', views.about, name='about'),
    path('admin/', admin.site.urls),
    path('legacy/', include('legacy.urls')),
    path('app/', include('app.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
