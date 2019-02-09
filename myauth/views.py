from django.shortcuts import render,redirect
from django.contrib.auth import authenticate ,login ,logout
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from .forms import StudentCreationForm,StudentChangeForm
from .models import Student
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash 
# Create your views here.

def home(request):
	return render(request,'myauth/home.html')

def mylogin(request):
	if request.method=="POST":
		user=authenticate(request, username=request.POST['用户名'],password=request.POST['密码'])
		if user is None:
			return render(request,'myauth/login.html',{'error':'用户名不存在'})
		else:
			login(request,user)
			return redirect('myauth:主页')
	else:
		return render(request,'myauth/login.html')

def mylogout(request):
	logout(request)
	return redirect('myauth:主页')

def register(request):
	if request.method=="POST":
		register_form=StudentCreationForm(request.POST)
		if register_form.is_valid():
			register_form.save()
			user=authenticate(username=register_form.cleaned_data['username'],password=register_form.cleaned_data['password1'])
			user.email=register_form.cleaned_data['email']
			Student(user=user,
				nickname=register_form.cleaned_data['nickname'],
				sex=register_form.cleaned_data['sex'],
				birthday=register_form.cleaned_data['birthday'],
				classroom=register_form.cleaned_data['classroom'],
			 ).save()
			login(request,user)
			return redirect('myauth:主页')
	else:
		register_form=StudentCreationForm()
	content={'注册表单':register_form}
	return render(request,'myauth/register.html',content)

@login_required(login_url='myauth:登录')
def user_center(request):
	if request.method=="POST":
		content={'user':request.user}
		return redirect('myauth:个人中心',content)

	else:
		return render(request,'myauth/user_center.html')

@login_required(login_url='myauth:登录')
def edit_profile(request):
	if request.method=="POST":
		change_form=StudentChangeForm(request.POST,instance=request.user)
		if change_form.is_valid():
			change_form.save()
			request.user.student.nickname=change_form.cleaned_data['nickname']
			request.user.student.sex=change_form.cleaned_data['sex']
			request.user.student.birthday=change_form.cleaned_data['birthday']
			request.user.student.classroom=change_form.cleaned_data['classroom']
			request.user.student.save()


			return redirect('myauth:个人中心')
	else:
		change_form=StudentChangeForm(instance=request.user)
	content={'编辑表单':change_form,'user':request.user}
	return render(request,'myauth/edit_profile.html',content)

@login_required(login_url='myauth:登录')
def change_password(request):
	if request.method=="POST":
		changepasswd_form=PasswordChangeForm(data=request.POST,user=request.user)
		if changepasswd_form.is_valid():
			changepasswd_form.save()
			return redirect('myauth:登录')
	else:
		changepasswd_form=PasswordChangeForm(user=request.user)
	content={'改密表单':changepasswd_form,'user':request.user}
	return render(request,'myauth/change_password.html',content)
