from django.http import HttpResponse

def danger_hook(request):
    return HttpResponse("This is the danger_hook page")
