from django.http import HttpResponse

def news(request):
    return HttpResponse("News page")
