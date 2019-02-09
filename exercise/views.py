from django.shortcuts import render,get_object_or_404,redirect
from .models import MathProblem,MathPoint
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

# Create your views here.
# 知识点列表
# tmp_ans={1:['aaa','bbb']}
ques_lst=[
	{'题目编号':1,'答题内容':'aaa'},
	{'题目编号':10,'答题内容':None},
	{'题目编号':20,'答题内容':None},
	{'题目编号':30,'答题内容':None},
	{'题目编号':40,'答题内容':None},
	{'题目编号':50,'答题内容':None},
	{'题目编号':60,'答题内容':None},

	# {'题目编号':10,'答题内容':None,'答案':None},
	# {'题目编号':20,'答题内容':None,'答案':None},
	# {'题目编号':30,'答题内容':None,'答案':None},
	# {'题目编号':40,'答题内容':None,'答案':None},
	# {'题目编号':50,'答题内容':None,'答案':None},
	# {'题目编号':60,'答题内容':None,'答案':None},
]
tmp_ans={}
# ques_lst=[1,10,15,20,50]
@login_required(login_url='myauth:登录')
def points_list(request):
    point_list = MathPoint.objects.all()
    paginator = Paginator(point_list, 25) # Show 25 contacts per page
 
    page = request.GET.get('page')
    try:
        point = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        point = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        point = paginator.page(paginator.num_pages)
		
    return render(request, 'exercise/points_list.html', {'point': point})

# 题目列表
@login_required(login_url='myauth:登录')
def get_point_ques(request,point_id):
	need_point=get_object_or_404(MathPoint,id=point_id)
	# need_point=MathPoint.objects.get(id=point_id)
	ques_list=MathProblem.objects.filter(ques_points__contains=need_point)
	paginator = Paginator(ques_list, 25) # Show 25 contacts per page
	
	page = request.GET.get('page')
	try:
		ques = paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		ques = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		ques = paginator.page(paginator.num_pages)
	content={'ques':ques}
	return render(request,'exercise/point_ques.html',content)

# 题目
@login_required(login_url='myauth:登录')
def get_ques(request,ques_id):
	need_ques=get_object_or_404(MathProblem,id=ques_id)
	need_ques.ques=need_ques.ques.split("\t")
	need_ques.answer=need_ques.answer.split("\t")
	content={'题目':need_ques,'显示答案':True}
	return render(request,'exercise/ques.html',content)

#做题
@login_required(login_url='myauth:登录')
def ans_ques(request,ans_ques_id):
	tmp_id=int(ans_ques_id)-1
	need_ques=get_object_or_404(MathProblem,id=ques_lst[tmp_id]['题目编号'])
	need_ques.ques=need_ques.ques.split("\t")
	# need_ques.answer=need_ques.answer.split("\t")
	# ques_lst[tmp_id]['答案']=need_ques.answer

	if request.method=="POST":
		ques_lst[tmp_id]['答题内容']=request.POST["输入答案"]
		return redirect('/ans_ques/'+str(int(ans_ques_id)+1))
		
	else:
		if ques_lst[tmp_id]['答题内容'] is None:
			content={'题目':need_ques,'开始作答':True}
		else:
			content={'题目':need_ques,'开始作答':True,'上次答案':ques_lst[tmp_id]['答题内容']}


	return  render(request,'exercise/ques.html',content)



# 对答案
@login_required(login_url='myauth:登录')
def check_ans(request,ans_ques_id):
	tmp_id=int(ans_ques_id)-1
	need_ques=get_object_or_404(MathProblem,id=ques_lst[tmp_id]['题目编号'])	
	need_ques.ques=need_ques.ques.split("\t")
	need_ques.answer=need_ques.answer.split("\t")
	content={'题目':need_ques,'检查答案':True,'我的答案':ques_lst[tmp_id]['答题内容']}
	return  render(request,'exercise/ques.html',content)

# # 查看做题结果
# def ans_result(request):
# 	return render()




