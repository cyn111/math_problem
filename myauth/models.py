from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
	user=models.OneToOneField(User,  on_delete=models.CASCADE)
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
	nickname = models.CharField(max_length=50, blank=True)
	birthday=models.DateField(blank=True)
	sex = models.CharField(max_length=32,choices=gender,default='男')
	classroom= models.CharField(max_length=32,choices=room,default='1班')
	# c_time = models.DateTimeField(auto_now_add=True)


	class Meta:
		verbose_name_plural = "Student"

	def __str__(self):
		return self.user.username


