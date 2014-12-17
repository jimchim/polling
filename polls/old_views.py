#unused code - hard way to write a view in Django

def index(request):
    question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'question_list': question_list}    
    #the key in this dictionary will be the global variables being passed into the template
    #in this case, we are passing a list of question object to the template.
    #the template we wrote will check if the quesiton_list variable is passed / exist there,
    #if so, it will print the questions as links to them with the question_text as the text for the links
    #if the variable is not defined, then it will equates 'No polls are available '
    
    #output = ', '.join([p.question_text for p in question_list])
    #return HttpResponse(output)

    #context = RequestContext(request, {            'question_list': question_list,     })
    #template = loader.get_template('polls/index.html') 
    #return HttpResponse(template.render(context))

    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    #return HttpResponse("You're looking at question %s." % question_id)


    #try:
        #question = Question.objects.get(pk = question_id) 
        #try to select an object from db using pk that matches the question_id
        #if found, assign it to var question

    #except Question.DoesNotExist:
        #raise Http404
        #if not found, raise Http404
    #return render(request, 'polls/detail.html', {'question': question})
        #the keyword argument(variable) here being passed to the template is named simply question
        #so we are going to just use this in the template, making it as simple as {{ question }}
        #to display the variable

    question = get_object_or_404(Question, pk=question_id) #try to get object with question_id as pk, if failed, raise 404
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):

    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/result.html',  {'question': question}) 
    #the dictionary object passed into the render function are argument that are used in the template


    """ #write the response here instead of returning a rendered template
    q = get_object_or_404(Question, pk = question_id)
    options = q.choice_set.all()
    response = "You're looking at the result of question %s: %s <br>"
    
    for option in options:
        text = option.choice_text
        votes = option.votes
        line = "<br>Choice Text: %s <br> Votes: %s <br>" % (text, votes)
        response += line

    response += "<br><a href = '/polls/%s'>Back to Question: %s</a>" % (q.id, q.question_text)

    return HttpResponse(response % (question_id, q.question_text))
    """

    #return HttpResponse("You're looking at the ReSuLt of question %s" % question_id)