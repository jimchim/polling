from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
#from django.template import RequestContext, loader    #will be using shortcuts.render instead
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from polls.models import Question, Choice

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'question_list'

    def get_queryset(self): 
    #this function is actually being used as a way to pass a list of object into the class
    #which will in turn be used to render the page with the template
    #so instead of added a model attribute to this class, the ListView class uses the get_quertset method
    #to get a list of objects to be work with.
        """Return the last five published questions - 
        questions that are scheduled to be published in the future will not be handled
        """
        #return Question.objects.order_by('-pub_date')[:5]
        return Question.objects.filter(
            pub_date__lte = timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Exclude any question that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte = timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/result.html'

def vote(request, question_id): 
    #this is not a page, this is a function that handles the data passed into it
    p = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = p.choice_set.get(pk = request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p, 
            'error_message': "You didn't select a choice.",
        })

    else:
        selected_choice.votes += 1
        selected_choice.save()
        #return HttpResponse(results(request, question_id))
        return HttpResponseRedirect(reverse('polls:results', args = (p.id,))) 

def new_question(request):
    newQuestionText = request.POST['question_text']
    newQuestion = Question(question_text = newQuestionText, pub_date = timezone.now())
    newQuestion.save()
    return HttpResponseRedirect(reverse('polls:index'))

def new_choice(request):
    newChoiceText = request.POST['choice_text']
    foreignKey = Question.objects.get(pk = request.POST['question_id'])
    newChoice =  Choice(question = foreignKey, choice_text = newChoiceText)
    newChoice.save()
    return HttpResponseRedirect(reverse('polls:detail', args = (request.POST['question_id']) ))