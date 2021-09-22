from django.http import HttpResponse

# Create your views here.
def index(request):
    content = "Hi! there. Please enter the number of pops."
    return HttpResponse(content)