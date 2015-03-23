from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
#from django.http import Http404
#from django.template import RequestContext, loader
from django.core.urlresolvers import reverse

from .models import Greeting
from polls.models import Choice, Question

import requests
import os

# Create your views here.
def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print r.text
    times = int(os.environ.get('TIMES',3))
    return HttpResponse('<pre>' + r.text + '</pre>'+ 'Hello! ' * times)

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})


# polls project
def indexpolls(request):
    # not use django.shortcuts
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    #context = RequestContext(request, {
    #    'latest_question_list': latest_question_list,
    #})
    #return HttpResponse(template.render(context))

    # use django.shortcuts
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)  # at this time we don't need `HttpResponse`, `loader`, and `RequestContext`

def detail(request, question_id):
    #return HttpResponse("You're looking at question %s." % question_id)

    #try:
    #    question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404("Question does not exist")
    #return render(request, 'polls/detail.html', {'question': question})

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
