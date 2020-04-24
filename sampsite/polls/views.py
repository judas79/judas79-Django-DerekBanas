# L2 use HttpResponse to pass info back view
from django.http import HttpResponse



# Create your views here.

# L2 setup the index page here for the poll app
def index(request):
    return HttpResponse("<h2>You are in the polls index")
