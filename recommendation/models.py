from django.db import models

# Create your models here.
class WrongQues(models.Model):
	stuId = models.CharField(max_length=8)
	quesId = models.CharField(max_length=8)

	class Meta:
		verbose_name_plural = "WrongQues"

	# def __str__(self):
	# 	return self.name
	
class RightQues(models.Model):
	stuId = models.CharField(max_length=8)
	quesId = models.CharField(max_length=8)

	class Meta:
		verbose_name_plural = "RightQues"

	# def __str__(self):
	# 	return self.name
