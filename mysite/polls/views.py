
#from django.http import HttpResponse
from django.db.models import F
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Choice, Question
from django.urls import path
from django.urls import reverse
# from django.template import loader
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[0:5]
    # template = loader.get_template("polls/index.html")
    hail = [0,2,4,5]
    context = {"hail":hail,"latest_question_list":latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,"polls/detail.html",{"question":question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request,"polls/detail.html",{"question":question,"error_message":"You didnt select a chioce."})
    else:
        selected_choice.votes=F("votes")+1
        selected_choice.save()
        
        return HttpResponseRedirect(reverse("polls:results",args=(question_id)))
    