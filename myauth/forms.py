from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms 

class StudentCreationForm(UserCreationForm):
	gender=(
		('男', '男'),
		('女', '女'),
		)

	room=(
		('1班', '1班'),
		('1班', '2班'),
		('1班', '3班'),
		('1班', '4班'),
		)
	nickname=forms.CharField(max_length=30,required=False)
	birthday=forms.DateField(required=False)
	sex = forms.CharField(max_length=32,widget=forms.widgets.Select(choices=gender))
	classroom= forms.CharField(max_length=32,widget=forms.widgets.Select(choices=room))


	class Meta:
		model=User
		fields=('username','password1','password2','email','nickname','birthday','sex','classroom')

class StudentChangeForm(UserChangeForm):
	gender=(
		('male', '男'),
		('female', '女'),
		)

	room=(
		('1', '1班'),
		('2', '2班'),
		('3', '3班'),
		('4', '4班'),
		)
	nickname=forms.CharField(max_length=30,required=False)
	birthday=forms.DateField(required=False)
	sex = forms.CharField(max_length=32,widget=forms.widgets.Select(choices=gender))
	classroom= forms.CharField(max_length=32,widget=forms.widgets.Select(choices=room))
	



	class Meta:
		model=User
		fields=('username','email','nickname','birthday','sex','classroom')

