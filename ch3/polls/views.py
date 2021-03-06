from django.shortcuts import render,get_object_or_404
from polls.models import Question,Choice
from django.urls import reverse
from django.http import HttpResponseRedirect

def index(request):
    lastest_question_list=Question.objects.all().order_by('-pub_date')[:5]
    context={'lastest_question_list': lastest_question_list}
    return render(request,'polls/index.html',context)


def detail(request,question_id):
    question=get_object_or_404(Question, pk=question_id)
    return render(request,'polls/detail.html',{'question':question})

def vote(request, question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        #설문 투표를 재 출력한다.
        return render(request,'polls/detail.html',{
            'question' : question,
            'error_message':"You didn't select a choice.",
        })
    else:
        selected_choice.votes+=1
        selected_choice.save()
        #post 데이터를 정상적으로 처리하였으면 HttpResponseRedirect를 호출해 처리
        return HttpResponseRedirect(reverse('polls:results',args=(question_id,)))

def results(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request, 'polls/results.html',{'question': question})
# Create your views here.
