from django.shortcuts import render
from myauth.models import Student
from exercise.models import MathProblem,MathPoint
from .models import WrongQues,RightQues
from django.contrib.auth.decorators import login_required



# Create your views here.



@login_required(login_url='myauth:登录')
def RecommendQues(request,userId):

	return render(request,'')



#推荐算法
