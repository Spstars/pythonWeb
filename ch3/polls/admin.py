from django.contrib import admin
from polls.models import Question,Choice


#테이블 형식이면 TabularInline , 쌓기 방 StackedInline
class ChoiceInline(admin.TabularInline):
    model=Choice
    extra=2

class QuestionAdmin(admin.ModelAdmin):
    #순서를 바꿔보자
    #fields=['pub_date','question_text']

    #시간 관련 접기
#fieldsets=[
#        ('Question statement',{'fields':['question_text']}),
#        ('Date information',{'fields':['pub_date'],'classes': ['collapse']}),
#    ]

    fieldsets=[
        (None ,{'fields':['question_text']}),
        ('Date information',{'fields':['pub_date'],'classes': ['collapse']}),
    ]
    inlines=[ChoiceInline] #choice 같이 보기
    list_display=('question_text','pub_date') #레코드 리스트 콜럼
    list_filter=['pub_date'] # 지정 필터에 사이드 추가
    search_fields = ['question_text'] #검색박스 추가

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)

# Register your models here.
