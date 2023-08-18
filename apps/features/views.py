from django.shortcuts import render


def features(request):
    return render(request, 'features.html')
