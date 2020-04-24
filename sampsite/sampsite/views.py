# L2 use HttpResponse to pass info back view
from django.http import HttpResponse

# L2 for random number use
import random

# L2 get request from view, return response using HttpResponse
def hello_world(request):

    # this will be returned if http://localhost:8000/helloworld/ is entered in the browser, html tags <h1> also work
    return HttpResponse('<h1>Hello World!</h1>')

# L2 get request from view, for our root address
def root_page(request):

    # this will be returned if http://localhost:8000; Root Home Page
    return HttpResponse('<h2>Root Home Page</h2>')

# L2 user request a random number 0 - 100 from url or random_number default is 100
def random_number(request, max_rand=100):

    # get user number, turn it into an integer from a string entry
    random_num = random.randrange(0, int(max_rand))

    # get the string %s entered by the user and return %d the random number, get our different values (max_rand, random_num)
    msg = '<h1>Random Number Between 0 and %s : %d</h1>' % (max_rand, random_num)

    return HttpResponse(msg)
