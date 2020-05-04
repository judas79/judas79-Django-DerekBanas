# L2 use HttpResponse to pass info back view
# from django.http import HttpResponse # commented out L4

# L3 locally '.' import from models
from .models import Question, Choice

# L3 renders a page when it is passed a template and any data required by the template ie index, detail, results
from django.shortcuts import render

# L3 handles 404 not found pages
from django.shortcuts import get_object_or_404

# L3 stops a form, once submitted, from submitting data twice
from django.http import HttpResponseRedirect

# L3 this module will allow us to return a url we can point to based on whatever the current question is
from django.urls import reverse

# L4 for use with generic views
from django.views import generic

# L4 get our timezone information
from django.utils import timezone

# Create your views here.

# L4 class IndexView, passed in .ListView, to display the list of questions
class IndexView(generic.ListView):

    # the templates directory location used for the list, pointer
    template_name = 'polls/index.html'

    # This 'defines' the question list we want to use
    context_object_name = 'latest_question_list'

    # L4 function, for listing our questions, using Question model by order of date, but only the last 5
    def get_queryset(self):
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('pub_date')[:5]

        #return Question.objects.order_by('-pub_date')[:5] # L4

# L4 class DetailView shows specifics of the question you want to see more about

class DetailView(generic.DetailView):

    # define model we will be using for the details
    model = Question

    # define the path directory to the template we will use
    template_name = 'polls/detail.html'

    # function, for listing our questions, using Question model by order of date, but only the last 5
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

# L4 class ResultView for the results of the question,
class ResultsView(generic.DetailView):

    # define model we will be using for the details
    model = Question

    # define the path directory to the template we will use
    template_name = 'polls/results.html'

# pass in request and specific question_id, return statement with question_id number
def vote(request, question_id):

    question = get_object_or_404(Question, pk=question_id)

    # Try to 'get' the selected radio button,
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    # We will hand particularly the Choice.DoesNotExist error
    except(KeyError, Choice.DoesNotExist):

        # Re-render the form if Choice.DoesNotExist error is true, get passed request for details page (template)
        # get passed in question, pass in error message "You..."
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice"
        })
    else:

        # If a choice was selected increment it in the DB
        # ERROR 'Choice' object has no attribute 'votes' so using vote for now
        selected_choice.vote += 1
        selected_choice.save()

        # Protect from data being sent twice if user clicks back
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))



'''
# L2 setup the index page here for the poll app
def index(request):
    return HttpResponse("<h2>You are in the polls index</h2>")

def index(request):
    # L3 Receive a list of 5 [:5] questions ordered by date.
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    # Define the name for the data to pass to the template
    context = {
        'latest_question_list': latest_question_list,
    }

    # Render the page in the browser using the template and data required by the template
    # pass in request, the location of our template polls/index.html, pass in context, the question list
    return render(request, 'polls/index.html', context)

# L3 setup the detail page to display questions and choices, pass in assigned id; for the poll app
def detail(request, question_id):
    # checks passed in id see if it exists, got to the page or open 404 if not
    question = get_object_or_404(Question, pk=question_id)

    # L3 render template, pas in request at page detail in the browser and pass in specific question
    return render(request, 'polls/detail.html', {'question': question})

# L3 setup the results page to display the Question results, pass in the id that is assigned; for the poll app
def results(request, question_id):
    # get the question using the id that was passed and 404 if not
    question = get_object_or_404(Question, pk=question_id)

    # pass in request, point to template 'results' pass information contained within question
    return render(request, 'polls/results.html',
                  {'question': question})
                  
'''