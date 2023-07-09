from django.urls import path
from home.views import home_view
from django.shortcuts import redirect
from django.urls import reverse


urlpatterns = [
    path('home/', home_view, name='home_page'),
    path('', lambda request: redirect(reverse('home_page'))),
]
