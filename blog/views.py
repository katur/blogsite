from django.shortcuts import render


def posts(request):
    return render(request, 'posts.html', {})
