from django.urls import path,include
from . import views
app_name='myauth'
urlpatterns = [
    path('', views.home,name="主页"),
    path('login/', views.mylogin,name="登录"),
    path('logout/', views.mylogout,name="登出"),
    path('register/', views.register,name="注册"),
    path('user_center/', views.user_center,name="个人中心"),
    path('user_center/edit_profile', views.edit_profile,name="编辑个人信息"),
    path('user_center/change_password', views.change_password,name="修改密码"),



]
