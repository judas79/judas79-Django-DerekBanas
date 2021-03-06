from django.db import models
# L2
import datetime
from django.utils import timezone


# Create your models here.

# L2 create question with tied in choices
class Question(models.Model):

    # define a database column with datatype CharField,
    # max length of character field entry
    question_text = models.CharField(max_length=200)

    # publish date field, and set up datetime to be more readable
    pub_date = models.DateTimeField('date published')

    # to get more details when returning an answer from this object
    def __str__(self):
        return self.question_text

    # see if the question was published recently or not
    def was_published_recently(self):

        # get current time, and return the current time
        # calculated by the code :

        now = timezone.now()

        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    # to display the publishing date in order
    was_published_recently.admin_order_field = 'pub_date'

    # changes True and False text in under heading Was Published Recently to green or red Icons
    was_published_recently.boolean = True

    # text above the True / False from Was Published Recently, to a shorter description
    was_published_recently.short_description = 'Published Recently'

        # L2
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# L2 different choices for our Questions
class Choice(models.Model):

    # define each choice is related to a single question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    # define text for our choice
    choice_text = models.CharField(max_length=200)

    # which is the most popular choice
    vote = models.IntegerField(default=0)

    # to get more details when returning an answer from this object
    def __str__(self):
        return self.choice_text

