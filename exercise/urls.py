from django.urls import path,include
from . import views
app_name='exercise'
urlpatterns = [
    path('points_list/', views.points_list,name="知识点列表"),    
    path('ques_list/<point_id>/', views.get_point_ques,name="题目列表"),    
    path('ques/<ques_id>', views.get_ques,name="题目"),
    path('ans_ques/<ans_ques_id>', views.ans_ques,name="答题"),
    path('check_ans/<ans_ques_id>', views.check_ans,name="对答案"),

    # path('ans_ques/<ques_id>', views.ans_ques,name="做题结果"),


]
