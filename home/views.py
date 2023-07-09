from django.shortcuts import render


def home_view(request):
    return render(request, 'home.html', {'page_name': 'My page'})
