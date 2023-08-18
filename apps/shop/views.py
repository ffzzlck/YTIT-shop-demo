from django.shortcuts import render


def shop(request):
    return render(request, 'product.html')
