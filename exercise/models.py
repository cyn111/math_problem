from django.db import models

# Create your models here.

class MathProblem(models.Model):
	title=models.TextField()
	ques = models.TextField()
	ques_type = models.TextField()
	answer = models.TextField()
	ques_points = models.TextField()
	
	


	class Meta:
		verbose_name_plural = "MathProblem"

	def __str__(self):
		return self.title

class MathPoint(models.Model):
	point = models.TextField()
	

	class Meta:
		verbose_name_plural = "MathPoint"

	def __str__(self):
		return self.point


