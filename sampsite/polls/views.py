# L2 use HttpResponse to pass info back view
# from django.http import HttpResponse

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

# Create your views here.
'''
# L2 setup the index page here for the poll app
def index(request):
    return HttpResponse("<h2>You are in the polls index</h2>")
    '''


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


# L3 setup the results page to display the Question results, pass in the id that is assigned; for the poll app
def results(request, question_id):
    # get the question using the id that was passed and 404 if not
    question = get_object_or_404(Question, pk=question_id)

    # pass in request, point to template 'results' pass information contained within question
    return render(request, 'polls/results.html',
                  {'question': question})


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





        # Protect from data being sent twice if user clicks back
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# L3 setup the detail page to display questions and choices, pass in assigned id; for the poll app
def detail(request, question_id):
    # checks passed in id see if it exists, got to the page or open 404 if not
    question = get_object_or_404(Question, pk=question_id)

    # L3 render template, pas in request at page detail in the browser and pass in specific question
    return render(request, 'polls/detail.html', {'question': question})
