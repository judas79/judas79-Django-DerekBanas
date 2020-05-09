# L3 this import was already here
from django.contrib import admin

# L3 Register your models that will sho up here.
# L4 add choice option to admin panel
from .models import Question, Choice


# L5 display choices for questions on same page two ways, either pass in
# StackedInline or TabularInline
class ChoiceInline(admin.TabularInline):

    # the model we will use for this is Choice
    model = Choice

    # define how many empty spaces below each choice
    extra = 1



# L5 display question on admin page,
class QuestionAdmin(admin.ModelAdmin):

    # L5 publishing date and text question in the admin/polls/question editing pages
    #fields = ['pub_date', 'question_text']

    # L5 break up the data in blocks, question text, a block separator, with Date Information text,
    # then Date dropdown selector then Time selector, all collapsed with a 'show' button
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information',
                  {'fields': ['pub_date'],
                   'classes': ['collapse']}),
                 ]
    # L5 implement choice class in QuestionAdmin
    inlines = [ChoiceInline]

    # L5 display date published and if it was recent or not
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # Add a filter box that lets the user sort by pub_date
    list_filter = ['pub_date']

    #  Allow the user to search by question text
    search_fields = ['question_text']

# L3 register Question to show up in the admin portion of the site
# L4 QuestionAdmin- reverses the order of the date, and question display, which one is above and below
# in the admin/polls/question editing pages
admin.site.register(Question, QuestionAdmin)

# L4 register Choice to show up in admin panel
admin.site.register(Choice)
