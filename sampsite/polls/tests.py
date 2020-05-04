# L4 imports
import datetime
from django.utils import timezone
from . models import Question

# runs tests without affecting data, by creating temporary test database
from django.test import TestCase

# L4 this module will allow us to return a url we can point to based on whatever the current question is
from django.urls import reverse

# Create your tests here.
'''
# L4 We will create a class to test our Question method:
class QuestionMethodTests(TestCase):
    
    # same code we created in shell condensed into one
    def test_was_published_recently_with_future_question(self):

        # create a time, 30 days into the future
        time = timezone.now() + datetime.timedelta(days=30)

        # create future question, that has a publish date
        future_question = Question(pub_date=time)

        # to see if the future_question is false,  pass in .was_published_recently(),
        # we expect the answer to be False
        self.assertIs(future_question.was_published_recently(), False)


    #  L4 Return false if pub_date is older then 1 day

    def test_was_published_recently_with_old_question(self):
        # Should return false if pub_date is older then 1 day
        time = timezone.now() - datetime.timedelta(days=30)
        # creat an old question
        old_question = Question(pub_date=time)
        # test the old question
        self.assertIs(old_question.was_published_recently(), False)

    # L4 Return True if published within the last day

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=1)
        # set recent question within the hour
        recent_question = Question(pub_date=time)
        # define our test
        self.assertIs(recent_question.was_published_recently(),


    # Create a function that creates questions at a specified date
    def create_question(question_text, days):

        # get current time plus whatever day is passed in to this function
        time = timezone.now() + datetime.timedelta(days=days)

        # return this question object, with passed in question text using time created above
        return Question.objects.create(question_text=question_text,
                                       pub_date=time)
                                       
# for our temporary database, created by the 'TestCase' imported module
class QuestionViewTests(TestCase):

    # Test to see what happens if there are no questions to show
    def test_index_view_with_no_questions(self):

        # Get the client for index part of our polls app using namespace
        response = self.client.get(reverse('polls:index'))

        # Check the status code, like we did in shell, and we expect 200 back
        self.assertEqual(response.status_code, 200)

        # Verify that response contains this string
        self.assertContains(response, "No polls are available.")

        # Check if latest_question_list is empty
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    # Make sure questions with a, pub_date in past, are shown
    def test_index_view_with_a_past_question(self):

        # Create sample question in our temporary database; negative 30
        create_question(question_text="Past question.", days=-30)

        # Get client, using namespace using reverse, of our index
        response = self.client.get(reverse('polls:index'))

        # Verify that the question shows, locking for questions with 'Past question' in them
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    # Make sure questions with future pub_dates, don't show
    def test_index_view_with_a_future_question(self):

        # Create question, "Future question." by calling create_question, 30 days in the future
        create_question(question_text="Future question.", days=30)

        # Get client, using namespace, using module reverse, in the polls index
        response = self.client.get(reverse('polls:index'))

        # Verify response contains text'self.assertContains', "No polls are available."
        self.assertContains(response, "No polls are available.")

        # Verify that latest_question_list is empty
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    # Verify that if past and future questions exist that only past is going to show
    def test_index_view_with_future_question_and_past_question(self):

        # Create 2 questions using create_question, notice negative 30 for Past question
        create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)

        # Get client, using namespace, using reverse for index in polls
        response = self.client.get(reverse('polls:index'))

        # Verify that question list only contains the past questions '<Question: Past question.>'
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    # Make sure question list shows multiple questions
    def test_index_view_with_two_past_questions(self):

        # Create 2 questions using create_question, notice both are negative
        create_question(question_text="Past question 1.", days=-30)
        create_question(question_text="Past question 2.", days=-5)

        # Get client, using namespace, using reverse for index in polls
        response = self.client.get(reverse('polls:index'))

        # Verify that both questions show
        self.assertQuerysetEqual(
            response.context['latest_question_list'],

            # we are looking for both questions
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )
'''

# as before we will use TestCase to create a temporary database
class QuestionIndexDetailTests(TestCase):

    # 13 Make sure future question detail pages show 404
    def test_detail_view_with_a_future_question(self):

        # Create question
        future_question = create_question(question_text='Future question.', days=5)

        # Open url using the future question in the url
        url = reverse('polls:detail', args=(future_question.id,))

        # Get client response
        response = self.client.get(url)

        # Verify that it returns expected 404
        self.assertEqual(response.status_code, 404)

    # Verify that past questions show in detail, as in, be displayed
    def test_detail_view_with_a_past_question(self):

        # Create question, past question, its already been created
        past_question = create_question(question_text='Past Question.', days=-5)

        # Open url with past question
        url = reverse('polls:detail', args=(past_question.id,))

        # Get response
        response = self.client.get(url)

        # Verify the question shows
        self.assertContains(response, past_question.question_text)